from spn.models import *
from pandas_ods_reader import read_ods
import os, shutil

"""

How to use this script:

DON'T 
DON'T
DON'T
– there's now a manage.py command that does the same thing. This file will get deleted.

































1. Edit INPUT_ODS_FILE var. 
    ---> path must be relative to the location of manage.py, or absolute

2. Edit the IMG_SET_NAME and IMG_SET_SLUG vars
	---> SLUG var must contain no spaces

2. enter the django shell    
    --->    $ python manage.py shell

3. run the script from there 
    --->     >>> exec(open('spn/import_img-set.py').read())

"""


# Edit these vars

INPUT_ODS_FILE = "spn/img-set-ODS/feline.ods"
INPUT_STIM_DIR = "spn/img-set-ODS/feline-stimuli/"
IMG_SET_NAME = "Types of cats"
IMG_SET_SLUG = "cats"



# Leave the rest alone!
"""
STATIC_DIR = "static/spn/img/"

if os.path.isfile(INPUT_ODS_FILE):
	print("file is file")
	imgset = SpnPictureSet.objects.create(name=IMG_SET_NAME, slug=IMG_SET_SLUG)
	df = read_ods(INPUT_ODS_FILE)
	for i, row in df.iterrows():
		print(row['FileName'])
		imginst = SpnPicture.objects.create(
			filename=row['FileName'], 
			sort_order=i,
			description=row['description'],
			source=row['source']
		)
		imginst.save()
		imgset.pictures.add(imginst)
		shutil.copy(
			f"{INPUT_STIM_DIR}{row['FileName']}", 
			f"{STATIC_DIR}{row['FileName']}"
		)
	imgset.save()

else:
	print("file not file")
	print(INPUT_ODS_FILE)

"""
