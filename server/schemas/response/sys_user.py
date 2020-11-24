'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-24 14:42:46
LastEditors: Moyu
LastEditTime: 2020-11-24 17:27:28
'''
from typing import Any, List

from pydantic import BaseModel


class LoginResponse(BaseModel):
    user: Any
    token: str
    expires_at: int
