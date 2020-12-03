'''
Description: 用户模型
Version: 1.0
Autor: Moyu
Date: 2020-11-21 16:22:35
LastEditors: Moyu
LastEditTime: 2020-11-25 10:27:10
'''
from tortoise import fields
from models.mixin import AbstractBaseModel, DateModelMixin
from models.sys_authority import SysAuthority


class SysUser(DateModelMixin, AbstractBaseModel):
    username = fields.CharField(max_length=255, description='用户名')
    password = fields.CharField(max_length=255, null=True, description='密码')
    nickname = fields.CharField(
        max_length=255, null=True, default='系统用户', description='昵称'
    )
    avatar = fields.CharField(
        max_length=255,
        null=True,
        default='http://qmplusimg.henrongyi.top/head.png',
        description='头像',
    )
    sys_authority: fields.ForeignKeyRelation[SysAuthority] = fields.ForeignKeyField(
        'models.SysAuthority',
        null=True,
        description='角色',
    )

    class Meta:
        table = "sys_user"
