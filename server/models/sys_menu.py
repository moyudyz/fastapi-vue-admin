'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-21 17:55:55
LastEditors: Moyu
LastEditTime: 2020-11-24 13:16:34
'''
from enum import IntEnum
from tortoise import fields
from models.mixin import AbstractBaseModel, DateModelMixin


class SysMenu(DateModelMixin, AbstractBaseModel):
    path = fields.CharField(max_length=255, unique=True, description='路由path')
    name = fields.CharField(max_length=255, description='路由name')
    hidden = fields.BooleanField(default=False, description='隐藏')
    component = fields.CharField(max_length=255, description='页面文件路径')
    sort = fields.IntField(description='排序标记')
    title = fields.CharField(max_length=255, description='展示名称')
    icon = fields.CharField(max_length=255, description='图标')
    keep_alive = fields.BooleanField(default=False, description='是否缓存')

    keep_alive = fields.CharField(max_length=255, description='是否缓存')
    parent: fields.ForeignKeyRelation['SysMenu'] = fields.ForeignKeyField(
        'models.SysMenu', related_name='children', null=True
    )
    children: fields.ReverseRelation['SysMenu']
    params: fields.ReverseRelation['SysMenuParams']

    class Meta:
        table = "sys_menu"


class ParamTypeEnum(IntEnum):
    PARAMS = 0
    QUERY = 1


class SysMenuParams(DateModelMixin, AbstractBaseModel):
    sys_menu = fields.ForeignKeyField('models.SysMenu', related_name='params')
    param_type = fields.IntEnumField(ParamTypeEnum, description='params?query')
    key = fields.CharField(max_length=255, description='参数键')
    value = fields.CharField(max_length=255, description='参数值')

    class Meta:
        table = "sys_menu_params"
