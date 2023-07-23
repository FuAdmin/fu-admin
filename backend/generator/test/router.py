from ninja import Router
from .api import router

test_router = Router()
test_router.add_router('/', router, tags=['模板测试'])
    