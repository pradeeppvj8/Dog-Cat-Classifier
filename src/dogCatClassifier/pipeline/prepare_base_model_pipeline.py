from dogCatClassifier.config import ConfigurationManager
from dogCatClassifier.components import PrepareBaseModel
from dogCatClassifier import logger

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config= prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e