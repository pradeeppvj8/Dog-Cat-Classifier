from dogCatClassifier.config import ConfigurationManager
from dogCatClassifier.components import DataIngestion
from dogCatClassifier import logger

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config= data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_and_clean_file()
        except Exception as e:
            raise e