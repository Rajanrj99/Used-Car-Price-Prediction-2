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
        
        if request.form.get("vehicleType") not in data["vehicleType_category"]:
            return render_template("form.html",message="vehicle type is not valid")
        if request.form.get("gearbox") not in data["gearbox_category"]:
            return render_template("form.html",message="gearbox type is not valid")
        if request.form.get("model") not in data["model_category"]:
            return render_template("form.html",message="model type is not valid")
        if request.form.get("fuelType") not in data["fuelType_category"]:
            return render_template("form.html",message="fuelType type is not valid")
        if request.form.get("brand") not in data["brand_category"]:
            return render_template("form.html",message="brand type is not valid")
        
        
        datanew = CustomData( yearOfRegistration = float(request.form.get('yearOfRegistration')),
        kilometer = float(request.form.get('kilometer')),
        vehicleType = request.form.get("vehicleType"),
        gearbox= request.form.get("gearbox"), 
        model = request.form.get("model"),
        fuelType= request.form.get("fuelType"), 
        brand =request.form.get("brand"))
    new_data = datanew.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = round(pred[0],2)

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)

#http://127.0.0.1:5000/ in browser