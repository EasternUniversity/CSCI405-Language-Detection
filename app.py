<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, g, url_for, jsonify
from chat import get_response
import joblib

#Data Processing Modules
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("chatbot.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


@app.route("/summary")
def language():
    return render_template("summary.html")

#=============================================================#
#                  Machine Learning Model Code                #
#=============================================================#

@app.route("/languagedetector")
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
    file = open('test_model.pkl', 'rb')

    #Eat the pickle (Load the Pickled Model)
    model = joblib.load(file)

    #See if you ate the right pickle (Predict)
    predicition = model.predict(data)

    return predicition

@app.route("/languageprediction", methods=['GET', 'POST'])
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
=======
from flask import Flask, render_template, request, redirect, g, url_for, jsonify
from chat import get_response
import joblib

#Data Processing Modules
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("chatbot.html")

@app.post("/predict_bot")
def predict_bot():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


@app.route("/summary")
def language():
    return render_template("summary.html")

#=============================================================#
#                  Machine Learning Model Code                #
#=============================================================#

@app.route("/languagedetector")
def detector():
    return render_template("languagedetector.html")

def processData(data="English"):
    
    dictionary = open('model_dictionary', 'r', encoding='utf-8')
    text = data
    print(text)
    chars = dictionary.read().split('\n')
    chars.pop()
        
    new_arr = np.zeros((len(text), len(chars)))
    i=0
    j=0
    for text in data:
        sentence = text
        j=0
        for char in chars:
            count = 0
            for letter in sentence:
                if letter == char:
                    count = count + 1
                fraction = count/len(sentence)
            new_arr[i,j] = fraction
            j = j + 1
        
        i = i + 1
            
    data_frame = pd.DataFrame(new_arr, columns = chars)
    return data_frame

def modelPredict(dataFrame):

    data = dataFrame
    
    #Grab a Pickle (Open PKL File)
    file = open('test_model.pkl', 'rb')

    #Eat the pickle (Load the Pickled Model)
    model = joblib.load(file)

    #See if you ate the right pickle (Predict)
    predicition = model.predict(data)

    return set(predicition)

@app.route("/languageprediction", methods=['GET', 'POST'])
def predict():
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
>>>>>>> 2ae14326ba0aec35a911a886b4152af8848e28fd
    app.run(debug=True)