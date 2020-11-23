'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 11:47:46
LastEditors: Moyu
LastEditTime: 2020-11-23 15:13:02
'''
import models
from core.config import settings
from utils.custom_exc import UserTokenException, NotFoundException, UnicornException
from aioredis import create_redis_pool, Redis


async def get_redis() -> Redis:
    try:
        redis = await create_redis_pool(settings.REDIS_URL)
        yield redis
    finally:
        redis.close()
