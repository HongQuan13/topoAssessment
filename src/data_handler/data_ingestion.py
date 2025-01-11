import os
import json
import logging
import pandas as pd
import pdfplumber
from pptx import Presentation

from data_handler.data_processor import DataProcessor

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))


class DataIngestion:
    def __init__(self):
        self.data = {}
        self._handle_file_path()
        self._read_json(self._json_path)
        self._read_csv(self._csv_path)
        self._read_pdf(self._pdf_path)
        self._read_pptx(self._pptx_path)

    def _handle_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        self._json_path = os.path.join(parent_dir, "datasets/dataset1.json")
        self._csv_path = os.path.join(parent_dir, "datasets/dataset2.csv")
        self._pdf_path = os.path.join(parent_dir, "datasets/dataset3.pdf")
        self._pptx_path = os.path.join(parent_dir, "datasets/dataset4.pptx")

    def _read_csv(self, file_path):
        try:
            df = pd.read_csv(file_path)
            data = df.to_dict(orient="records")
            self.data["csv"] = DataProcessor.clean_csv(data)
            logger.info(f"CSV Data Loaded: {df.shape} rows and columns.")
        except Exception as e:
            logger.info(f"Error reading CSV: {e}")

    def _read_pptx(self, file_path):
        try:
            ppt = Presentation(file_path)
            data = DataProcessor.clean_pptx(ppt)
            self.data["pptx"] = data
            logger.info(f"PPTX Data Loaded.")
        except Exception as e:
            logger.error(f"Error reading PPTX: {e}")
            return None

    def _read_pdf(self, file_path):
        try:
            with pdfplumber.open(file_path) as pdf:
                data = DataProcessor.clean_pdf(pdf)
            self.data["pdf"] = data
            logger.info(f"PDF Data Loaded.")
        except Exception as e:
            logger.info(f"Error reading PDF: {e}")

    def _read_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            self.data["json"] = DataProcessor.clean_json(data)
            logger.info(f"JSON Data Loaded.")
        except Exception as e:
            logger.info(f"Error reading JSON: {e}")

    def all_data(self):
        return self.data


if __name__ == "__main__":
    data_handler = DataIngestion()
    data_handler.all_data()
