import logging
from fastapi import HTTPException

from constant.info_constant import InfoDetail
from data_handler.data_ingestion import DataIngestion
from interfaces.data_interface import AllDataResponse


logger = logging.getLogger(__name__)


class DataService:
    def __init__(self):
        logger.info(InfoDetail.class_initialize("DataService"))

    def get_data(self, file_type: str = ""):
        data_handler = DataIngestion()
        all_data = data_handler.all_data()

        if file_type not in ["csv", "pptx", "json", "pdf", ""]:
            raise HTTPException(status_code=404, detail="Not Exist")

        if file_type:
            return AllDataResponse(
                data=all_data[file_type],
            )

        return AllDataResponse(
            data=all_data,
        )
