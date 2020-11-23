'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 13:27:27
LastEditors: Moyu
LastEditTime: 2020-11-23 13:44:29
'''
from tortoise import fields
from .mixin import AbstractBaseModel, DateModelMixin


class SysDict(DateModelMixin, AbstractBaseModel):
    name = fields.CharField(max_length=255, description='中文名')
    key = fields.CharField(max_length=255, description='英文名')
    status = fields.BooleanField(default=True, description='状态')
    desc = fields.CharField(max_length=255, description='描述')
    sys_dict_details: fields.ReverseRelation['SysDictDetail']

    class Meta:
        table = 'sys_dict'


class SysDictDetail(DateModelMixin, AbstractBaseModel):
    sys_dict = fields.ForeignKeyField('models.SysDict', related_name='sys_dict_details')
    label = fields.CharField(max_length=255, description='展示值')
    value = fields.IntField(description='字典值')
    status = fields.BooleanField(default=True, description='状态')
    sort = fields.IntField(default=1, description='排序标记')

    class Meta:
        table = 'sys_dict_detail'
