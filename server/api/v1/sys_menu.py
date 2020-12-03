from typing import Any, List

import models
import schemas
from aioredis import Redis
from api import deps
from core import security
from core.config import settings
from extensions import logger
from fastapi import APIRouter, Body, Depends, Header, Path, Query

router = APIRouter()


@router.get(
    "/getMenu",
    summary="动态获取用户菜单",
    response_model=List[models.sys_menu.SysMenu_Pydantic],
)
async def get_menu():
    print(models.sys_menu.SysMenu_Pydantic.schema_json(indent=4))
    queryset = models.SysMenu.filter(hidden=False, parent_id=None).order_by('sort')
    temp = await models.sys_menu.SysMenu_Pydantic.from_queryset(queryset)
    return temp


# @router.post(
#     "/addMenu",
#     summary="新增菜单",
#     response_model=schemas.response.SysMenuResponse,
# )
# async def add_menu(
#     obj_in: schemas.request.MenuRequest,
# ):
#     sys_menu = await models.SysMenu.create(**obj_in.menu.dict())
#     return response.ok_detailed(
#         data=schemas.response.SysMenuResponse.from_orm(sys_menu),
#         msg='获取成功',
#     )
