'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-24 14:42:46
LastEditors: Moyu
LastEditTime: 2020-11-25 16:19:36
'''
from typing import Any, List

from fastapi import Body
from pydantic import BaseModel


class Login(BaseModel):
    username: str = Body(..., description='用户名')
    password: str = Body(..., description='密码')


class Register(BaseModel):
    username: str = Body(..., description='用户名')
    password: str = Body(..., description='密码')
    nickname: str = Body('user', description='昵称')
    avatar: str = Body('http://qmplusimg.henrongyi.top/head.png', description='头像')
    sys_authority_id: int = Body(1, description='角色')


class ChangePassword(BaseModel):
    username: str = Body(..., description='用户名')
    password: str = Body(..., description='密码')
    new_password: str = Body(..., description='新密码')


class SetUserAuth(BaseModel):
    user_id: int = Body(..., description='用户ID')
    sys_authority_id: int = Body(..., description='角色ID')
