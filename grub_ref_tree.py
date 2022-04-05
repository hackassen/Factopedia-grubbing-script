import requests
from bs4 import BeautifulSoup as bs
import time, sys
import pandas as pd

import init


'''
    grub the tree of refs to endpoint pages
    tree twig contains url, parent url and some twig specific info
'''

import etc.incoms as incoms
import my_requests
from etc.ref_tree import refnav


def getref_tree(tree, url, prop_row=dict(), prop_list=list(), level=0):
    prop_row_=prop_row.copy()

    #print(f'url: {url}, prop_row_: {prop_row_}')
    print(f'url: {url}')
    
    if level==len(tree): # exit if there is no more decsendents
        prop_row_.update({'url':url})
        prop_list.append(prop_row_)
        return

    row=tree[level]
    resp=requests.get(url, headers=incoms.headers)
    soup=bs(resp.content, 'html.parser')
    lnks=soup.select(row['links'])
    if not lnks or not len(lnks):
        print(f'!!Warning: getref_tree: no links found for css:{row["links"]} on URL: {url}. Check etc/ref_tree.py settings.')
        return

    # page addons managing
    if 'addons' in row:
        for addon_row in row['addons']:
            try:
                el=soup.select_one(addon_row['css'])
                if not el:
                    print(f"!!Warning: Addon  {addon_row['name']} (css: {addon_row['css']}) fetching error on {url}")
                    continue
                if addon_row['attr']=='text': addon_val=el.getText()
                else: addon_val=el.attrs[addon_row['attr']]
                prop_row_.update({addon_row['name']:addon_val})
                
            except AttributeError as ex:
                print(f"!!Warning: Addon fetching error: {ex} no {url}. Check etc/ref_tree.py settings.")
                continue
                    
    #stopi=0
    for lnk in lnks:

        #!!!
        #if stopi>5: break
        #else: stopi+=1
        
        prop_row_.update({row['link_tag']:lnk.getText()})        
        url_=lnk.attrs['href']
        getref_tree(tree, url_, prop_row_, prop_list, level+1)

        # having a little nap
        my_requests.waitabit(incoms.sleep_interval[0], incoms.sleep_interval[1])
        
    return prop_list

if type(refnav) is list:
    ref_table=getref_tree(refnav, incoms.base_url)
else:
    ref_table=refnav();
    
#print(ref_table)


# converting refs to panas DataFrame
reftable=pd.DataFrame(ref_table)

#saving refs to file
reftable.to_csv(incoms.project_outdir+'refs.csv', sep=';', index=False)

    
print(' Grubbing ref tree finished.')
