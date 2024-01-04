from dogCatClassifier.config import ConfigurationManager
from dogCatClassifier.components import PrepareCallback, Training
from dogCatClassifier import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callback_config()
            prepare_callbacks= PrepareCallback(config=prepare_callbacks_config)
            callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list)
        except Exception as e:
            raise e