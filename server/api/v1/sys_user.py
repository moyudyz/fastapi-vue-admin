'''
Description: 系统用户
Version: 1.0
Autor: Moyu
Date: 2020-11-24 14:33:29
LastEditors: Moyu
LastEditTime: 2020-11-24 17:31:22
'''
import random
import string
from datetime import datetime, timedelta
from typing import Any

import models
import schemas
from aioredis import Redis
from api import deps
from core import security
from core.config import settings
from core.security import verify_password, get_password_hash
from extensions import logger
from fastapi import APIRouter, Body, Depends, Header, Path, Query
from utils import response

router = APIRouter()


@router.post("/login", summary="登陆获取access-token", response_model=schemas.Token)
async def login_access_token(login: schemas.request.Login) -> Any:
    """
    username: 用户名
    password: 密码
    """
    sys_user = await models.SysUser.filter(username=login.username).filter().first()
    if not sys_user:
        return response.fail_msg('用户名不存在或者密码错误')

    if not verify_password(login.password, sys_user.password):
        return response.fail_msg('用户名不存在或者密码错误')
    try:
        token, expire_at = security.create_access_token(sys_user)
    except Exception as e:
        logger.error(e)
        return response.fail_msg('获取token失败')

    # 多点登陆
    if not settings.USER_MULTIPOINT:
        return response.ok_data(
            data=schemas.response.LoginResponse(
                user=sys_user, token=token, expire_at=expire_at
            )
        )

    return response.ok_data({})
