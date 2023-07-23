from ninja import Router
from .api import router

template_test_router = Router()
template_test_router.add_router('/', router, tags=['测试1'])
    