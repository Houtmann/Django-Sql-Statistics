import operator
from typing import OrderedDict

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


def delete_all() -> int:
    cache_keys = cache.keys("sql-stat:*")
    for key in cache_keys:
        cache.delete(key)
    return len(cache_keys)


def get_sort_items(sort: str) -> list:
    cache_keys: [str] = cache.keys("sql-stat:*")
    res: OrderedDict = cache.get_many(cache_keys)
    order: bool = False
    if sort == 'ASC':
        order = False
    if sort == 'DESC':
        order = True

    sorted_by_cumulate_time = sorted(res.items(), key=res.get("cumulateTime"), reverse=order)

    return sorted_by_cumulate_time


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
            help="print data, order can change with 'ASC' or 'DESC' ",
            nargs='?'

        )



    def handle(self, *args, **options):
        show_order: bool = options.get("show")
        delete: bool = options.get("delete")

        if show_order:
            items = get_sort_items(show_order)
            for item in items:
                #print(item)
                self.stdout.write(f"{item[0]} {item[1]}")

        if delete:
            nb_deleted_keys = delete_all()
            self.stdout.write(self.style.SUCCESS(f"Successfully delete {nb_deleted_keys} keys"))
