#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" --- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well.
Not everyone gets along!
This year, you resolve, will be different.
You're going to find the optimal seating arrangement
and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount
their happiness would increase or decrease if they were to find themselves
sitting next to each other person. You have a circular table that will be
 just big enough to fit everyone comfortably,
 and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned,
and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David,
Alice would lose 2 happiness units (because David talks so much),
but David would gain 46 happiness units
(because Alice is such a good listener),
for a total change of 44.

If you continue around the table,
you could then seat Bob next to Alice (Bob gains 83, Alice gains 54).
Finally, seat Carol, who sits next to Bob
(Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41).
The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario,
you find that this one is the most optimal,
with a total change in happiness of 330.

What is the total change in happiness for
the optimal seating arrangement of the actual guest list? """


# LOGIC
# The approach taken here is a variation of the
# Traveling Salesman Problem
# https://en.wikipedia.org/wiki/Travelling_salesman_problem
# where the travelling salesman must travel around all cities
# with a minimum distance.
# In this case, the cities are people, and the distance is their
# reaction to each other.
# We have to find the route resulting in the maximum distance or score.
# There's also a difference in the terms of calculating the score,
# unlike TSP, the people's reaction are bidirectional,
# i.e. A sitting next to B means we have to calculate the score
# for A's reaction to B, and B's reaction to A.
#
# The algorithm used here is a BRUTE FORCE variation.
# It looks at all the possibilites and selects the one with the max score.


# Set of people who will sitting around the table
people = set()

# Dictionary of reactions
# Stores the reaction of each person for their neighbour
# The format is :
# {
#   'person': {
#       'neighbour': score,
#   }
# }
# The score is stored positive or negative based on whether
# they gain or lose happiness.
reactions = {}


# read input from file
with open('./input.txt', 'r') as f:
    text = f.readlines()

# Parse the input to get people, and their reactions
# the pattern is like:
# Person would lose(-)/gain(+) score happines ... next to Neighbour
import re
pattern = r'(\w+) would (\w+) (\d+) [\w ]+ to (\w+)\.'

# Create the reactions for all the people
for line in text:

    # Strip whitespace, input file will contain newlines
    line = line.strip()

    # self is the current person in context
    # reaction is a string, specifying whether they lose/gain points
    # points is the happiness score
    # other is the other person (neighbour) in context
    self, reaction, points, other = re.match(pattern, line).groups()

    # add self and other people to the set
    people.add(self)
    people.add(other)

    # adjust score according to whether they're gaining or losing happiness
    # gain is +ve, lose is -ve
    if reaction == 'gain':
        points = int(points)
    elif reaction == 'lose':
        points = int(points) * -1
    else:  # just an edge case for fail-safety
        points = 0

    # if there are no reactions for this person in the dict,
    # create an empty dict for storing reactions
    if reactions.get(self, None) is None:
        reactions[self] = {}

    # set reactions of this person for their neighbour other to points
    reactions[self][other] = points


def score_group(group):
    """Calculate score of the group based on their reactions"""

    # Set initial score to 0.
    # This is the net happiness before they sit in the group.
    #
    # Calculate the score of the by taking a pair at a time,
    # and calculating both their reactions for each other.
    # Note: python wraps around from first to last input
    # because of the list[-1] notation
    score = 0
    for i in range(len(group)):
        score += reactions[group[i - 1]][group[i]]
        score += reactions[group[i]][group[i - 1]]

    return score


# best score resulting in maximum happiness gain for group
best_score = 0
# arrangement resulting in maximum happiness gain
best_arrangement = None


# To get all possible iterations of group arrangements,
# use permutations.
# Check the score of each one, and save the best score
# available so far.
# At the end, the score would reflect the best arrangement possible.
from itertools import permutations
for group in permutations(people):
    score = score_group(group)
    if best_score < score:
        best_score = score
        best_arrangement = group

print(best_score)
