def generator_router(router_info):
    router_txt = f'''from ninja import Router
from .api import router

{router_info.code}_router = Router()
{router_info.code}_router.add_router('/', router, tags=['{router_info.name}'])
    '''
    return router_txt
    pass
