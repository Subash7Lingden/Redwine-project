from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestionn import DataIngestionTrainingPipeline




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



