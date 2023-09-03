from ninja import Router
from  api import router

test_one_router = Router()
test_one_router.add_router('/', router, tags=['测试1'])
    