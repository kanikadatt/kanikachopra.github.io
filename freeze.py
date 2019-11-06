# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:21:14 2019

@author: RQ
"""

from flask_frozen import Freezer
from myapp import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()