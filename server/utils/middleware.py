'''
Description: 中间件
Version: 1.0
Autor: Moyu
Date: 2020-11-23 15:20:25
LastEditors: Moyu
LastEditTime: 2020-11-23 15:23:31
'''
from fastapi import FastAPI, Request


def register_middleware(app: FastAPI) -> None:
    @app.middleware('http')
    async def error_to_email(request: Request, call_next):
        response = await call_next(request)
        return response

    @app.middleware('http')
    async def operation_record(request: Request, call_next):
        response = await call_next(request)
        return response