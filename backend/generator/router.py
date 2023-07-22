#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/7/21 14:10
# file: router.py
# author: 臧成龙
# QQ: 939589097
from ninja import Router
from .test.api import router as test_router

generator_router = Router()
generator_router.add_router('/', test_router, tags=['模板测试'])




