from datetime import datetime
from typing import Any, List

from pydantic import BaseModel


class AbstractResponse(BaseModel):
    class Config:
        json_encoders = {datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')}


class AbstractPageResult(AbstractResponse):
    items: List[Any] = []
    total: int = 0
    page: int = 0
    page_size: int = 0


class ErrorMessageModel(BaseModel):
    code: str
    message: str
    detail: Any = None
