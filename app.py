from flask import Flask, render_template, request, redirect, g, url_for, jsonify
from chat import get_response

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


@app.route("/languagedetector")
def detector():
    return render_template("languagedetector.html")

if __name__ == "__main__":
    app.run(debug=True)