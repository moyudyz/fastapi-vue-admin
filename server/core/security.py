'''
Description: 系统安全
Version: 1.0
Autor: Moyu
Date: 2020-11-21 15:13:04
LastEditors: Moyu
LastEditTime: 2020-11-23 11:11:27
'''
from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.hash import django_pbkdf2_sha256
from schemas import TokenPayload

from core.config import settings

pwd_context = django_pbkdf2_sha256.using(rounds=180000)

ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(access_token: str) -> TokenPayload:
    payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    token_data = TokenPayload(**payload)
    return token_data


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
