from ninja import Router
from .api import router

fd_router = Router()
fd_router.add_router('/', router, tags=['fd'])
    