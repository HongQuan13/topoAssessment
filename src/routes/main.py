import logging
from fastapi import APIRouter

from routes.sub_routes.data_router import DataRouter
from routes.sub_routes.ping_router import PingRouter


logger = logging.getLogger(__name__)

main_router = APIRouter()

ROUTE_BASE = "api"
main_router.include_router(
    PingRouter().router,
    prefix=f"/{ROUTE_BASE}/ping",
)
main_router.include_router(
    DataRouter().router,
    prefix=f"/{ROUTE_BASE}/data",
)
