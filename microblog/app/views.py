#!/usr/bin/env python
"""
views.py,
copyright (c) 2016 by Stefan Lehmann

"""
from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'
