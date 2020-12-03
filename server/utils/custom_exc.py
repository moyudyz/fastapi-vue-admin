'''
Author: moyu
Date: 2020-09-27 15:23:22
LastEditors: Moyu
LastEditTime: 2020-11-25 15:42:25
Description: 自定义异常处理
FilePath: /myfastapi/utils/custom_exc.py
'''
import traceback
from typing import Any, Dict, Optional

from extensions import logger
from fastapi import FastAPI, Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel


class ErrorMessageModel(BaseModel):
    code: str
    message: str
    detail: Any = None


class NotFoundException(HTTPException):
    """ 请求的资源不存在 """

    def __init__(
        self,
        error_code: str,
        error_msg: str,
        detail: Any = None,
    ) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not Found",
        )


class UnauthorizedException(HTTPException):
    """ 签名验证失败 """

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )


class ForbiddenException(HTTPException):
    """ 权限异常 """

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden",
        )


class TooManyRequestsException(HTTPException):
    """ 请求超过频率限制 """

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too Many Requests",
        )


def register_exc(app: FastAPI) -> None:
    """ 覆盖异常处理 """

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.debug(f"HTTP异常\n{request.method} | URL:{request.url} | {exc.detail}")
        return ORJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=exc.detail,
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        logger.debug(f"参数异常\n{request.method} | URL:{request.url}\n{exc}")
        return ORJSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=exc._error_cache,
        )

    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(
            f"程序异常\n{request.method} | URL:{request.url}\n \
            Headers:{request.headers}\n{traceback.format_exc()}"
        )
        return ORJSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content="服务器内部错误",
        )
