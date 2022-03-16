from wordlisttranslation.models import WordlistWord, WordlistWordSet
from pandas_ods_reader import read_ods
import os, shutil

"""

How to use this script:

1. Edit INPUT_ODS_FILE var. 
    ---> path must be relative to the location of manage.py, or absolute

2. Edit the WL_SET_NAME and WL_SET_SLUG vars
	---> SLUG var must contain no spaces

2. enter the django shell    
    --->    $ python manage.py shell

3. run the script from there 
    --->     >>> exec(open('wordlisttranslation/import_wordlist.py').read())

"""


# Edit these vars

INPUT_ODS_FILE = "wordlisttranslation/wordlist-set-ODS/swadesh-like.ods"
WL_SET_NAME = "Swadesh-like Wordlist"
WL_SET_SLUG = "swadesh-like"
WL_SOURCE = "" # may be set an empty string



# Leave the rest alone!


if os.path.isfile(INPUT_ODS_FILE):
	print("file is file")
	WLset = WordlistWordSet.objects.create(name=WL_SET_NAME, slug=WL_SET_SLUG, source=WL_SOURCE)
	df = read_ods(INPUT_ODS_FILE)
	for i, row in df.iterrows():
		print(row['WORD'])
		Winst = WordlistWord.objects.create(
			word=row['WORD'], 
			sort_order=i
		)
		Winst.save()
		WLset.words.add(Winst)
	WLset.save()

else:
	print("file not file")
	print(INPUT_ODS_FILE)

