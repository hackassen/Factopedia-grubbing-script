#import etc.html_parse

base_url="https://www.laptoparena.net"
project_name='laptops/'

headers={
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    }

cache_dir='../cache/'
rec_dir='../rec/'
out_dir='../out/'
project_outdir=out_dir;#out_dir+project_name
img_dir=project_outdir+'img/'

sleep_interval=[0,0.5] # from, to
