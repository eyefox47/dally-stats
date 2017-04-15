from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import every new session for every campaign that has a \
            youtube_playlist'

    def handle(self, *args, **options):
        pass
