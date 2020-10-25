from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


def delete_all() -> int:
    cache_keys = cache.keys("sql-stat:*")
    for key in cache_keys:
        cache.delete(key)
    return len(cache_keys)

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
        delete = options.get("delete")

        if delete:
            nb_deleted_keys = delete_all()
            self.stdout.write(self.style.SUCCESS(f"Successfully delete {nb_deleted_keys} keys"))


