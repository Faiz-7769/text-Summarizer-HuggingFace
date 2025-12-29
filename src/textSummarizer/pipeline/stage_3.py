from src.textSummarizer.config.configuration import ConfigManager
from src.textSummarizer.components.model_trainer import ModelTrainer
from src.textSummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
