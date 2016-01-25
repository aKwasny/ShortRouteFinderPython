from collections import defaultdict
import CitiesDB


def start(originCity, visitedCities, connectedCitiesDistances):
    for city in list(CitiesDB.CitiesDB.keys()):
        # TODO: make adding instead of replacing
        if city in list(CitiesDB.CitiesDB.get(originCity).get('Routes').keys()):
            connectedCitiesDistances[city] = CitiesDB.CitiesDB.get(city).get('Routes').keys()
            visitedCities[city] = city
        elif city == originCity:
            connectedCitiesDistances[city] = 0;
            visitedCities[city] = None
        else:
            connectedCitiesDistances[city] = float('inf')
            visitedCities[city] = None

    return


# TODO: done
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

    #0 How does it work:
    #1 searching for the closest node
    #2 downloading routes from it
    #3 deleting previous connections
    #4 relax
    notYetVisited.remove(cityVisitedNow) #3
    checking_if_shortest(cityVisitedNow, visitedCities, connectedCitiesDistances) #4

    finalConnection = create_route(originCity, destinatedCity, visitedCities, connectedCitiesDistances)
    return finalConnection


def add_city_to_map():


def add_route_to_map():


def delete_city_from_map():


def delete_route_from_map():
