'''
Description: 通用响应模型
Version: 1.0
Autor: Moyu
Date: 2020-11-23 11:58:44
LastEditors: Moyu
LastEditTime: 2020-11-23 12:02:00
'''
from typing import Any, List

from pydantic import BaseModel


class PageResult(BaseModel):
    items: List[Any] = []
    total: int = 0
    page: int = 0
    page_size: int = 0
