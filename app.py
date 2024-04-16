from flask import Flask, request, render_template, jsonify
# Alternatively can use Django, FastAPI, or anything similar
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from src.category import data

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/predict', methods = ['POST', "GET"])

def predict_datapoint(): 
    
    if request.method == "GET": 
        return render_template("form.html")
    else: 
        
        from src.category import data
        
        if request.form.get("Name") not in data["Name_category"]:
            return render_template("form.html",message="Name type is not valid")
        if request.form.get("Location") not in data["Location_category"]:
            return render_template("form.html",message="Location type is not valid")
        if request.form.get("Fuel_Type") not in data["Fuel_Type_category"]:
            return render_template("form.html",message="Fuel_Type is not valid")
        if request.form.get("Transmission") not in data["Transmission_category"]:
            return render_template("form.html",message="Transmission type is not valid")
        if request.form.get("Owner_Type") not in data["Owner_Type_category"]:
            return render_template("form.html",message="Owner_Type is not valid")
        
        
        datanew = CustomData( 
                             Name =request.form.get("Name"),
        Location =request.form.get("Location"),
        Year =float(request.form.get("Year")),
        Kilometers_Driven=float(request.form.get("Kilometers_Driven")),
        Fuel_Type =request.form.get("Fuel_Type"),
        Transmission = request.form.get("Transmission"),
        Owner_Type =request.form.get("Owner_Type"),
        Mileage =float(request.form.get("Mileage")),
        Engine =float( request.form.get("Engine")),
        Power =float(request.form.get("Power")),
        Seats=float(request.form.get("Seats"))
                             )
    new_data = datanew.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = round(pred[0],2)

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)

#http://127.0.0.1:5000/ in browser