from django.core.management.base import BaseCommand, CommandError
from vidnar.models import *
from pandas_ods_reader import read_ods
import os, shutil





"""
The assumption is that this is run from root, where the manage.py file is. If not take necessary steps to get the file paths correct.
"""




class Command(BaseCommand):

    help = "Import videos as a set from an ODS spreadsheet"

    def add_arguments(self, parser):
        parser.add_argument('-o', '--other_language', action='store_true', help="Set for video sets to be described in Research Group's L2 / other language.")
    
    def handle(self, *args, **options):
        INPUT_ODS_FILE = input("Enter path to ODS file (e.g. vidnar/vid-set-ODS/mpi-cut-n-break.ods): ")
        INPUT_STIM_DIR = input("Enter path to the directory with video stimuli (e.g. vidnar/vid-set-ODS/mpi-cut-n-break/): ")
        VID_SET_NAME = input("Enter a name for the video set (e.g. Cut and Break Videos): ")
        VID_SET_SLUG = input("Enter a slug for the video set (e.g. cutnbreak-vids). No spaces or whacky characters: ")
        STATIC_DIR = "static/vidnar/vid/"

        if other_language:
            VID_SET_TARGET_LANG = 'other_language'
        else:
            VID_SET_TARGET_LANG = 'target_language'

        
        if os.path.isfile(INPUT_ODS_FILE):
            self.stdout.write("file is file")
            vidset = VidnarVideoSet.objects.create(
                name=VID_SET_NAME, 
                slug=VID_SET_SLUG, 
                target_language=VID_SET_TARGET_LANG
            )
            df = read_ods(INPUT_ODS_FILE)
            for i, row in df.iterrows():
                self.stdout.write(row['FileName'])
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
            self.stdout.write("file not file")
            self.stdout.write(INPUT_ODS_FILE)
