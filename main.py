from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestionn import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline



STAGE_NAME = "Data Ingestion stage"
if __name__ =="__main__":
    try:
        logger.info("f>>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation Stage"
if __name__ =="__main__":
    try:
        logger.info("f>>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation Stage"
if __name__ =="__main__":
    try:
        logger.info("f>>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model Trainer Stage"
if __name__ =="__main__":
    try:
        logger.info("f>>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        model_trainer= ModelTrainerPipeline()
        model_trainer.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e


