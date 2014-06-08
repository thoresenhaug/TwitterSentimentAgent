#!/usr/bin/env python
# encoding: utf-8
"""
WebAPI.py

Created by Erik Thoresen Haug on 2014-06-07.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

from flask import Flask, url_for
import json

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/companies')
def api_companies():
    return json.dumps([{"ticker":"msft","name":"Microsoft" }, {"ticker":"aapl","name":"Apple"}])


if __name__ == '__main__':
    app.run()
