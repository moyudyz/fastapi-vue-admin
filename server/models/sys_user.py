'''
Description: 用户模型
Version: 1.0
Autor: Moyu
Date: 2020-11-21 16:22:35
LastEditors: Moyu
LastEditTime: 2020-11-23 15:35:38
'''
from tortoise import fields
from .mixin import AbstractBaseModel, DateModelMixin


class SysUser(DateModelMixin, AbstractBaseModel):
    username = fields.CharField(max_length=150, description='用户名')
    password = fields.CharField(max_length=128, null=True, description='密码')
    nickname = fields.CharField(
        max_length=150, null=True, default='系统用户', description='昵称'
    )
    avatar = fields.CharField(
        max_length=255,
        null=True,
        default='http://qmplusimg.henrongyi.top/head.png',
        description='头像',
    )
    sys_authorty: fields.ForeignKeyRelation["SysAuthorty"] = fields.ForeignKeyField(
        'models.SysAuthorty'
    )

    class Meta:
        table = "sys_user"
