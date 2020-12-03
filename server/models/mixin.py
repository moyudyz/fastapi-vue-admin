'''
Description: 通用Mixin
Version: 1.0
Autor: Moyu
Date: 2020-11-21 16:24:39
LastEditors: Moyu
LastEditTime: 2020-11-25 15:45:18
'''
from tortoise import fields
from tortoise.models import Model


class DateModelMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True, description='创建时间')
    updated_at = fields.DatetimeField(null=True, auto_now=True, description='更新时间')
    deleted_at = fields.DatetimeField(null=True, description='删除时间')


class AbstractBaseModel(Model):
    id = fields.BigIntField(pk=True)

    class Meta:
        abstract = True
