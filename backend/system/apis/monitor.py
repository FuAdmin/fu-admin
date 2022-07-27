#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/7/26 14:12
# file: monitor.py
# author: 臧成龙
# QQ: 939589097
from ninja import Router

from utils.fu_response import FuResponse
from utils.system import system

router = Router()


@router.get("/monitor")
def list_role(request):
    qs = system().GetSystemAllInfo()
    return FuResponse(data=qs)
