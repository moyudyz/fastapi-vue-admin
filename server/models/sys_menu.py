'''
Description: 
Version: 1.0
Autor: Moyu
Date: 2020-11-21 17:55:55
LastEditors: Moyu
LastEditTime: 2020-11-24 13:16:34
'''
from enum import IntEnum
from tortoise import fields
from models.mixin import AbstractBaseModel, DateModelMixin
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class SysMenu(DateModelMixin, AbstractBaseModel):
    path = fields.CharField(max_length=255, unique=True, description='路由path')
    name = fields.CharField(max_length=255, description='路由name')
    hidden = fields.BooleanField(default=False, description='隐藏')
    component = fields.CharField(max_length=255, description='页面文件路径')
    sort = fields.IntField(description='排序标记')
    title = fields.CharField(max_length=255, description='展示名称')
    icon = fields.CharField(max_length=255, description='图标')
    keep_alive = fields.BooleanField(default=False, description='是否缓存')
    parent: fields.ForeignKeyNullableRelation['SysMenu'] = fields.ForeignKeyField(
        'models.SysMenu', related_name='children', null=True
    )
    children: fields.ReverseRelation['SysMenu']
    params: fields.ReverseRelation['SysMenuParams']

    def meta(self) -> dict:
        return {"title": self.title, "icon": self.icon, "keep_alive": self.keep_alive}

    class Meta:
        table = "sys_menu"

    class PydanticMeta:
        # exclude = (
        #     "parent",
        #     "created_at",
        #     "updated_at",
        #     "deleted_at",
        #     "sort",
        #     "title",
        #     "icon",
        #     "keep_alive",
        # )
        # computed = ("meta",)
        allow_cycles = True
        max_recursion = 3


class ParamTypeEnum(IntEnum):
    PARAMS = 0
    QUERY = 1


class SysMenuParams(DateModelMixin, AbstractBaseModel):
    sys_menu = fields.ForeignKeyField('models.SysMenu', related_name='params')
    param_type = fields.IntEnumField(ParamTypeEnum, description='params?query')
    key = fields.CharField(max_length=255, description='参数键')
    value = fields.CharField(max_length=255, description='参数值')

    class Meta:
        table = "sys_menu_params"


SysMenu_Pydantic = pydantic_model_creator(
    SysMenu,
    exclude=(
        "id",
        "parent",
        "created_at",
        "updated_at",
        "deleted_at",
        "sort",
        "title",
        "icon",
        "keep_alive",
    ),
    computed=("meta",),
)
print(SysMenu_Pydantic.schema_json())

SysMenu_List_Pydantic = pydantic_queryset_creator(
    SysMenu,
    exclude=(
        "id",
        "parent",
        "created_at",
        "updated_at",
        "deleted_at",
        "sort",
        "title",
        "icon",
        "keep_alive",
    ),
    computed=("meta",),
    allow_cycles=True,
)
