from typing import Any

import models
import schemas
from aioredis import Redis
from api import deps
from core import security
from core.config import settings
from extensions import logger
from fastapi import APIRouter, Body, Depends, Header, Path, Query
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# @router.post(
#     "/login",
#     summary="登陆获取access-token",
#     response_model=schemas.response.LoginResponse,
# )
# async def login_access_token(
#     obj_in: schemas.request.Login, redis: Redis = Depends(deps.get_redis)
# ):
#     """
#     username: 用户名
#     password: 密码
#     """
#     sys_user = await models.SysUser.filter(username=obj_in.username).filter().first()
#     if not sys_user:
#         return response.fail_msg('用户名或者密码错误')

#     if not security.verify_password(obj_in.password, sys_user.password):
#         return response.fail_msg('用户名或者密码错误')
#     try:
#         token, expires_at = security.create_access_token(sys_user)
#     except Exception as e:
#         logger.error(e)
#         return response.fail_msg('获取token失败')

#     # 开启多点登陆, 直接返回token
#     if settings.USER_MULTIPOINT:
#         return response.ok_detailed(
#             data=schemas.response.LoginResponse(
#                 user=sys_user, token=token, expires_at=expires_at
#             ),
#             msg="登陆成功",
#         )
#     # 获取redis中的token
#     jwt_str = await redis.get(sys_user.username)
#     if jwt_str:
#         # 原jwt_str加入黑名单
#         await models.JwtBlackList.create(jwt=jwt_str)
#         # 重新设置jwt_str
#         await redis.set(sys_user.username, token, expire=60 * 60 * 24 * 8)
#         return (
#             schemas.response.LoginResponse(
#                 user=sys_user, token=token, expires_at=expires_at
#             ),
#         )
#     else:
#         await redis.set(sys_user.username, token, expire=60 * 60 * 24 * 8)
#         return response.ok_detailed(
#             data=schemas.response.LoginResponse(
#                 user=await schemas.response.SysUserResponse.from_tortoise_orm(sys_user),
#                 token=token,
#                 expires_at=expires_at,
#             ),
#             msg="登陆成功",
#         )


# @router.post(
#     "/register",
#     summary="注册账号",
#     response_model=schemas.response.SysUserResponse,
# )
# async def register(obj_in: schemas.request.Register):
#     """
#     username: 用户名
#     password: 密码
#     nickname: 昵称 = 'user'
#     avatar: 头像 = 'http://qmplusimg.henrongyi.top/head.png'
#     authority_id: 角色ID = None
#     """
#     if await models.SysUser.filter(username=obj_in.username).exists():
#         return response.fail_msg(msg='用户名已存在')
#     # 加密密码
#     obj_in.password = security.get_password_hash(obj_in.password)
#     # 转成字典
#     obj_in_data = jsonable_encoder(obj_in)
#     # 创建用户
#     sys_user = await models.SysUser.create(**obj_in_data)
#     return response.ok_detailed(
#         data=await schemas.response.SysUserResponse.from_tortoise_orm(sys_user),
#         msg='注册成功',
#     )


# @router.post(
#     "/changePassword",
#     summary="修改密码",
#     response_model=schemas.response.SysUserResponse,
# )
# async def change_password(obj_in: schemas.request.ChangePassword):
#     sys_user = await models.SysUser.filter(username=obj_in.username).first()
#     if sys_user is None:
#         return response.fail_msg(msg='用户名或原密码错误')
#     if not security.verify_password(obj_in.password, sys_user.password):
#         return response.fail_msg('用户名或原密码错误')
#     sys_user.password = security.get_password_hash(obj_in.new_password)
#     sys_user.save(update_fields=['password', 'updated'])
#     return response.ok_msg('修改成功')


# @router.get(
#     "/getUserList",
#     summary='分页获取用户列表',
#     response_model=schemas.response.UserListResponse,
# )
# async def get_user_list(
#     page_info: schemas.request.PageInfo = Depends(deps.get_page_info),
# ):
#     query = models.SysUser.filter()
#     queryset = query.offset(page_info.page - 1).limit(page_info.size)
#     total = await query.count()
#     temp = await schemas.response.SysUserListResponse.from_queryset(queryset)

#     return response.ok_detailed(
#         data=schemas.response.UserListResponse(
#             items=temp,
#             total=total,
#             page=page_info.page,
#             page_size=page_info.size,
#         ),
#         msg='获取成功',
#     )