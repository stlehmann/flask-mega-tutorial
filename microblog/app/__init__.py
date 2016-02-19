#!/usr/bin/env python
"""
__init__.py,
copyright (c) 2016 by Stefan Lehmann

"""
from flask import Flask

app = Flask(__name__)
from app import views