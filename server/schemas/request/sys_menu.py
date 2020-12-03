from typing import Any, List

import models
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

SysMenuRequest = pydantic_model_creator(models.SysMenu, exclude=['id'])
SysMenuParamsRequest = pydantic_model_creator(models.SysMenuParams, exclude=['id'])


class MenuRequest(BaseModel):
    menu: SysMenuRequest
    params: List[SysMenuParamsRequest] = []