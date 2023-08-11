#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/7/21 14:10
# file: router.py
# author: 臧成龙
# QQ: 939589097
from ninja import Router
from .go_view_data.api import router as go_view_data_router
from .go_view_project.api import router as go_view_project_router


go_view_router = Router()
go_view_router.add_router('/', go_view_data_router, tags=['Go View Data'])
go_view_router.add_router('/', go_view_project_router, tags=['Go View Project'])





