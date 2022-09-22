from vidnar.models import *
from pandas_ods_reader import read_ods
import os, shutil


"""

How to use this script:

DON'T
DON'T
DON'T !!! --> use the management command instead






































1. Edit INPUT_ODS_FILE var. 
    ---> path must be relative to the location of manage.py, or absolute

2. Edit the VID_SET_NAME and VID_SET_SLUG vars
	---> SLUG var must contain no spaces

2. enter the django shell    
    --->    $ python manage.py shell

3. run the script from there 
    --->     >>> exec(open('vidnar/import_vid-set.py').read())

"""

"""
# Edit these vars

INPUT_ODS_FILE = "vidnar/vid-set-ODS/mpi-cut-n-break.ods"
INPUT_STIM_DIR = "vidnar/vid-set-ODS/mpi-cut-n-break/"
VID_SET_NAME = "Cut and Break Videos"
VID_SET_SLUG = "cutnbreak-vids"

	# !!! # from the next two lines, it must be either one or the other
#VID_SET_TARGET_LANG = 'target_language'
VID_SET_TARGET_LANG = 'other_language'

# Leave the rest alone!

STATIC_DIR = "static/vidnar/vid/"

if os.path.isfile(INPUT_ODS_FILE):
	print("file is file")
	vidset = VidnarVideoSet.objects.create(
		name=VID_SET_NAME, 
		slug=VID_SET_SLUG, 
		target_language=VID_SET_TARGET_LANG
	)
	df = read_ods(INPUT_ODS_FILE)
	for i, row in df.iterrows():
		print(row['FileName'])
		vidinst = VidnarVideo.objects.create(
			filename=row['FileName'], 
			sort_order=i,
			description=row['description'],
			source=row['source']
		)
		vidinst.save()
		vidset.videos.add(vidinst)
		shutil.copy(
			f"{INPUT_STIM_DIR}{row['FileName']}", 
			f"{STATIC_DIR}{row['FileName']}"
		)
	vidset.save()

else:
	print("file not file")
	print(INPUT_ODS_FILE)

"""

