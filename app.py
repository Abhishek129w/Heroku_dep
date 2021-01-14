# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:38:17 2021

@author: a.e.kumar.jaiswal
"""

import numpy as np
# import pandas as pd
import pickle
from flask import Flask, Blueprint, request, jsonify, render_template

app=Flask(__name__)
# print("hello")
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    
    output=round(prediction[0],2)
    
    return render_template('index.html',prediction_text='Employee Salary should be ${}'.format(output))

if __name__=="__main__":
    app.run(debug=True)
    
