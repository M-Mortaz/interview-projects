import redis
import os
# TODO: add host, port and db to the environment variables to be configurable
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

#  when you want use redis to store some data please import redis_client from here :)
