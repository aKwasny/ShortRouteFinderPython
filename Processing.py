from collections import defaultdict
import CitiesDB

#TODO: nothing
def start(originCity, visitedCities, connectedCitiesDistances):
    for city in list(CitiesDB.CitiesDB.keys()):
        if city in list(CitiesDB.CitiesDB.get(originCity).get('Routes').keys()):
            connectedCitiesDistances[city] = CitiesDB.CitiesDB.get(originCity).get('Routes').keys(city)
            visitedCities[city] = originCity
        elif city == originCity:
            connectedCitiesDistances[city] = 0;
            visitedCities[city] = None
        else:
            connectedCitiesDistances[city] = float('inf')
            visitedCities[city] = None

    return


#TODO: nothing
# this is relax
def checking_if_shortest(cityVisitedNow, visitedCities, connectedCitiesDistances):
    sideNodes = list(CitiesDB.CitiesDB.get(cityVisitedNow).get('Routes').keys())
    # DistanceThroughVisitedCity = connectedCitiesDistances.get(visitedCity)
    for sideNode in sideNodes:
        DistanceThroughSideNode = connectedCitiesDistances.get(sideNode) + CitiesDB.CitiesDB.get(cityVisitedNow).get('Routes').get(sideNode)
        DistanceThroughVisitedCity = connectedCitiesDistances.get(cityVisitedNow) + CitiesDB.CitiesDB.get(cityVisitedNow).get('Routes').get(sideNode)
        if connectedCitiesDistances.get(cityVisitedNow) > DistanceThroughSideNode:
            connectedCitiesDistances[cityVisitedNow] = DistanceThroughSideNode
            visitedCities[cityVisitedNow] = sideNode
        if connectedCitiesDistances.get(sideNode) > DistanceThroughVisitedCity:
            connectedCitiesDistances[sideNode] = DistanceThroughVisitedCity
            visitedCities[sideNode] = cityVisitedNow

    return

# TODO: is everything alright??
def create_route(originCity, destinatedCity, visitedCities, connectedCitiesDistances):
    list_of_cities_to_visit = [destinatedCity]
    while visitedCities.get(destinatedCity) != originCity:
        list_of_cities_to_visit.append(visitedCities.get(destinatedCity))
    list_of_cities_to_visit.append(originCity)
    list_of_cities_to_visit.reverse()
    createdRoute = {'Origin City': originCity, 'Destination': destinatedCity, 'Route length': connectedCitiesDistances.get(destinatedCity)}
    return createdRoute


# TODO: fucking everything!!!
def dijkstra(originCity, destinatedCity):
    visitedCities = {}
    connectedCitiesDistances = {}
    notYetVisited = list(CitiesDB.CitiesDB.keys())
    cityVisitedNow = originCity
    alreadyVisitedCities = CitiesDB.CitiesDB.get(cityVisitedNow).get('Routes')
    notYetVisited.remove(originCity)

    start(originCity, visitedCities, connectedCitiesDistances)

    citiesIveBeenIn = originCity
    citiesIveBeenInConnections = CitiesDB.CitiesDB.get(citiesIveBeenIn).get('Routes')
    notYetVisited.remove(originCity)

    #while (notYetVisited):
     #   while not citiesIveBeenInConnections:
      #      citiesIveBeenInConnections = CitiesDB.CitiesDB.get(citiesIveBeenIn).get('Routes').copy()

    #1 searching for the closest node
    #x = min(float(s) for s in l)
    citiesIveBeenIn = min(citiesIveBeenInConnections.keys(), ) #TODO: <---
    #2 downloading routes from it
    citiesIveBeenInConnections = citiesIveBeenInConnections.copy()
    #3 deleting previous connections
    notYetVisited.remove(cityVisitedNow)
    #4 relax - checking_if_shortest
    checking_if_shortest(cityVisitedNow, visitedCities, connectedCitiesDistances)

    finalConnection = create_route(originCity, destinatedCity, visitedCities, connectedCitiesDistances)
    return finalConnection

#TODO: nothing
def add_city_to_map(city):
    for neighbouringCity in list(CitiesDB.CitiesDB.get(city).get('Routes').keys()):
        distance = CitiesDB.CitiesDB.get(city).get('Routes').get(neighbouringCity)
        CitiesDB.CitiesDB.get(neighbouringCity).get('Routes')[city] = distance
#TODO: nothing
def add_route_to_map():
    for route in list(CitiesDB.GeneratedRoutes.keys()):
        originCity = CitiesDB.GeneratedRoutes.get(route).get('originCity')
        destinatedCity = CitiesDB.GeneratedRoutes.get(route).get('destinatedCity')
        newRoute = dijkstra(originCity, destinatedCity)
        CitiesDB.GeneratedRoutes[route] = newRoute

#TODO: nothing
def delete_city_from_map(city):
    for neighbouringCity in list(CitiesDB.CitiesDB.get(city).get('Routes').keys()):
        del CitiesDB.CitiesDB.get(neighbouringCity).get('Routes')[city]
# TODO
def delete_route_from_map(city):
    for route in list(CitiesDB.GeneratedRoutes.keys()):
        if city in route:
            del CitiesDB.GeneratedRoutes[route]
            continue
        for
