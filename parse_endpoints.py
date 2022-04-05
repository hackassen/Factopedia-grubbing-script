import requests
from bs4 import BeautifulSoup as bs
import time, os
import pandas as pd
import sys
import re

import init
import etc.incoms as incoms
from etc.incoms import sleep_interval
from my_execman import ExecMan
import etc.html_parse as customfun

import my_requests
import etc.ref_tree as reftree

'''
    endpoint page parsing
'''

parse_errors=list()
prop_list=list()
cats=dict()

data=list()
cats=dict()

refs=pd.read_csv(incoms.project_outdir+'refs.csv', sep=';')

#adding properties from refs tree
addon_nms=list()
if type(reftree.refnav) is list: # refnav was defined as list
    for row in reftree.refnav:
        if 'link_tag' in row:
            addon_nms.append(row['link_tag'])
        if 'addons' in row:
            for addonrow in row['addons']:
                addon_nms.append(addonrow['name'])
else: # refnav was defined as function
    #just add all ref columns that not in ignore_cats    
    #for fl in set(refs.columns).difference(set(init.ignore_cats)):
    #    addon_nms.append(fl)
    pass

#sys.exit()


#for i, ref_row in refs.loc[:1].iterrows():
for i, ref_row in refs.iterrows():
    try:
        imgs=list()
        
        url=ref_row['url']
        print(url)
        
        #resp=requests.get(url, headers=incoms.headers)
        resp=my_requests.get(url, headers=incoms.headers)
        soup=bs(resp.text, 'html.parser')

        fields, values = customfun.get_props(soup)

        if len(fields)!=len(values):
            parse_errors.append({'url':url, 'reason': 'fields len not equal to values len'})    
            #print('!!! Warring: fields len not equal to values len. ')
            ExecMan.warning('fields len not equal to values len.')
            continue

        # getting images
        main_img=customfun.get_mainimg(soup)
        if main_img: imgs.append(main_img)

        imgs+=customfun.get_images(soup)
           
        #saving images to file
        img_nms=list()
        for lnk in imgs[:init.MAX_IMAGES_COUNT]:	
            try:
                img_nm=re.search('[^/]+$', lnk)[0]
                img_nms.append(img_nm)
                if img_nm in os.listdir(incoms.img_dir): continue
                with open(incoms.img_dir+img_nm, 'wb') as out_file:
                    out_file.write(requests.get(lnk).content)
            except BaseException as ex:
                #print(f'!!   Warning: Image saving error: {ex}')
                ExecMan.warning(f'Image saving error: {ex}')
                img_nms.remove(img_nm)
                
        img_nms='\n'.join(img_nms)    
        
        prop_row={
            'url':url,
            'img': img_nms,    
            }

        #adding properties from refs tree
        for addon_nm in addon_nms:
            prop_row[addon_nm]=ref_row[addon_nm]
            #!!! not tested code !!!
            cats[addon_nm]=None
        
        prop_row.update(customfun.get_addons(soup, ref_row))
        
        for i in range(len(fields)):
            # properties fields and values hairbrushing
            field=customfun.prop_nm_hairbrush(str(fields[i]))
            value=customfun.prop_val_hairbrush(str(values[i]))
            prop_row[field]=value    

            # getting categories
            cat=customfun.get_category(fields[i])
            
            # !! better to adjust it in etc
            if not cat: cat='General'
            
            if field not in cats:
                cats[field]=cat

        prop_list.append(prop_row)

        # sleeping for a few seconds
        my_requests.waitabit(sleep_interval[0], sleep_interval[1])
        
    except BaseException as ex:
        mess=f" !!! Some exception occured:{ex}"
        print(mess)
        parse_errors.append({'url':url, 'reason': str(ex)})    
        continue;

pd.DataFrame(prop_list).to_csv(incoms.project_outdir+'Data.csv', sep=';', index=False)
pd.DataFrame(parse_errors).to_csv(incoms.project_outdir+'parse_errors.csv', sep=';', index=False)
pd.DataFrame(data=[cats], index=['cat']).to_csv(incoms.project_outdir+'Categories.csv', sep=';', index=True)

print(' Parsing endopints finished.')

if len(parse_errors):
    print(f" During parsing errors occured: {len(parse_errors)}. Detail in file 'parse_errors.csv'.")

ExecMan.report()
