from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Show sql Statistics'

    def add_arguments(self, parser):

        parser.add_argument(
            '--delete',
            action='store_true',
            help='delete all data',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help='delete all data',
        )

        #parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        pass