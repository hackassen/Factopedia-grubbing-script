'''
    columns table creation
'''

import sys, re
import pandas as pd
import numpy as np
import etc.columns
from etc.types_and_units import units, pos

api_wrapper_dir='../api/python/factopedia';
if not api_wrapper_dir in sys.path:
    sys.path.insert(0, api_wrapper_dir)
    
from base import Factopedia
import etc.upload_settings as uplsets
from incoms import *
import init
from my_execman import ExecMan

ExecMan.note('Process_cats_table start (columns table creation).')

lang='en'
wrapper = Factopedia(uplsets.token)


#name='Lens mount'
#f_response = wrapper.get_property_category(name=name, language='en')
#resp_obj=f_response.json()
#print(f'responce:{f_response}, \nJSON:{resp_obj}')
#id_=wrapper.retrieve_category_id(name)
#print(f'id:{id_}')
#sys.exit()


cats=pd.read_csv(project_outdir+"Categories2.csv", sep=';', index_col=0)
data=pd.read_csv(project_outdir+'Data2.csv', sep=';')

# adding new rows
cats=cats.append(pd.Series(None, name='cat_id'))
cats=cats.append(pd.Series(None, name='prop_id'))
cats=cats.append(pd.Series(None, name='unit'))
cats=cats.append(pd.Series(None, name='unit_id'))
cats=cats.append(pd.Series(None, name='type'))
cats=cats.append(pd.Series(None, name='pos'))

# intergity check
illegal_fields=set.difference(set(data.columns).difference(init.ignore_cats), set(cats.columns))
if len(illegal_fields):
    ExecMan.warning('Integrity check failed. Data2 and Categories2 columns missmatch.')

# deleting ignoring cats
cats.drop(columns=set(cats.columns).intersection(set(init.ignore_cats)), inplace=True)

for c in cats.columns:
    if (not c in units) or (not c in pos):
        ExecMan.warning(f'Integrity check failed for "{c}". Check "types_and_units.py" file')


# preparing the columns table
for i, v in cats.iteritems():

    if (i not in units) or (i not in pos):
        ExecMan.warning(f" Skipping '{i}'")
        continue;
        
    print(f'processing property: "{i}"...')
    #print(type(v["cat"]))

    if not pd.isnull(v['cat']):
        cat_id=wrapper.retrieve_category_id(name=v['cat'])
    else:
        cat_id=None
        
    print(f'> category name:{v["cat"]}')
    print(f'> category id:{cat_id}')
    cats.loc['cat_id', i]=cat_id

    type_=units[i][0]
    print(f'> type:{type_}')
    cats.loc['type', i]=type_
    
    unit=units[i][1]
    if unit:
        unit_id=wrapper.retrieve_unit_id(name=unit, unit_type=type_)
        print(f'> unit:{unit}')
        print(f'> unit id:{unit_id}')
        cats.loc['unit', i]=unit
        cats.loc['unit_id', i]=unit_id
    else:
        print('> No unit')
        
    prop_id=wrapper.retrieve_property_id(name=i, type_=type_)
    print(f'> property id:{prop_id}')
    cats.loc['prop_id', i]=prop_id
    
    cats.loc['pos', i]=pos.index(i)
    print(f'> pos:{pos.index(i)}')


cats.to_csv(project_outdir+'COLUMNS.csv', sep=';', index=True)
ExecMan.note(f'process_cats_table - finished')
