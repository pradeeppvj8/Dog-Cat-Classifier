from dogCatClassifier.pipeline import DataIngestionPipeline
from dogCatClassifier.pipeline import PrepareBaseModelPipeline
from dogCatClassifier.pipeline import ModelTrainingPipeline
from dogCatClassifier.pipeline import EvaluationPipeline
from dogCatClassifier import logger

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<<<<")
    prepare_base_model_pipeline = PrepareBaseModelPipeline()
    prepare_base_model_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<<<<")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<<<<")
    eval_pipeline = EvaluationPipeline()
    eval_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e