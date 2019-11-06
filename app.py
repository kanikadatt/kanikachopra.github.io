# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:24:32 2019

@author: Kanika Chopra
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
