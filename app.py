# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:24:32 2019

@author: Kanika Chopra
"""

from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST','GET'])
def get_data():
    if request.method == 'POST':
        start = request.form.get('start')
        end = request.form.get('end')
        
        insiderscore = insiderplot.return_json(start, end)
        
    return render_template('index.html', insider = insiderscore)

if __name__=="__main__":
    app.run(debug = False)
