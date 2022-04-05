import pandas as pd
import sys
import numpy as np
import requests
from pprint import pprint
import re

api_wrapper_dir='../api/python/factopedia';
if not api_wrapper_dir in sys.path:
    sys.path.insert(0, api_wrapper_dir)
    
from base import Factopedia
from etc.upload_settings import *
from incoms import *
from pathlib import Path

lang='en'
wrapper = Factopedia(token)
'''
# filling the "aircrafts" category by emply values, needed just once
data_cols=pd.read_csv(project_outdir+'COLUMNS.csv', sep=';', index_col=0)
properties=list()

for it in data_cols.columns:
    prop_dict={
    'id':data_cols.loc['prop_id', it],
    'type':data_cols.loc['type', it],
    'value':''
    }
    if not pd.isnull(data_cols.loc['unit_id', it]):
        prop_dict['unit_id']=data_cols.loc['unit_id', it]

    if not pd.isnull(data_cols.loc['cat_id', it]):
        prop_dict['category_id']=data_cols.loc['cat_id', it]

    if not pd.isnull(data_cols.loc['pos', it]):
        prop_dict['order_by']=data_cols.loc['pos', it]

    properties.append(prop_dict)

pprint(f'properties={properties}')
#f_response = wrapper.create_object('Cities_test1', 'en', parent_id=parent, properties=properties)
    
id_=copters_id
f_response = wrapper.update_object(id_, properties=properties)
print(f'Response: {f_response},\n Resopne JSON: {f_response.json()}')
sys.exit()
'''

#applparents=pd.read_csv(project_outdir+'upplparents.csv', sep=';')

responces=list()

# loading the data from file
data=pd.read_csv(project_outdir+'Data2.csv', sep=';', dtype=str)
data_cols=pd.read_csv(project_outdir+'COLUMNS.csv', sep=';', index_col=0)

# uploading the data to the server
atypes_id={'Airplanes': airplanes_id, 'Helicopters': copters_id}

for raw in data.loc[([627, 702, 717, 742, 757, 848, 876]),:].iterrows(): #going through all the data
#for raw in data.loc[578:,:].iterrows(): #going through all the data
#for raw in data.iterrows(): #going through all the data
    #atype=raw[1]['Aircraft_type']
    #manuf=raw[1]['Manufacturer']    

    '''
    # getting the parent
    paridsearch=applparents[(applparents['parent']==atypes_id[atype]) & (applparents['name']==manuf)]
    if len(paridsearch): # there is a parent in the lookup table
        manuf_id=paridsearch.loc[0, 'id']
        print(f' Found manuf id: {manuf_id} for {manuf} in  {atype}') 
    else:
        # creating new manufacturer
        print(f' Creating manufactirer "{manuf}" in "{atype}"') 

        resp = wrapper.create_object(
        name=manuf,
        language=lang,
        parent_id=atypes_id[atype],
        
        # some croutches....
        properties=[
            {
            'id':676, # Country
            'type':'text',
            'value':raw[1]['Country'],
            'order_by':1,
            }])
    
        responce_json=resp.json()
        print(f"   Creating manufactirer {manuf} result {resp} , \n{responce_json}")
        manuf_id=responce_json['id']
        paridsearch=paridsearch.append({'id':manuf_id, 'name':name, 'parent':atypes_id[atype]}, ignore_index=True)    
    
    print(f" Manufactirer id : {manuf_id}")

    # / getting the parent
    '''
    atype=raw[1]['Aircraft_type']
    if not atype in atypes_id:
        print(f'{raw[0]} skipping as atype is {atype}')
        continue
    
    parent_id=atypes_id[atype]
    
    name=raw[1]['Model']
         
    # creating object propety list
    properties=list()
    
    #going through the data columns (attributes)
    for field in raw[1].drop(labels=['Url', 'Img', 'Aircraft_type']).iteritems():
        p_name=field[0]
        p_val=field[1]
        # making property list
        if not p_val or pd.isnull(p_val):
            continue

        # если значение - массив, подготовка
        if data_cols.loc['type', p_name]=='array':
            p_val=p_val.lower().split(',')
            
        prop_dict={
            'id':data_cols.loc['prop_id', p_name],
            'type':data_cols.loc['type', p_name],
            'value':p_val,
            'order_by':data_cols.loc['pos', p_name],
            }
        if not pd.isnull(data_cols.loc['unit_id', p_name]):
            prop_dict['unit_id']=data_cols.loc['unit_id', p_name]

        if not pd.isnull(data_cols.loc['cat_id', p_name]):
            prop_dict['category_id']=data_cols.loc['cat_id', p_name]

        properties.append(prop_dict)
    #/for
        
    # printing property list
    #for p in properties:
    #    print(p)
    #sys.exit()

    #uploading images
    if not pd.isnull(raw[1]['Img']):
        images_=[img_dir+im for im in raw[1]['Img'].split('\n')[:max_img_count] if Path(img_dir+im).stat().st_size <= max_img_size]
    else:
        images_=[]
    #print(f' images={images_}')
    #sys.exit()
    
    #aliases
    '''
    aliases=list()
    try:
        aliases_nms=['Model number', 'Alternate model number(s)']
        for al in aliases_nms:
            if not pd.isnull(raw[1][al]):
                aliases.append(raw[1][al])
    except BaseException as x:
        print(f' !!! aliases exception: {x}')
    '''
    #adding (uploading) object

    while (True):
        f_response = wrapper.create_object(
            name,
            lang,
            parent_id=parent_id,
            images=images_,
            #main_image=images_[0],
            #aliases=aliases,
            properties=properties
        )    
        #f_response=wrapper.update_object(95944, properties=properties, main_image=images_[0],)
        if f_response.reason == 'Payload Too Large':
            if len(images_)>1:
                images_=images_[:-1]
                print(f'>> {raw[0]} - decreasing image count bue to too lage payload. There are {len(images_)} images.')
                continue

        # ! here needed to provide for another attempt in the case of 502: 'Bad Gateway'..
        
            
        break
        
    # responces collection
    resp_dict=dict()
    resp_dict['i']= raw[0]    
    resp_dict['code']=str(f_response.status_code)
    mess='No message'
    
    try:
        resp_dict['reason']=str(f_response.reason)
        mess=f_response.json()[0]['message']
        resp_dict['message']=mess
    except BaseException as x:
        #print(f'{raw[0]}: {x}')
        pass
    
    responces.append(resp_dict)

    print(f'{raw[0]}: {f_response.status_code}: {f_response.reason} : {mess}')    
    #responce_json=f_response.json()
    #print('Response JSON:', responce_json, '\n')
    
    # for reporting purpurses only 
    #print(raw[1]['Url'])
    #print(responce_json['url'])

#paridsearch.to_csv(project_outdir+'upplparents.csv', sep=';', index=False)
pd.DataFrame(responces).to_csv('responces.csv', sep=';', index=True)      
print('> JOB DONE.')
