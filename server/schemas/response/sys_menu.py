from typing import Any, List

import models
from pydantic import BaseModel
from schemas.response import AbstractPageResult, AbstractResponse
from tortoise.contrib.pydantic import pydantic_model_creator
