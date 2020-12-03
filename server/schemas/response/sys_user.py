'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-24 14:42:46
LastEditors: Moyu
LastEditTime: 2020-11-25 16:36:30
'''
from typing import Any, List

import models
from pydantic import BaseModel
from schemas.response import AbstractPageResult, AbstractResponse
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

SysUserResponse = pydantic_model_creator(models.SysUser, exclude=['password'])
SysUserListResponse = pydantic_queryset_creator(models.SysUser, exclude=['password'])


class LoginResponse(AbstractResponse):
    user: SysUserResponse
    token: str
    expires_at: int


class UserListResponse(AbstractPageResult):
    items: SysUserListResponse = []