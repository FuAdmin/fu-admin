import redis
from django.conf import settings
from conf.env import *


redis_host = REDIS_HOST
redis_db = REDIS_DB
redis_port = REDIS_PORT
redis_password = REDIS_PASSWORD
if redis_password:
    POOL = redis.ConnectionPool(host=redis_host, port=redis_port, password=redis_password, max_connections=1000)
else:
    POOL = redis.ConnectionPool(host=redis_host, port=redis_port, max_connections=1000)

