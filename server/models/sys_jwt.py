'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 13:27:27
LastEditors: Moyu
LastEditTime: 2020-11-25 11:34:22
'''
from tortoise import fields
from models.mixin import AbstractBaseModel, DateModelMixin


class JwtBlackList(DateModelMixin, AbstractBaseModel):
    jwt = fields.TextField(description='jwt')

    class Meta:
        table = 'sys_jwt_blacklist'