'''
Description: API模型
Version: 1.0
Autor: Moyu
Date: 2020-11-23 12:51:47
LastEditors: Moyu
LastEditTime: 2020-11-23 12:57:45
'''
from tortoise import fields
from .mixin import AbstractBaseModel, DateModelMixin


class SysApi(DateModelMixin, AbstractBaseModel):
    path = fields.CharField(max_length=255, description='路径')
    desc = fields.CharField(max_length=255, description='中文描述')
    api_group = fields.CharField(max_length=255, description='组')
    method = fields.CharField(max_length=255, description='方法')

    class Meta:
        table = "sys_api"
