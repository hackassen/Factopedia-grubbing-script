'''
    doing all the initial job.
'''
import etc.incoms as incoms
import sys, os

print(f'Initializing project "{incoms.project_name}"') 

#creating folders
if not os.path.exists(incoms.cache_dir): os.mkdir(incoms.cache_dir)
if not os.path.exists(incoms.rec_dir): os.mkdir(incoms.rec_dir)
if not os.path.exists(incoms.out_dir): os.mkdir(incoms.out_dir)
if not os.path.exists(incoms.project_outdir): os.mkdir(incoms.project_outdir)    
if not os.path.exists(incoms.img_dir): os.mkdir(incoms.img_dir)

#libraries including

mylibpath='../../../my_lib/';
if not mylibpath in sys.path:
    sys.path.insert(0, mylibpath)

ignore_cats={'Url', 'Img', 'url', 'img'}

MAX_IMAGES_COUNT=5
