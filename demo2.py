from customer_personality.exception import AppException
from customer_personality.logger.logs import logging
from customer_personality.components.data_ingestion import DataIngestion
from customer_personality.components.data_validation import DataValidation
from customer_personality.components.data_transformation import DataTransformation
from customer_personality.components.model_training import ModelTrainer

#obj = DataIngestion()
#obj.initiate_data_ingestion()
#print("Data Ingestion Completed!")

#obj = DataValidation()
#obj.initiate_data_validation()
#print("Data Validation Completed!")

obj = DataTransformation()
obj.initiate_data_transformation()
print("Data transformation Completed!")

obj = ModelTrainer()
obj.initiate_model_trainer()
print("Model Training Completed!")