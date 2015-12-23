#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" --- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit;
his elves have provided him the distances between every pair of locations.
He can start and end at any two (different) locations he wants,
but he must visit each location exactly once.
What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605,
and so the answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off,
Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants,
and he still must visit each location exactly once.

For example, given the distances above,
the longest route would be
982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route? """


# LOGIC
# This is a variant of the Travelling Salesman Problem
# https://en.wikipedia.org/wiki/Travelling_salesman_problem
# where the Santa has to visit each city once, and cover all cities
# in the longest distance possible.
# The variation is -
# Santa does not have to come back to the starting position.
#
# The approach taken in this solutino is BRUTE FORCE.
# It calculates all possible paths for permutations of cities,
# calculcates their distances, and finds the route with the longest distance.
#
# This runs in n! time since for each permutation,
# there are n! possibilities that need to be verified
#
# The general algorithm and approach to problem solving was learnt from
# Peter Norvig's TSP iPython notebook
# http://norvig.com/ipython/


from itertools import permutations
import logging
import re
import sys


logger = logging.getLogger('__file__')
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info(' ### STARTING PROGRAM ###\n\n')


# regex pattern used to parse input
# each line if of the form:
# city (source) to city (destination) = distance
pattern = r'^(\w+) to (\w+) = (\d+)'

# parsed routes
# each route will be a dictionary with the keys:
#   'from': city of origin
#   'to': city of destination
#   'distance': distance between two cities
routes = []

# set of cities
# will contain only the set of cities in the problem
# this is used to form the permutations of all possible routes
cities = set()


# read input from file
with open('./input.txt', 'r') as f:
    text = f.readlines()

# Parse each line and create route for each pair of cities
logger.info('Creating distance matrix for cities')
for line in text:

    # parse origin, destination and distance
    city_from, city_to, distance = re.match(pattern, line).groups()

    # add to routes the city pair and its inverse
    routes.append({
        'to': city_to,
        'from': city_from,
        'distance': int(distance),
    })

    # add to cities set the two cities
    cities.add(city_from)
    cities.add(city_to)

    logger.info(
        '{here} -> {to} = {distance}'.format(
            here=city_from, to=city_to, distance=distance))

logger.info('Cities: {cities}\n\n'.format(cities=cities))


def route_distance(origin, destination):
    """Calculate the distance of route between two cities.
    Will return None if route does not exist. """

    # Get route from routes
    # In any direction, i.e. x->y AND y->x
    route = [
        x for x in routes
        if (x['to'] == destination and x['from'] == origin)
        or (x['from'] == destination and x['to'] == origin)]

    # If such a route exists, return its distance.
    # Else, return None
    if route:
        return route[0]['distance']
    else:
        return None


def tour_length(tour):
    """Calculate the length of tour.
    Will return sum of all routes from first city to last,
    or None if the tour contains invalid routes. """

    length = 0  # length of tour
    for i in range(1, len(tour)):  # iterate over each city pair
        length_route = route_distance(tour[i], tour[i - 1])
        # If the route is invalid, return None
        if length_route is None:
            return None
        length += length_route

    return length


def longest_tour(tours):
    """Get the longest tours out of all given tours.
    The longest tour is chosen based on tour distance,
    i.e. sum of all distances of cities along the route. """

    # Get tour length for each tour
    tours = [(tour, tour_length(tour)) for tour in tours]
    for tour, distance in tours:
        logger.debug(
            '{tour} --> {distance}'.format(
                tour=tour, distance=distance))

    # Remove tours that contain invalid routes,
    # specified by distance = None
    tours = [
        (tour, distance) for tour, distance in tours
        if distance is not None]

    # Return tour with longest distance,
    # accessed at position 1 in the tuple
    return max(tours, key=lambda x: x[1])


def alltours_tsp(cities):
    """Solve the Travelling Salesman Problem for the given set of cities.
    Will return a tuple containing the tour and its total distance. """

    return longest_tour(permutations(cities))


# get the longest tour and distance through TSP algorithm
tour, distance = alltours_tsp(cities)
print(distance)

logger.info(' ### ENDED PROGRAM ###')
