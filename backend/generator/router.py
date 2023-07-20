#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/7/21 14:10
# file: router.py
# author: 臧成龙
# QQ: 939589097
from ninja import Router
from .iii.api import router as iii_router

generator_router = Router()
generator_router.add_router('/', iii_router, tags=['哦哦哦'])



