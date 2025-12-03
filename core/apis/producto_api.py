from ninja import NinjaAPI
from productos.api import router as productos_router        

productos_api = NinjaAPI()
productos_api.add_router("/productos/", productos_router)