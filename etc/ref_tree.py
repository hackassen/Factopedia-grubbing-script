from bs4 import BeautifulSoup as bs
import bs4
import re

import etc.incoms as incoms
import requests
from bs4 import BeautifulSoup as bs
import time, sys
import pandas as pd
import my_requests

'''
    here some project specific functions must be defined:
        * information how to reach endpoint pages and all necesary information on the way
'''

'''
    the list of dictionaries: {
                                'links': css_or_fun,
                                'link_text_tag': '',
                                addons:[{
                                    'css':css_or_fun,
                                    'attr':attr,
                                    'name':'',
                                    ...}],
                                ...}
'''
'''
# in these case it is a list
refnav=[
    {
        'links': 'ul.list-manufacturers li a',
        'link_tag': 'manufacturer',
        },
    {
        'links': 'div.content-area section ul li a',
        'link_tag': 'model',
        'addons':[
                {
                'css': 'header.entry-header h1',
                'attr':'text',
                'name': 'manufaturer_1'
                },
                {
                'css': 'header.entry-header p',
                'attr':'text',
                'name': 'country'
                },
            ]
        },
    ]
'''
# in these case it is a function
def refnav(prop_row=dict(), prop_list=list()):
    errors=list();
    url=incoms.base_url+"/laptop-finder"
    # getting the list of brands avalible
    resp=requests.get(url, headers=incoms.headers)
    soup=bs(resp.content, 'html.parser')
    lnks=soup.select("ul#pr4 li a")
    for l in lnks:
        brand=l.attrs['data-val'].strip()
        print(f"> processing brand: {brand}")
        last_nr=0
        dlast_nr=16
        while True:
            brand_url=incoms.base_url+f"/include/backend_filters.php?url=Brand={brand}&last_prod_nr={last_nr}&display_mode=grid"
            print(f"> processing brand url: {brand_url}")
            try:
                resp1=requests.get(brand_url)
                product_list_html=resp1.json()['products']
                soup1=bs(product_list_html, 'html.parser')
                lnks1=soup1.select("div.product>a:nth-child(1)")
                if not len(lnks1):
                    break
                for lnk1 in lnks1:
                    prod_url=incoms.base_url+lnk1.attrs['href']
                    print(f"  >> product url: {prod_url}")
                    prop_row=dict()
                    prop_row['brand']=brand
                    prop_row['url']=prod_url
                    
                    if prop_row in prop_list:
                        raise Exception("product already in the list")
                    
                    prop_list.append(prop_row)
                 
                last_nr+=dlast_nr

                my_requests.waitabit(incoms.sleep_interval[0], incoms.sleep_interval[1])
            except Exception as x:
                mess=f" !!! ERROR occured: {x}"
                errors.append(mess)
                print(mess)
                break
            
            #if last_nr > 100 : break
            #break

        #break;

                

    if len(errors):
        print("ERRORS:")
        for er in errors: print(er);
        
    return prop_list
    

    
