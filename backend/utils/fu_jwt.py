# -*- coding: utf-8 -*-
# @Time    : 2022/5/14 16:19
# @Author  : 臧成龙
# @FileName: fu_jwt.py
# @Software: PyCharm
from typing import Union
from simplejwt import util
from simplejwt.jwt import default_alg, _hash, Jwt
import datetime
import json


class DateEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			return obj.strftime("%Y-%m-%d %H:%M:%S")
		else:
			return json.JSONEncoder.default(self, obj)


class FuJwt(Jwt):

	def encode(self) -> str:
		payload = {}
		payload.update(self.registered_claims)
		payload.update(self.payload)
		return encode(self.secret, payload, self.alg, self.header)


def encode(secret: Union[str, bytes], payload: dict = None, alg: str = default_alg, header: dict = None) -> str:
	"""
    :param secret: The secret used to encode the token.
    :type secret: Union[str, bytes]
    :param payload: The payload to be encoded in the token.
    :type payload: dict
    :param alg: The algorithm used to hash the token.
    :type alg: str
    :param header: The header to be encoded in the token.
    :type header: dict
    :return: A new token
    :rtype: str
    """
	secret = util.to_bytes(secret)

	payload = payload or {}
	header = header or {}

	header_json = util.to_bytes(json.dumps(header))
	header_b64 = util.b64_encode(header_json)
	payload_json = util.to_bytes(json.dumps(payload, cls=DateEncoder))
	payload_b64 = util.b64_encode(payload_json)

	pre_signature = util.join(header_b64, payload_b64)
	signature = _hash(secret, pre_signature, alg)
	signature_b64 = util.b64_encode(signature)

	token = util.join(pre_signature, signature_b64)
	return util.from_bytes(token)
