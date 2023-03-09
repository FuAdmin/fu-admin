# -*- coding: utf-8 -*-
# @Time    : 2022/5/14 15:27
# @Author  : 臧成龙
# @FileName: fu_response.py.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse

from .fu_jwt import DateEncoder

# class JsonResponse(HttpResponse):
#
# 	def __init__(
# 			self,
# 			data,
# 			safe=True,
# 			**kwargs,
# 	):
# 		if safe and not isinstance(data, dict):
# 			raise TypeError(
# 				"In order to allow non-dict objects to be serialized set the "
# 				"safe parameter to False."
# 			)
# 		kwargs.setdefault("content_type", "application/json")
# 		data = json.dumps(data, cls=DateEncoder)
# 		super().__init__(content=data, **kwargs)


class FuResponse(HttpResponse):

	def __init__(self, data=None, msg='success', code=2000, *args, **kwargs):
		std_data = {
			"code": code,
			"result": data,
			"message": msg,
			"success": True
		}
		data = json.dumps(std_data, cls=DateEncoder)
		super().__init__(data, *args, **kwargs)
