'''
Author: moyu
Date: 2020-09-27 15:23:22
LastEditors: Moyu
LastEditTime: 2020-11-23 11:51:55
Description: 自定义异常处理
FilePath: /myfastapi/utils/custom_exc.py
'''
import traceback

from extensions import logger
from fastapi import FastAPI, Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import PlainTextResponse


class NotFoundException(Exception):
    """ 资源找不到异常 """

    def __init__(self, err_desc: str = "Page Not Found"):
        self.err_desc = err_desc


class UserTokenException(Exception):
    """ 用户认证失败 """

    def __init__(self, err_desc: str = "Forbidden"):
        self.err_desc = err_desc


class UnicornException(Exception):
    """ 自定义异常 """

    def __init__(self, err_desc: str):
        self.err_desc = err_desc


def register_exc(app: FastAPI) -> None:
    """ 注册/覆盖异常处理 """

    # UserTokenError异常处理
    @app.exception_handler(UnicornException)
    async def unicorn_exception_handler(request: Request, exc: UnicornException):
        logger.debug(f"自定义异常\n{request.method} | URL:{request.url} | {exc.err_desc}")
        return PlainTextResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=exc.err_desc
        )

    # UserTokenError异常处理
    @app.exception_handler(UserTokenException)
    async def token_exception_handler(request: Request, exc: UserTokenException):
        logger.debug(f"认证异常\n{request.method} | URL:{request.url} | {exc.err_desc}")
        return PlainTextResponse(
            status_code=status.HTTP_403_FORBIDDEN, content=exc.err_desc
        )

    # NotFoundError异常处理
    @app.exception_handler(NotFoundException)
    async def notfount_exception_handler(request: Request, exc: NotFoundException):
        logger.debug(f"无效资源\n{request.method} | URL:{request.url} | {exc.err_desc}")
        return PlainTextResponse(
            status_code=status.HTTP_404_NOT_FOUND, content=exc.err_desc
        )

    # 覆盖HTTPException异常处理
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.debug(f"HTTP异常\n{request.method} | URL:{request.url} | {exc.detail}")
        return PlainTextResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=exc.detail
        )

    # 覆盖RequestValidationError异常处理
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        logger.debug(f"参数异常\n{request.method} | URL:{request.url}\n{exc}")
        return PlainTextResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=str(exc)
        )

    # 覆盖全部异常处理
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(
            f"程序异常\n{request.method} | URL:{request.url}\n \
            Headers:{request.headers}\n{traceback.format_exc()}"
        )
        return PlainTextResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content='Server internal error',
        )
