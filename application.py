from flask import Flask, render_template, request, redirect, g, url_for, jsonify
from chat import get_response
import joblib

#Data Processing Modules
import pandas as pd
import numpy as np

application = Flask(__name__)

@application.route("/")
def homepage():
    return render_template("home.html")

@application.route("/projects")
def projects():
    return render_template("chatbot.html")

@application.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


@application.route("/summary")
def language():
    return render_template("summary.html")

#=============================================================#
#                  Machine Learning Model Code                #
#=============================================================#

@application.route("/languagedetector")
def detector():
    return render_template("languagedetector.html")

def processData(data="English"):
    
    dictionary = open('model_dictionary', 'r', encoding='utf-8')
    text = data
    print(text)
    chars = dictionary.read().split('\n')
    chars.pop()
        
    new_arr = np.zeros((len(text), len(chars)))
    j=0
    for char in chars:
        count = 0
        for letter in text:
            if letter == char:
                count = count + 1
        fraction = count/len(text)
        new_arr[0,j] = fraction
        j = j + 1

    data_frame = pd.DataFrame(new_arr, columns = chars)
    return data_frame

def modelPredict(dataFrame):

    data = dataFrame
    
    #Grab a Pickle (Open PKL File)
    file = open('model.pkl', 'rb')

    #Eat the pickle (Load the Pickled Model)
    model = joblib.load(file)

    #See if you ate the right pickle (Predict)
    predicition = model.predict(data)

    return predicition[0]

@application.route("/languageprediction", methods=['GET', 'POST'])
def langPredict():
    if request.method == 'POST':
        data = request.form.get('input_words')
    
        #try:
        processed_data = processData(data)
        prediction = modelPredict(processed_data)

        print(prediction)
        return render_template('predict.html', prediction=prediction)
        
        #except ValueError:
            #return "Please Enter valid values"

        pass
    pass

if __name__ == "__main__":
    application.run(host="localhost", port=5000, debug=True)