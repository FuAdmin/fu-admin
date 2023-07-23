from ninja import Router
from .api import router

test_demo_router = Router()
test_demo_router.add_router('/', router, tags=['测试案例'])
    