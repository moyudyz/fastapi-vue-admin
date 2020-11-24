'''
Description: 系统角色
Version: 1.0
Autor: Moyu
Date: 2020-11-21 17:07:41
LastEditors: Moyu
LastEditTime: 2020-11-24 13:16:53
'''
from tortoise import fields
from models.mixin import AbstractBaseModel, DateModelMixin


class SysAuthorty(DateModelMixin, AbstractBaseModel):
    name = fields.CharField(max_length=150, description='角色名')
    parent: fields.ForeignKeyRelation['SysAuthorty'] = fields.ForeignKeyField(
        'models.SysAuthorty', related_name='children', null=True
    )
    children: fields.ReverseRelation['SysAuthorty']
    sys_menus: fields.ManyToManyRelation['SysMenu'] = fields.ManyToManyField(
        'models.SysMenu', through='sys_authorty_menu'
    )

    class Meta:
        table = "sys_authorty"
