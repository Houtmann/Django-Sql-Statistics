import re

from django.core.cache import cache
from django.db import connection
from django.urls import resolve

def get_configuration():
    pass


class LogSql(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            func, args, kwargs = resolve(request.path)

            if not hasattr(func, '__name__'):
                # A class-based view
                func_path = '.'.join([func.__class__.__module__, func.__class__.__name__])
            elif hasattr(func, '__module__'):
                # A function-based view
                func_path = '.'.join([func.__module__, func.__name__])
            else:
                func_path = re.sub(r' at 0x[0-9a-f]+', '', repr(func))

            if 'decorators' in func_path.split('.'):
                func_path = f"{request.resolver_match.namespaces[0]}.{request.resolver_match.url_name}"

        except Exception as e:
            func_path = None
        try:
            queries = connection.queries.copy()
            time = 0
            number_queries = 0
            print(queries)
            for tb in queries:
                time = time + float(tb.get('time'))
                number_queries += 1

            cache_value = cache.get(f'sql-stat:{func_path}')
            print(func_path, cache_value)
            if cache_value is None:
                data = {"cumulateQueriesNumbers": number_queries,
                        "cumulateTime": time,
                        'lastQueriesNumbers': number_queries,
                        'lastTimeQueries': time}


            else:
                data = {"cumulateQueriesNumbers": cache_value.get('cumulateQueriesNumbers') + number_queries,
                        "cumulateTime": cache_value.get('cumulateTime') + time,
                        'lastQueriesNumbers': number_queries,
                        'lastTimeQueries': time}

            cache.set(f"sql-stat:{func_path}", data, None)

        except Exception as e:
            pass

        return response
