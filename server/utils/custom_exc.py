'''
Author: moyu
Date: 2020-09-27 15:23:22
LastEditors: Moyu
LastEditTime: 2020-11-24 14:31:50
Description: 自定义异常处理
FilePath: /myfastapi/utils/custom_exc.py
'''
import traceback

from extensions import logger
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError

from utils import response


def register_exc(app: FastAPI) -> None:
    """ 覆盖异常处理 """

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.debug(f"HTTP异常\n{request.method} | URL:{request.url} | {exc.detail}")
        return response.fail_msg(msg=exc.detail)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        logger.debug(f"参数异常\n{request.method} | URL:{request.url}\n{exc}")
        return response.fail_detailed(data=exc.body, msg='参数错误')

    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(
            f"程序异常\n{request.method} | URL:{request.url}\n \
            Headers:{request.headers}\n{traceback.format_exc()}"
        )
        return response.fail_msg(msg='服务器内部错误')
