'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 15:26:15
LastEditors: Moyu
LastEditTime: 2020-11-23 15:47:08
'''
from models import SysUser, SysAuthorty
from core.config import settings
from security import get_password_hash


def init_db() -> None:
    sys_authorty = SysAuthorty.all().first()
    if not sys_authorty:
        sys_authorty = SysAuthorty.create(name='普通用户')
    sys_user = SysUser.filter(username=settings.FIRST_SUPERUSER).first()
    if not sys_user:
        SysUser.create(
            username=settings.FIRST_SUPERUSER,
            password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
            sys_authorty=sys_authorty,
        )
