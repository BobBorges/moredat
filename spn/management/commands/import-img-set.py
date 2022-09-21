from django.core.management.base import BaseCommand, CommandError
from spn.models import *
from pandas_ods_reader import read_ods
import os, shutil





"""
The assumption is that this is run from root, where the manage.py file is. If not take necessary steps to get the file paths correct.
"""


class Command(BaseCommand):

    help = "Use this to import images as a set from an ODS spreadsheet"

    def handle(self, *args, **options):
        INPUT_ODS_FILE = input("Enter path to ODS file (e.g. spn/img-set-ODS/feline.ods): ")
        INPUT_STIM_DIR = input("Enter path to the directory with images you want to import (e.g. `spn/img-set-ODS/feline-stimuli/`, note the trailing slash): ")
        IMG_SET_NAME = input("Enter a name for the picture set (e.g. Types of cats): ")
        IMG_SET_SLUG = input("Enter a slug for the picture set (e.g. cats). No spaces or whacky characters: ")
        STATIC_DIR = "static/spn/img/" # edit if necessary

        if os.path.isfile(INPUT_ODS_FILE):
            self.stdout.write("file is file")
            imgset = SpnPictureSet.objects.create(name=IMG_SET_NAME, slug=IMG_SET_SLUG)
            df = read_ods(INPUT_ODS_FILE)
            for i, row in df.iterrows():
                self.stdout.write(row['FileName'])
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
            self.stdout.write("file not file")
            self.stdout.write(INPUT_ODS_FILE)        
