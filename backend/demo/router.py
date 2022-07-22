#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/7/21 14:10
# file: router.py
# author: 臧成龙
# QQ: 939589097
from ninja import Router
from demo.api import router

demo_router = Router()
demo_router.add_router('/', router, tags=["Demo"])
