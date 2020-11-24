'''
Author: moyu
Date: 2020-09-27 15:23:22
LastEditors: Moyu
LastEditTime: 2020-11-24 16:38:00
Description: 自定义异常处理
FilePath: /myfastapi/utils/custom_exc.py
'''
from typing import Any

from fastapi import status
from fastapi.responses import ORJSONResponse
from schemas.response import CodeIntEnum, Response


def ok():
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=Response(code=CodeIntEnum.SUCCESS.value, data=None, msg='操作成功').dict(),
    )


def ok_msg(msg: str):
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=Response(code=CodeIntEnum.SUCCESS.value, data=None, msg=msg).dict(),
    )


def ok_data(data: Any):
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=Response(code=CodeIntEnum.SUCCESS.value, data=data, msg='操作成功').dict(),
    )


def ok_detailed(data: Any, msg: str):
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=Response(code=CodeIntEnum.SUCCESS.value, data=data, msg=msg).dict(),
    )


def fail():
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=Response(code=CodeIntEnum.ERROR.value, data=None, msg='操作失败').dict(),
    )


def fail_msg(msg: str):
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=Response(code=CodeIntEnum.ERROR.value, data=None, msg=msg).dict(),
    )


def fail_detailed(data: Any, msg: str):
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=Response(code=CodeIntEnum.ERROR.value, data=data, msg=msg).dict(),
    )
