from flask import Flask, render_template, request, redirect, g, url_for


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")
