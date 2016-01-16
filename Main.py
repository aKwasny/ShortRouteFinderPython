# -*- coding: <utf-8> -*-
import random
from flask import Flask, request, render_template, session, redirect
from werkzeug.debug import DebuggedApplication

#app_url = '/kwasiboa/ShortRouteFinder'
#app_url = ''

app = Flask(__name__)
app.secret_key = '$KK09W87bjbhAsibi1$%#!Oa'
citiesbase = 'cities.txt'
all_cities = {}
all_users = {}

app.debug = False
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route(app_url + '/')
def index():
    return render_template('ShortRouteFinder.html')



if __name__== '__main__':
    app.run()
    