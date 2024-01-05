from dogCatClassifier.config import ConfigurationManager
from dogCatClassifier.components import Evaluation
from dogCatClassifier import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            val_config = config.get_validation_config()
            evaluation = Evaluation(config=val_config)
            evaluation.evaluation()
            evaluation.save_score()
        except Exception as e:
            raise e