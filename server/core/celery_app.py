'''
Description: 后台任务
Version: 1.0
Autor: Moyu
Date: 2020-11-21 15:13:04
LastEditors: Moyu
LastEditTime: 2020-11-23 11:10:35
'''
from celery import Celery

celery_app = Celery("worker", broker="amqp://moyu:moyu2020@localhost:5672/moyu")

celery_app.conf.task_routes = {"worker.test_celery": "main-queue"}
