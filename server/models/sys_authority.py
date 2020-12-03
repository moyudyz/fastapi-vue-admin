'''
Description: 系统角色
Version: 1.0
Autor: Moyu
Date: 2020-11-21 17:07:41
LastEditors: Moyu
LastEditTime: 2020-11-25 10:34:39
'''
from tortoise import fields
from models.mixin import AbstractBaseModel, DateModelMixin
from models.sys_menu import SysMenu


class SysAuthority(DateModelMixin, AbstractBaseModel):
    name = fields.CharField(max_length=150, description='角色名')
    parent: fields.ForeignKeyRelation['models.SysAuthority'] = fields.ForeignKeyField(
        'models.SysAuthority', related_name='children', null=True
    )
    children: fields.ReverseRelation['SysAuthority']
    sys_menus: fields.ManyToManyRelation[SysMenu] = fields.ManyToManyField(
        'models.SysMenu', through='sys_authority_menu'
    )

    class Meta:
        table = "sys_authority"
