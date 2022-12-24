import logging
from time import sleep

from django.db import transaction
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
import redis
from django.views.decorators.csrf import csrf_exempt

from counterapp.models import Counter, MySQLCounter

REDIS_KEY = 'gio222_hook'

redis_conn = redis.Redis('127.0.0.1')
logger = logging.getLogger(__name__)

redis_conn.delete(REDIS_KEY)


@method_decorator(csrf_exempt, name='dispatch')
class RedisHook(View):
    def post(self, request):
        with redis_conn.pipeline() as p:
            p.incrby(REDIS_KEY)
            p.expire(REDIS_KEY, 600)
            cur_count, _ = p.execute()

        # sleep(3)

        logger.info(f'cur_count: {cur_count}')
        print(f'cur_count: {cur_count}')
        return HttpResponse(f'Django REDIS OK {cur_count}', content_type='plain/text')


@method_decorator(csrf_exempt, name='dispatch')
class SQLiteHook(View):
    @transaction.atomic
    def post(self, request):
        # Creation handled in apps.py
        Counter.objects.filter(name=REDIS_KEY).update(count=F('count') + 1)
        sqlite_count_obj = Counter.objects.get(name=REDIS_KEY)

        logger.info(f'cur_count: {sqlite_count_obj.count}')
        print(f'cur_count: {sqlite_count_obj.count}')
        return HttpResponse(f'Django SQLite OK {sqlite_count_obj.count}', content_type='plain/text')


@method_decorator(csrf_exempt, name='dispatch')
class MySQLHook(View):
    @transaction.atomic
    def post(self, request):
        # Creation handled in apps.py
        MySQLCounter.objects.filter(name=REDIS_KEY).update(count=F('count') + 1)
        mysql_count_obj = MySQLCounter.objects.get(name=REDIS_KEY)

        logger.info(f'cur_count: {mysql_count_obj.count}')
        print(f'cur_count: {mysql_count_obj.count}')
        return HttpResponse(f'Django MySQL OK {mysql_count_obj.count}', content_type='plain/text')
