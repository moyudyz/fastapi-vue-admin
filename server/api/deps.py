'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 11:47:46
LastEditors: Moyu
LastEditTime: 2020-12-02 11:20:38
'''
from types import FunctionType

import models
from aioredis import Redis, create_redis_pool
from core.config import settings
from fastapi import Query
from pydantic import BaseModel
from schemas.request import PageInfo


async def get_redis() -> Redis:
    try:
        redis = await create_redis_pool(settings.REDIS_URL)
        yield redis
    finally:
        redis.close()


# 分页参数依赖
async def get_page_info(
    page: int = Query(1, ge=1, description='页码'),
    page_size: int = Query(10, le=50, description='数量'),
) -> PageInfo:
    return PageInfo(page=page, page_size=page_size)


# async def get_page_info(
#     page: int = Query(1, ge=1, description='页码'),
#     page_size: int = Query(10, le=50, description='数量'),
# ) -> PageInfo:
#     return PageInfo(page=page, page_size=page_size)
