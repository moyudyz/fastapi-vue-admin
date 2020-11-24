'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 11:47:46
LastEditors: Moyu
LastEditTime: 2020-11-24 15:46:18
'''
import models
from core.config import settings
from aioredis import create_redis_pool, Redis


async def get_redis() -> Redis:
    try:
        redis = await create_redis_pool(settings.REDIS_URL)
        yield redis
    finally:
        redis.close()
