'''
Description: 程序主入口
Version: 1.0
Autor: Moyu
Date: 2020-11-21 11:38:19
LastEditors: Moyu
LastEditTime: 2020-11-23 17:02:37
'''
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

from api import api_router
from core.config import settings
from utils.custom_exc import register_exc
from utils.middleware import register_middleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    docs_url=f"{settings.API_V1_STR}/docs",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    redoc_url=None,
)

# 注册tortoise
register_tortoise(
    app,
    db_url=settings.DB_URI,
    modules={
        "models": [
            "SysUser",
            "SysApi",
            "SysAuthorty",
            "SysDict",
            "SysDictDetail",
            "JwtBlackList",
            "SysMenu",
            "SysMenuParams",
            "SysOperationRecord",
        ]
    },
)

# 注册CORS中间件
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 注册路由
app.include_router(api_router, prefix=settings.API_V1_STR)

# 注册自定义异常处理
register_exc(app)

# 注册自定义中间件
register_middleware(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, debug=False)