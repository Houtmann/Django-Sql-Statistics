import operator
from typing import OrderedDict

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


def delete_all() -> int:
    cache_keys = cache.keys("sql-stat:*")
    for key in cache_keys:
        cache.delete(key)
    return len(cache_keys)


def show_all(sort: str):
    cache_keys: [str] = cache.keys("sql-stat:*")
    res: OrderedDict = cache.get_many(cache_keys)
    order: bool = False
    if sort == 'ASC':
        order = False
    if sort == 'DESC':
        order = True

    sorted_by_cumulate_time = sorted(res.items(), key=res.get("cumulateTime"), reverse=order)

    for line in sorted_by_cumulate_time:
        print(line)
        #print(line)




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
        sort: str = options.get("sort")
        delete: bool = options.get("delete")

        if show:
            show_all(sort)

        if delete:
            nb_deleted_keys = delete_all()
            self.stdout.write(self.style.SUCCESS(f"Successfully delete {nb_deleted_keys} keys"))
