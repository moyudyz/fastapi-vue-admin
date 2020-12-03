'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 11:37:56
LastEditors: Moyu
LastEditTime: 2020-11-25 15:52:47
'''
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from .v1 import sys_user
from .v1 import sys_menu

api_router = APIRouter(default=ORJSONResponse)

api_router.include_router(sys_user.router, tags=["系统用户"], prefix='/base')
api_router.include_router(sys_menu.router, tags=["系统菜单"], prefix='/menu')
