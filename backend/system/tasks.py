#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/6/14 17:53
# file: tasks.py
# author: 臧成龙
# QQ: 939589097
from celery.app import task

from fuadmin.celery import app


@app.task(name="system.tasks.test_task")
def test_task():
    print('test')