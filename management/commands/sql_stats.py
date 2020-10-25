from typing import OrderedDict

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


def delete_all() -> int:
    cache_keys = cache.keys("sql-stat:*")
    for key in cache_keys:
        cache.delete(key)
    return len(cache_keys)


def show_all(order: str):
    cache_keys: [str] = cache.keys("sql-stat:*")
    res: OrderedDict = cache.get_many(cache_keys)
    for line in res.items():
        print(line)




class Command(BaseCommand):
    help = 'Show sql Statistics'

    def add_arguments(self, parser):

        parser.add_argument(
            '--delete',
            action='store_true',
            help='delete all data',
        )

        parser.add_argument(
            '--show',
            action='store_true',
            help='print data in console',
        )

    def handle(self, *args, **options):
        show: bool = options.get("show")
        order: str = options.get("order")
        delete: bool = options.get("delete")

        if show:
            show_all(order)

        if delete:
            nb_deleted_keys = delete_all()
            self.stdout.write(self.style.SUCCESS(f"Successfully delete {nb_deleted_keys} keys"))
