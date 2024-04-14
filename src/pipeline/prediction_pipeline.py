import sys 
import os 
from src.exception import CustomException 

from src.logger import logging 
from src.utils import load_obj
from flask import Flask, request, render_template
import pandas as pd

class PredictPipeline: 
    def __init__(self) -> None:
        pass

    def predict(self, features): 
        try: 
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e: 
            logging.info("Error occured in predict function in prediction_pipeline location")
            raise CustomException(e,sys)
        
class CustomData: 
        def __init__(self, yearOfRegistration:int, 
                     kilometer:float, 
                      vehicleType:str,
                      gearbox:str,
                     model:str, 
                     fuelType:str, 
                     brand:str): 
            self.yearOfRegistration =yearOfRegistration
            self.kilometer = kilometer
            self.vehicleType = vehicleType
            self.gearbox= gearbox
            self.model = model
            self.fuelType = fuelType 
            self.brand = brand
        
            

        
        def get_data_as_dataframe(self): 
            try: 
                custom_data_input_dict = {
                    'yearOfRegistration': [self.yearOfRegistration], 
                    'kilometer': [self.kilometer], 
                    'vehicleType': [self.vehicleType], 
                    'gearbox': [self.gearbox],
                    'model':[self.model],
                    'fuelType':[self.fuelType], 
                    'brand': [self.brand], 
                        

                }
                
                df = pd.DataFrame(custom_data_input_dict)
                logging.info("Dataframe created")
                return df
            except Exception as e:
                logging.info("Error occured in get_data_as_dataframe function in prediction_pipeline")
                raise CustomException(e,sys) 
             
             
        