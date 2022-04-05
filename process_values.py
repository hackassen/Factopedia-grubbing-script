import sys, re
import pandas as pd
import numpy as np
from etc.columns import *
from incoms import *
from etc.values_proc import *
from etc.values_proc_funcs  import custom_process
import init
from my_execman import ExecMan

from bs4 import BeautifulSoup as bs

'''
    data values procession
'''

data=pd.read_csv(project_outdir+"Data1.csv", sep=';')
cats=pd.read_csv(project_outdir+'Categories1.csv', sep=';', index_col=0)


print(f'proccess_values - processing {len(data)} rows...')


'''
    !!! сделать красиво, с настройкой в etc
'''
#replacing No/Yes values to Flase, True
#cols=[
#      ]
#for col in cols:
#    try:        
#        data[col]=data[col].str.replace('^[Nn]o$', 'False', regex=True)
#        data[col]=data[col].str.replace('^N$', 'False', regex=True)
#        data[col]=data[col].str.replace('^[Yy]es$', 'True', regex=True)
#        data[col]=data[col].str.replace('^Y$', 'True', regex=True)
#        
#    except :
#        pass

#replacing 'None' values to ''
'''cols=['Reference card',
      ]
for col in cols:
    try:        
        data[col]=data[col].str.replace('^[Nn]one$', '', regex=True)
    except :
        pass
'''

'''
# !! CROTCHES
#replacing '&amp;' to '&' is a crotches need to perform normaly....
cols=[
    'Engine',
      ]
for col in cols:
    try:        
        data[col]=data[col].str.replace('\&amp;', '&', regex=True)
    except BaseException as ex:
        pass
'''

#espacing residual html entities like '&amp;'
#print('purging HTML from plain data')
#for col in data.columns:
#    data[col].apply(lambda val:bs(val, 'html.parser').text.strip('-').strip())
#print('HTML has been pureged/')

    
for i, str_ in data.iterrows():
#for i, str_ in data.loc[:50,:].iterrows():

    for nm in value_proc_settings:
        v=value_proc_settings[nm]

        if not pd.isnull(str_[nm]) :
            in_val=str(str_[nm])

            val=''
            #managing boolean fields
            if 'bool' in v:
                if(re.match(bool_YES_regex, in_val):
                   val='True'
                   #continue
                elif(re.match(bool_NO_regex, in_val):
                   val='False'
                   #continue
                        
            #replacing what need to be replaced..
            if 'repl' in v: in_val=re.sub(v['repl'], v['replto'], in_val)
                
            if 'list' in v: # this is a list
                match=re.findall(v['reg'], in_val)
                if 'unique' in v:
                    match=np.unique(match).tolist()
                    if 'sort' in v:
                        if 'precision' in  v:
                            if v['precision']==0:
                                match=np.sort([int(j) for j in match]).tolist()
                        else:
                            match=np.sort([float(j) for j in match]).tolist()
                        match=[str(j) for j in match]
                if 'capitalize' in v: match=[j.strip().capitalize() for j in match]                    
                    
                val=','.join([j.strip() for j in match])
            elif'range' in v: # this is a range
                match=re.search(v['reg'], in_val)
                match_single=re.search(v['regSingle'], str_[nm])
                if match:
                    val=match[1].replace(',','')+' - '+match[2].replace(',','')
                elif match_single:
                    val=match_single[1].replace(',','')+' - '+match_single[1].replace(',','')                
                                    
            elif 'precision' in v:
                match=re.search(v['reg'], in_val)
                if match:
                    try:
                        val=float(match[1].replace(',',''))

                        # multiplying Koeff 
                        if 'MultK' in v: val*=float(v['MultK'])
                            
                        if v['precision'] == 0:
                            val=round(val)
                        else:
                            val=round(val, v['precision'])
                    except BaseException as x:
                        #print(f' "{nm}" => {match[1]} exception:{x}')
                        ExecMan.error(f' "{nm}" => {match[1]} exception:{x}')

            elif'reg' in v: # just reg

                #print(f'{nm} => {in_val}')
                match=re.search(v['reg'], in_val)
                if match: val=match[1]
                #print(f'VALIN:{in_val}      VALOUT:{val}')
            
            data.loc[i, nm]=str(val).strip()

    #/ for ... in value_proc_settings

    # user defined column procession
    custom_process(data, str_, i)
        

# removing some useless columns
#data.drop(columns=columns_names.cols_to_delete, inplace=True)
#cats.drop(columns=columns_names.cols_to_delete.intersection(cats.columns), inplace=True)



#replacing '0' values to 'None'
cols=['Seats','Seats - business class', 'Seats - first class',]

for col in cols:
    try:        
        data[col]=data[col].str.replace('0', '', regex=True)
    except BaseException as ex:
        pass

# !! CROTCHES
#replacing engine type in the Engine field
bad_ending={'Piston', 'Jet',  	'Turbofan' ,'Turboshaft', 'Turboprop', 'Turbofans', 'Other', 'Turbine', 'turboprop', 'turbofan', 'propeller', 'Stroke',}
for en in bad_ending:
    data['Engine']=data['Engine'].str.replace(en+"$", '', regex=True)



# saving to file
data.to_csv(project_outdir+'Data2.csv', sep=';', index=False)
cats.to_csv(project_outdir+'Categories2.csv', sep=';', index=True)
 
print(f'proccess_values - finished')
