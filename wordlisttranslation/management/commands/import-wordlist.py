from django.core.management.base import BaseCommand, CommandError
from wordlisttranslation.models import *
from pandas_ods_reader import read_ods
import os, shutil





"""
The assumption is that this is run from root, where the manage.py file is. If not take necessary steps to get the file paths correct.
"""




class Command(BaseCommand):

    help = "Use this to import a wordlist from an ODS spreadsheet"

    def handle(self, *args, **options):
        INPUT_ODS_FILE = input("Enter path to ODS file (e.g. wordlisttranslation/wordlist-set-ODS/swadesh-like.ods): ")
        WL_SET_NAME = input("Enter a name for the Word List (e.g. Swadesh-like Wordlist): ")
        WL_SET_SLUG = input("Enter a slug for the word list (e.g. swadesh-like). No spaces or whacky characters: ")
        WL_SOURCE = input("Enter a source for the word list. This can be blank (just press enter to continue): ")


        if os.path.isfile(INPUT_ODS_FILE):
            self.stdout.write("file is file")
            WLset = WordlistWordSet.objects.create(
                name = WL_SET_NAME,
                slug = WL_SET_SLUG,
                source = WL_SOURCE
            )
            df = read_ods(INPUT_ODS_FILE)
            for i, row in df.iterrows():
                self.stdout.write(row['WORD'])
                Winst = WordlistWord.objects.create(
                    word = row['WORD'], 
                    sort_order = i
                )
                Winst.save()
                WLset.words.add(Winst)
            WLset.save()
        else:
            self.stdout.write("file not file")
            self.stdout.write(INPUT_ODS_FILE)

