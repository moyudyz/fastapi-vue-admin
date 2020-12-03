'''
Description: 请求通用模型
Version: 1.0
Autor: Moyu
Date: 2020-11-23 12:03:14
LastEditors: Moyu
LastEditTime: 2020-12-02 10:39:40
'''
from typing import Any, List

from fastapi import Body
from pydantic import BaseModel


class PageInfo(BaseModel):
    page: int = 1
    size: int = 10


class GetById(BaseModel):
    id: int


class IdSReq(BaseModel):
    ids: List[int]
