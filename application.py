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

@application.route("/chatbot")
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
    
    #Load in Alphabets
    alpha_latin = open('dict_latin', 'r', encoding='utf-8')
    chars = alpha_latin.read().split(',')
    chars.pop()
    
    with open('dict_other', 'r', encoding='utf-8') as alpha_other:
        tmp = alpha_other.read().split('\n')
        chars_2 = [char.split(',') for char in tmp]
        chars_2.pop()
    
    text = data
    #print(text, chars, chars_2) FOR DEBUGGING ONLY
        
    new_arr = np.zeros((1, len(chars)))
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

    #now second part of searching for chars
    new_arr_2 = np.zeros((1, len(chars_2)))
    count = 0.0
    j = 0
    for list in chars_2:
        count = 0.0
        for char in list:
            for letter in text:
                if letter == char:
                    count = count + 1.0
        fraction = count/len(text)
        new_arr_2[0,j] = fraction
        j = j+1
    
    names = ['Thai', 'Russian', 'Korean', 'Japanese', 'Chinese', 'Tamil', 'Arabic', 'Persian', 'Urdu', 'Hindi', 'Pushto']
    
    data_frame_2 = pd.DataFrame(new_arr_2, columns = names)
    
    final_data_frame = pd.concat([data_frame, data_frame_2], axis=1)
    return final_data_frame

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
