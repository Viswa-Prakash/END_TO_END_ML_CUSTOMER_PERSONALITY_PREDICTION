import os
import sys
from customer_personality.logger.logs import logging
from customer_personality.utils.utils import read_yaml_file
from customer_personality.exception import AppException
from customer_personality.entity.config_entity import DataIngestionConfig
from customer_personality.constant import *


class AppConfiguration:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(file_path=config_file_path)
        except Exception as e:
            raise AppException(e, sys) from e

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.configs_info['data_ingestion_config']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

            ingested_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['raw_data_dir'])

            response = DataIngestionConfig(
                dataset_download_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )

            logging.info(f"Data Ingestion Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e
        