'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 13:48:06
LastEditors: Moyu
LastEditTime: 2020-11-23 15:34:13
'''
from tortoise import fields
from .mixin import AbstractBaseModel, DateModelMixin


class SysOperationRecord(DateModelMixin, AbstractBaseModel):
    ip = fields.CharField(max_length=100, description='请求IP')
    method = fields.CharField(max_length=100, description='请求方法')
    path = fields.CharField(max_length=255, description='请求路径')
    status = fields.IntField(description='请求状态')
    latency = fields.IntField(description='延迟')
    agent = fields.CharField(max_length=100, description='代理')
    error_message = fields.CharField(max_length=255, null=True, description='错误信息')
    body = fields.TextField(max_length=100, description='请求Body')
    resp = fields.TextField(max_length=100, description='响应Body')
    sys_user: fields.ForeignKeyRelation['SysUser'] = fields.ForeignKeyField(
        'models.SysUser', description='用户'
    )

    class Meta:
        table = "sys_operation_record"
