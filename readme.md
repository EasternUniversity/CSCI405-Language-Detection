# CSCI405 Natural Language Processing Project

## Giovanni Ruggirello, Joshua Korang, Jesse Byler, Alex Berger, Donye Wakefield

The purose of this Project is to create a program that detects from a user input. The program will be trained on data and some code provided by [Kaggle's Language Detection Model](https://www.kaggle.com/code/martinkk5575/language-detection/notebook)* and use _`Type of Decision Tree`_ Algorithms to detect what language a user is typing into a text box.

_*To support Kaggle, the data is not provided here, but on their own website. Please [download the data there](https://www.kaggle.com/code/martinkk5575/language-detection/notebook) before operating this model!_

----

## How to Build the Flask App

### Dependencies
This Flask app requires additional dependecies on top of `Python 3.x` and `Flask and its virtual environment` to ensure the Chat Bot works correctly. Those are python modules that are installed by running `pip install` in your virtual environment:

```
pip install numpy
pip install tflearn
pip install tensorflow
pip install nltk
pip install torch
pip install torchvision
```
```
While in your virtual environment type:
    -> python
        >> import nltk
        >> nltk.download('punkt')
        >> quit()
```
----

### Chatbot
<img src="Good chatbot image.jpg" alt="This is our Chatbot.">
