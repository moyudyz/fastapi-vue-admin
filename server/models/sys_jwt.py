'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 13:27:27
LastEditors: Moyu
LastEditTime: 2020-11-23 13:29:51
'''
from tortoise import fields
from .mixin import AbstractBaseModel, DateModelMixin


class JwtBlackList(DateModelMixin, AbstractBaseModel):
    jwt = fields.CharField(max_length=255, description='jwt')

    class Meta:
        table = 'sys_jwt_blacklist'