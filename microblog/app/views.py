#!/usr/bin/env python
"""
views.py,
copyright (c) 2016 by Stefan Lehmann

"""
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'MrLeeh'}
    return render_template('index.html', title='Home', user=user)
