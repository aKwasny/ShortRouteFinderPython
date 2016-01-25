# -*- coding: <utf-8> -*-
import json
import random
from flask import Flask, request, render_template, session, redirect
from werkzeug.debug import DebuggedApplication
import CitiesDB
import Processing

app_url = '/kwasiboa/ShortRouteFinder'
# app_url = ''

app = Flask(__name__)
app.secret_key = '$KK09W87bjbhAsibi1$%#!Oa'
all_cities = {}
all_users = {}

app.debug = False
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route(app_url + '/')
def index():
    return render_template('ShortRouteFinder.html')


@app.route(app_url + '/citiesdb', methods=['GET'])
def giveMeCitiesDB():
    map = json.dumps(CitiesDB.CitiesDB)
    return map


@app.route(app_url + '/onlycities', methods=['GET'])
def giveMeOnlyCities():
    givenCities = json.dumps({'cities': list(CitiesDB.CitiesDB.keys())}).encode('utf8')
    print(givenCities)
    return givenCities


@app.route(app_url + '/cities/<city>', methods=['GET', 'PUT', 'DELETE'])
def cityActions(city):
    if request.method == 'GET':
        if city not in CitiesDB.CitiesDB.keys():
            return '404 city not found\n'
        giveCity = json.dumps(CitiesDB.CitiesDB[city]).encode('utf8')
        return giveCity
    # TODO: finish the PUT function code - not working already; add city do CitiesDB,
    if request.method == 'PUT':
        if city in CitiesDB.CitiesDB.keys():
            return 'City already in database.\n'
        Processing.add_city_to_map(city)
        Processing.add_route_to_city()

    if request.method == 'DELETE':
        if city in CitiesDB.CitiesDB.keys():
            Processing.remove_city_from_map()
            Processing.remove_route_from_city()
            del CitiesDB.CitiesDB[city]
        else:
            return "City already not in database.\n"
    return '200 OK, city removed.\n'


@app.route(app_url + '/findShortestRoute/<originCity>_<destinationCity>', methods=['GET', 'PUT', 'DELETE'])
def findShortestRoute(originCity, destinationCity):
    theRoute = originCity + '_' + destinationCity
    if request.method == 'GET':
        if theRoute not in CitiesDB.CitiesDB.keys():
            return '404 Route not inside database.\n'
        theRoute = json.dumps(CitiesDB.GeneratedRoutes).encode('utf8')
        return theRoute
    if request.method == 'PUT':
        CitiesDB.GeneratedRoutes[theRoute] = Processing.dijsktra()  # TODO:add graph, origin, destination
        return '200 OK, route placed into database.\n'
    if request.method == 'DELETE':
        if theRoute in CitiesDB.GeneratedRoutes.keys():
            del CitiesDB.GeneratedRoutes[theRoute]
            return '200 OK, route deleted from database.\n'
        else:
            return '404 Route not generated before.\n'


if __name__ == '__main__':
    app.run()
