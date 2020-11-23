'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 14:07:02
LastEditors: Moyu
LastEditTime: 2020-11-23 15:36:18
'''
from tortoise import fields
from .mixin import AbstractBaseModel, DateModelMixin


class SysCasbin(AbstractBaseModel):
    ptype = fields.CharField(max_length=255, default='p', source_field='p_type')
    sys_authority_id = fields.CharField(max_length=255, null=True, source_field='v0')
    path = fields.CharField(max_length=255, null=True, source_field='v1')
    method = fields.CharField(max_length=255, null=True, source_field='v2')
    v3 = fields.CharField(max_length=255, null=True, source_field='v3')
    v4 = fields.CharField(max_length=255, null=True, source_field='v4')
    v5 = fields.CharField(max_length=255, null=True, source_field='v5')

    class Meta:
        table = 'sys_casbin'
