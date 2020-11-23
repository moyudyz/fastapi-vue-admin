'''
Description: 通用Mixin
Version: 1.0
Autor: Moyu
Date: 2020-11-21 16:24:39
LastEditors: Moyu
LastEditTime: 2020-11-21 16:34:20
'''
from tortoise import fields
from tortoise.models import Model


class DateModelMixin:
    created = fields.DatetimeField(null=True, auto_now_add=True, description='创建时间')
    updated = fields.DatetimeField(null=True, auto_now=True, description='更新时间')
    deleted = fields.DatetimeField(null=True, description='删除时间')


class AbstractBaseModel(Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True