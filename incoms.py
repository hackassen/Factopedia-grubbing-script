import etc.html_parse

base_url="https://aerocorner.com/manufacturers/"
project_name='aircorner/'

'''
headers={
    'scheme': 'https',
    'accept': '*/*',
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    #'content-type': 'application/json',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
'''
headers={
    'accept-language': 'en-US,en;q=0.9',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }

cache_dir='cache/'
rec_dir='rec/'
out_dir='out/'
project_outdir=out_dir+project_name
img_dir=project_outdir+'img/'

sleep_interval=[0,1] # from, to
