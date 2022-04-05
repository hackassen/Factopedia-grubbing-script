import pandas as pd
from etc.columns import *
from etc.columns_tosum import *
from etc.incoms import *

import init
from my_execman import ExecMan
import sys
import my_process

'''
    columns reanaming, deleting, adding, hairbrushing ...
'''

print(f'proces_names running - column names hairbrushing...')


#data=pd.read_csv(project_outdir+"Data.csv", sep=';', low_memory=False)
#!!!
data=pd.read_csv(project_outdir+"Data.trim.csv", sep=';', low_memory=False)

cats=pd.read_csv(project_outdir+'Categories.csv', sep=';', index_col=0, low_memory=False)
#sys.exit()



def add_column(tables, after, name, ofset=0):
    try:
        for table in tables:
            nones=[None for i in range(len(table))]
            n=table.columns.get_loc(after)
            table.insert(loc=n+1+ofset, column=name, value=nones)
    except BaseException as x:
        ExecMan.error(f'add_column: {x}')



#trimming columns
cols_to_del=set(data.columns.to_list()).difference(set(cols_to_stay))
data.drop(columns=list(cols_to_del), inplace=True)

cols_to_del=set(cats.columns.to_list()).difference(set(cols_to_stay))
cats.drop(columns=list(cols_to_del), inplace=True)

# addind some extra colunms
for val in cols_to_add:     
    add_column([data, cats] ,val['after'], val['name'], 0)
    if 'cat' in val:
        cats.loc['cat',val['name']]=val['cat']
    else:
        cats.loc['cat',val['name']]=cats.loc['cat', val['after']]

#summing columns
for i in range(len(data)):
    for c in cols_to_summ:
        data.loc[i, c]=next((v for v in data.loc[i, list(cols_to_summ[c])] if not pd.isnull(v)), None)

#   deleting columns been summed
for c in cols_to_summ:
    for cc in cols_to_summ[c]:
        data.drop(columns=cc, inplace=True)
        cats.drop(columns=cc, inplace=True)

# renaming columns
repl_nms=cols_to_remane
for c in repl_nms.keys():
    if not c in data.columns:
        #print(f'   > !!Warning: "{c}" doesnt exist in data')
        Man.warning(f"'{c}' doesnt exist in data")

data.rename(columns=repl_nms, inplace=True)
cats.rename(columns=repl_nms, inplace=True)

# removing some useless columns
#data.drop(columns=columns_names.cols_to_delete, inplace=True)
#cats.drop(columns=columns_names.cols_to_delete.intersection(cats.columns), inplace=True)


# sorting cats
cats.sort_values(by='cat', axis=1, inplace=True)


# Hairbrashing column names and
ind=list()
for i in range(len(data.columns)):
    nm=data.columns[i]
    nm=my_process.SmartStringCatitalise(nm)
    ind.append(nm)    
data.columns=ind

ind=list()
for i in range(len(cats.columns)):
    nm=cats.columns[i]
    #if nm[0].islower():
    nm=nm.capitalize()
    ind.append(nm)    
cats.columns=ind

#Capitalizig cats
cats.loc['cat',:]=cats.loc['cat',:].str.capitalize()

# Filling cats by default
for i, v in cats.loc['cat', :].iteritems():
    if pd.isnull(v):
        cats.loc['cat', i]='General'
		
# '&', '+' symbil replacing...
data.columns=data.columns.str.replace('[\&]', 'and')
cats.columns=cats.columns.str.replace('[\&]', 'and')
data.columns=data.columns.str.replace('[\+]', ' plus ')
cats.columns=cats.columns.str.replace('[\+]', ' plus ')
cats.loc['cat', :]=cats.loc['cat', :].str.replace('&', 'and')


# saving to file
data.to_csv(project_outdir+'Data1.csv', sep=';', index=False)
cats.to_csv(project_outdir+'Categories1.csv', sep=';', index=True)

print('proces_names done')


