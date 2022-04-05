from bs4 import BeautifulSoup as bs
import bs4
import re
import etc.incoms as incoms

#from my_execman import ExecMan

# !!! почемуто не могу подключить модуль my_execman

#import sys
#print(sys.path)

'''
    here some project specific functions must be defined:
        * name (optionaly)
        * properties table - prop_val(prop_nm), prop_cat(prop_nm)
        * main_image (optionaly)
        * images list - imgs
        * list of auxillary information - addon
'''

# properties hairbrushing funcion
def prop_nm_hairbrush(val:str):
    val=re.sub('<[^>]+>|\\n|:', ' ', val)
    val=re.sub('\s{2,}', ' ', val).strip()

    #espacing residual html entities like '&amp;'
    val=bs(val, 'html.parser').text.strip('-').strip()

    return val

# properties hairbrushing funcion
prop_val_hairbrush=prop_nm_hairbrush

# properties fetching function
def get_props(soup:bs4.BeautifulSoup):
    fields=soup.select("table.specs td.table_cat")
    values=soup.select("table.specs td.table_cat+td")

    # adding type like 'model'
    fields.append('model')
    values.append(soup.select_one('ul.breadcrumbs li.current'))
    
    # adding type like 'product code'
    fields.append('product code')
    values.append(soup.find("b", text ='Product code: ').nextSibling)        
    
    return (fields, values)

# categories fetching function
def get_category(refel:bs4.element.Tag):
    try:
        cat_name=refel.findPrevious('th').getText().strip()
        if not len(cat_name):
            cat_name=refel.findPrevious('th').findPrevious('th').getText().strip()
        return cat_name
    except:
        return None        

# main image fetching function
def get_mainimg(soup:bs4.BeautifulSoup):
    return None

# other images fetching function
def get_images(soup: bs4.BeautifulSoup):
    img_arr=soup.select("div.gallery div.gallery-slide img.gallery-image")
    imgs=list()
    for img in img_arr:
        try:
            if img.has_attr('data-src'):
                lnk=img.attrs['data-src']
            else:
                lnk=img.attrs['src']

            lnk=incoms.base_url+lnk
            #print(f"---{lnk}")
            imgs.append(lnk)
        except BaseException as ex:
            print(f'!! Warning: image fetching error: {ex}')

    return imgs

# addons fetching
def get_addons(soup: bs4.BeautifulSoup, ref_row):
    addons=dict()
    try:
        pass
        #addons['manufacturer']=re.search('^[^\s]+',ref_row['name'])[0]
    except BaseException as ex:
        #ExecMan.warning(f'Manufacturer extraction error: {ex}')
        print(f'!! Warning: Manufacturer extraction error: {ex}')
    
    return addons
