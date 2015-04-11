#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
app.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2015-04-11
'''
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash
from flask.ext.pymongo import PyMongo

MONGO2_DBNAME = 'five_eight_shop'
MONGO2_HOST = ''

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)
#mongo = PyMongo(app, config_prefix='MONGO2')

@app.route('/')
def index():
    online_users = 'x' #mongo.db.users.find({'online': True})
    return render_template('index.html', online_users=online_users)

if __name__ == '__main__':
    app.run()
