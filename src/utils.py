import os 
import sys 
import pickle 
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging

def save_function(file_path, obj): 
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok= True)
    with open (file_path, "wb") as file_obj: 
        pickle.dump(obj, file_obj)

def model_performance(X_train, y_train, X_test, y_test, models): 
    try: 
        report = {}
        for i in range(len(models)): 
            model = list(models.values())[i]
# Train models
            model.fit(X_train, y_train)
# Test data
            y_test_pred = model.predict(X_test)
            #R2 Score 
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e: 
        raise CustomException(e,sys)

# Function to load a particular object 
def load_obj(file_path):
    try: 
        with open(file_path, 'rb') as file_obj: 
            return pickle.load(file_obj)
    except Exception as e: 
        logging.info("Error in load_object fuction in utils")
        raise CustomException(e,sys)
    
#database loader
def data_base():
    from sqlalchemy import create_engine
    from urllib.parse import quote_plus

    username = "root"
    password = "Rajanraj123@"
    host = "127.0.0.1"
    database_name = "cars"


    # URL-encode the password
    safe_password = quote_plus(password)

    # Create the connection string for mysql-connector-python
    connection_string = f"mysql+mysqlconnector://{username}:{safe_password}@{host}/{database_name}"

    # Create the engine
    engine = create_engine(connection_string)
    
    query = "SELECT * From usedcar"
    df = pd.read_sql(query, engine)
    filepath=os.path.join('notebooks','data', 'usedcar.csv')
    df.to_csv(filepath, index=False)
    print(f"CSV file saved to {filepath}")
    print("succesfully created db")
    