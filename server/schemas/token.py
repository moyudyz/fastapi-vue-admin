'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-24 11:40:07
LastEditors: Moyu
LastEditTime: 2020-11-24 11:41:52
'''
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str = None
    token_type: str = None


class TokenPayload(BaseModel):
    sub: Optional[int] = None
    exp: Optional[int] = None
