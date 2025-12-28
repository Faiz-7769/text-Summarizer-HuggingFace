from src.textSummarizer.config.configuration import ConfigManager
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.logging import logger



class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()
