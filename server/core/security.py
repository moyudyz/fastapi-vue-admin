'''
Description: 系统安全
Version: 1.0
Autor: Moyu
Date: 2020-11-21 15:13:04
LastEditors: Moyu
LastEditTime: 2020-11-24 17:32:08
'''
from datetime import datetime, timedelta
from typing import Any, Union

import jwt
from models import SysUser
from passlib.hash import django_pbkdf2_sha256
from schemas import TokenPayload

from core.config import settings

pwd_context = django_pbkdf2_sha256.using(rounds=180000)

ALGORITHM = "HS256"


def create_access_token(sys_user: SysUser, expires_delta: timedelta = None) -> str:
    if expires_delta:
        expires_at = datetime.utcnow() + expires_delta
    else:
        expires_at = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {
        "sub": str(sys_user.id),
        "nickname": sys_user.nickname,
        "username": sys_user.username,
        "authority_id": str(sys_user.sys_authorty_id),
        "buffer_time": str(60 * 60 * 24),  # 缓冲时间1天
        "not_before": datetime.utcnow() - timedelta(seconds=1),  # 生效时间
        "expires_at": expires_at,  # 过期时间
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt.decode("utf-8"), expires_at


def verify_access_token(access_token: str) -> TokenPayload:
    payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    token_data = TokenPayload(**payload)
    return token_data


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
