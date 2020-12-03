'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-23 15:26:15
LastEditors: Moyu
LastEditTime: 2020-11-25 10:41:52
'''
from tortoise import Tortoise, run_async

from core.config import settings
from core.security import get_password_hash
from models import SysAuthority, SysUser


async def init_db():
    await Tortoise.init(db_url=settings.DB_URI, modules={'models': ['models']})
    # Generate the schema
    await Tortoise.generate_schemas()
    sys_user = await SysUser.filter(username=settings.FIRST_SUPERUSER).first()
    if not sys_user:
        await SysUser.create(
            username=settings.FIRST_SUPERUSER,
            password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
        )


if __name__ == "__main__":
    run_async(init_db())
