'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-24 13:31:30
LastEditors: Moyu
LastEditTime: 2020-11-24 16:29:46
'''
from enum import IntEnum
from typing import Any, List

from pydantic import BaseModel


class CodeIntEnum(IntEnum):
    SUCCESS = 0
    ERROR = 1


class Response(BaseModel):
    code: int
    data: Any
    msg: str
