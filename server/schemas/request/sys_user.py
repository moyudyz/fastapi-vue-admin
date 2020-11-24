'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-24 14:42:46
LastEditors: Moyu
LastEditTime: 2020-11-24 14:48:44
'''
from typing import Any, List

from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class Register(BaseModel):
    username: str
    password: str
    nickname: str = 'user'
    avatar: str = 'http://qmplusimg.henrongyi.top/head.png'
    authority_id: int = None


class ChangePassword(BaseModel):
    username: str
    password: str
    new_password: str


class SetUserAuth(BaseModel):
    user_id: int
    authority_id: int
