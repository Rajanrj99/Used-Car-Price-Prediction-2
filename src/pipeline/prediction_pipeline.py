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
        def __init__(self, Name:str, 
                     Location:str, 
                        Year:float,
                      Kilometers_Driven:float,
                     Fuel_Type:str, 
                     Transmission:str, 
                     Owner_Type:str,
                     Mileage:float,
                     Engine:float,
                     Power:float,
                     Seats:float,
                     ): 
                self.Name =Name
                self.Location = Location
                self.Year = Year
                self.Kilometers_Driven=Kilometers_Driven
                self.Fuel_Type =Fuel_Type
                self.Transmission = Transmission
                self.Owner_Type = Owner_Type
                self.Mileage =Mileage
                self.Engine = Engine
                self.Power = Power
                self.Seats=Seats
                
            
            
        
            
    
        
        def get_data_as_dataframe(self): 
            try: 
                custom_data_input_dict = {
                    'Name': [self.Name], 
                    'Location': [self.Location], 
                    'Year': [self.Year], 
                    'Kilometers_Driven': [self.Kilometers_Driven],
                    'Fuel_Type':[self.Fuel_Type],
                    'Transmission':[self.Transmission], 
                    'Owner_Type': [self.Owner_Type], 
                    'Mileage': [self.Mileage], 
                    'Engine': [self.Engine], 
                    'Power': [self.Power],
                     'Seats': [self.Seats],
                    
                    
                    
                        

                }
                
                df = pd.DataFrame(custom_data_input_dict)
                logging.info("Dataframe created")
                return df
            except Exception as e:
                logging.info("Error occured in get_data_as_dataframe function in prediction_pipeline")
                raise CustomException(e,sys) 
             
             
        