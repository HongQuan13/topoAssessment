import logging
from fastapi import APIRouter

from constant.info_constant import InfoDetail
from services.data_service import DataService

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class DataRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("", self.all_data, methods=["GET"])
        self.router.add_api_route("/{file_type}", self.get_filter_data, methods=["GET"])
        self.handler = DataService()

    def all_data(self):
        logger.info(InfoDetail.func_call("all_data"))
        return self.handler.get_data()

    def get_filter_data(self, file_type: str):
        logger.info(InfoDetail.func_call("get_filter_data"))
        return self.handler.get_data(file_type)
