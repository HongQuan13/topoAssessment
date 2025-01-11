import logging

from constant.info_constant import InfoDetail
from interfaces.ping_interface import PingResponse

logger = logging.getLogger(__name__)


class PingService:
    def __init__(self):
        logger.info(InfoDetail.class_initialize("PingService"))

    def handle_ping(self):
        return PingResponse(message="pong")
