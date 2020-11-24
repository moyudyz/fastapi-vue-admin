'''
Description: 配置文件
Version: 1.0
Autor: Moyu
Date: 2020-11-21 15:13:04
LastEditors: Moyu
LastEditTime: 2020-11-24 17:20:28
'''
import yaml
import secrets
from typing import List, Optional, Dict, Any
from pydantic import BaseSettings, AnyHttpUrl, EmailStr, validator

with open('config.yaml', encoding='utf-8') as fs:
    data = yaml.load(fs, Loader=yaml.FullLoader)


class Settings(BaseSettings):
    """ 配置文件类 """

    # =============项目配置================
    PROJECT_NAME: str = 'FastAPI-Vue-Admin接口文档'
    DESCRIPTION: str = '基于FastAPI+Vue搭建的后台管理系统框架'
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SERVER_HOST: AnyHttpUrl = 'http://localhost:8000'
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:9528']

    # =============数据库配置================
    DB_SERVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_NAME: str
    DB_URI: str = None

    @validator("DB_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return (
            "mysql://{user}:{password}@{server}:{port}/{db}?charset=utf8mb4".format_map(
                user=cls.DB_USER,
                password=cls.DB_PASSWORD,
                server=cls.DB_SERVER,
                port=cls.DB_PORT,
                db=cls.DB_NAME,
            )
        )

    REDIS_URL: str = 'redis://root:@127.0.0.1:6379/0?encoding=utf-8"'

    # =============邮箱相关================
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "email-templates/build"
    EMAILS_ENABLED: bool = False

    # =============超级管理员================
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    USERS_OPEN_REGISTRATION: bool = False  # 开放注册
    USER_MULTIPOINT: bool = False  # 多点登陆
    SENTRY_DSN: str = None

    class Config:
        case_sensitive = True


settings = Settings(**data)


TORTOISE_ORM = {
    "connections": {"default": settings.DB_URI},
    "apps": {
        "models": {
            "models": ["aerich.models", "models"],
            # 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}
