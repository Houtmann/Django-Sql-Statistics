from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Show sql Statistics'

    def add_arguments(self, parser):

        parser.add_argument('path', nargs='+', type=str)


        parser.add_argument(
            '--order_by',
            action='store_true',
            help='order_by time',
        )

    def handle(self, *args, **options):
        pass