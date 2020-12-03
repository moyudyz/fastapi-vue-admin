'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-24 11:40:07
LastEditors: Moyu
LastEditTime: 2020-11-25 11:22:51
'''
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str = None
    token_type: str = None


class TokenPayload(BaseModel):
    sub: Optional[int] = None
    nickname: Optional[str] = None
    username: Optional[str] = None
    authority_id: Optional[int] = None
    buffer_time: Optional[int] = None
    not_before: Optional[int] = None
    expires_at: Optional[int] = None
