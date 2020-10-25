# Django-Sql-Statistics

Django-Sql-Statistics Middleware provides statistics on the number of sql queries, 
as well as the cumulative time per view.

-You need to have a cache system like memcached or Redis

# Result Exemple
```json
('sql-stat:django.contrib.admin.sites.login', {'cumulateQueriesNumbers': 0, 'cumulateTime': 0, 'lastQueriesNumbers': 0, 'lastTimeQueries': 0}),
('sql-stat:django.contrib.admin.sites.index', {'cumulateQueriesNumbers': 0, 'cumulateTime': 0, 'lastQueriesNumbers': 0, 'lastTimeQueries': 0})
('sql-stat:test.views.testView', {'cumulateQueriesNumbers': 4, 'cumulateTime': 0.008, 'lastQueriesNumbers': 1, 'lastTimeQueries': 0.002})
```