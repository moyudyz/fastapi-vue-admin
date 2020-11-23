'''
Description: 日志扩展
Version: 1.0
Autor: Moyu
Date: 2020-11-23 11:06:55
LastEditors: Moyu
LastEditTime: 2020-11-23 11:09:08
'''
import os
import time
from loguru import logger

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)
