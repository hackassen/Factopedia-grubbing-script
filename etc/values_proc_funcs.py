# user defined columns procession...
import pandas as pd
import sys, re


def custom_process(data:pd.DataFrame, str_:pd.Series, i:int):

    '''
    # Foundation date'
    prop_nm='Foundation century'
    val=str_[prop_nm]
    if not pd.isnull(val):
        century=year=None
        match_century=re.search('([0-9]{1,2}).*\scentury', val)
        match_BC=re.search('\sBC', val)
        match_year=re.search('([0-9]{4})', val)
        try:
            if match_century:            
                    century=int(match_century[1])
                    if match_BC:
                        century*=-1    
            elif match_year:
                year=int(match_year[1])
                century=year//100+1
                
            data.loc[i, 'Foundation century']=century
            data.loc[i, 'Foundation year']=year
        
        except BaseException as x:
            print(f'User proc error:{x}')
    '''

    # Power, hp
    prop_nm='Power, hp'
    val=str_[prop_nm]
    if not pd.isnull(val):
        power_hp=power_lbf=None
        match_hp=re.search('([0-9\,]+)\shorsepower', val)
        match_lbf=re.search('([0-9\,]+)\spound-force', val)
        if match_hp:
            power_hp=match_hp[1]
        if match_lbf:
            power_lbf=match_lbf[1]
            
        data.loc[i, 'Power, hp']=power_hp
        data.loc[i, 'Power, lbf']=power_lbf
        

