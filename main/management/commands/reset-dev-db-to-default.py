from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):

    help = "Na dis' no wroko ete. Use this command to reset the database to its default state."

    def handle(self, *args, **options):
        self.stdout.write("\nNa dis' no wroko ete. A o kon.\n\n")
