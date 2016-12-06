#!/usr/bin/env python3

__author__ = "Harshvardhan Pandit"
__license__ = "MIT"

# # Day 1: No Time for a Taxicab
# [link](http://adventofcode.com/2016/day/1)

# ## Problem Statement
# Santa's sleigh uses a very high-precision clock to guide its movements,
# and the clock's oscillator is regulated by stars.
# Unfortunately, the stars have been stolen... by the Easter Bunny.
# To save Christmas,
# Santa needs you to retrieve all fifty stars by December 25th.

# Collect stars by solving puzzles.
# Two puzzles will be made available on each day in the advent calendar;
# the second puzzle is unlocked when you complete the first.
# Each puzzle grants one star. Good luck!

# You're airdropped near Easter Bunny Headquarters in a city somewhere.
# "Near", unfortunately, is as close as you can get -
# the instructions on the Easter Bunny Recruiting Document
# the Elves intercepted start here,
# and nobody had time to work them out further.

# The Document indicates that you should start at the given coordinates
# (where you just landed) and face North. Then, follow the provided sequence:
# either turn left (L) or right (R) 90 degrees,
# then walk forward the given number of blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though,
# so you take a moment and work out the destination.
# Given that you can only walk on the street grid of the city,
# how far is the shortest path to the destination?

# For example:

# Following R2, L3 leaves you
# 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you
# 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.

# How many blocks away is Easter Bunny HQ?

# ## Solution logic
#
# This looks to be a simple trace the path sort of problem.
# Assume we start at origin `(0,0)`,
# then use counters to keep track of where we are
# on a virtual grid. Also need to keep track of direction.
# Read the input, then parse it to read whether to go left or right.
# Keep a variable direction to indicate where we are currently moving.
# Direction is a `vector (x,y)`
# to represent the math to do when calculcating the
# next point on the grid.
# `North(0,1); South(0,-1); East(1,0); West(-1,0)`
#
# **Tricky:** how to convert north to west by reading in left?
# _North_ is `(0,1)` and West is `(-1,0)`
# Similarly, `West --left--> South`,
# which can be written as `(-1,0)--L-->(0,-1)`
#
# Drawing up a table to see if I can find a pattern or a formula
# <pre>
#   **Table: Turning LEFT**
#   Direction   Value       Turned      Value
#   North       (0,1)       West        (-1,0)
#   West        (-1,0)      South       (0,-1)
#   South       (0,-1)      East        (1,0)
#   East        (1,0)       North       (0,1)
#
#   **Table: Turning RIGHT**
#   Direction   Value       Turned      Value
#   North       (0,1)       East        (1,0)
#   West        (-1,0)      North       (0,1)
#   South       (0,-1)      West        (-1,0)
#   East        (1,0)       South       (0,-1)
# </pre>
#
# Looking at the table, it is apparent that on every turn, there is a change
# in the field which contain a non-zero value (x or y)
# So we always swap the active (that's what I'll call the non-zero field) field
# The trick here is the sign of the values. It is not true that the sign always
# changes. For e.g. East--Left-->North
#
# <pre>Turn left:
#  - swap (x,y = y,x)
#  - apply mask (-1,1)
# Turn right:
#  - swap (x,y = y,x)
#  - apply mask (1,-1)</pre>
#
# ### Algorithm
# <pre>
#  - Initialise starting direction as North
#  - Read the input
#  - For every input:
#    - based on turn, get new direction
#    - multiply the direction vector by distance in input
#    - add the new vector to point on graph
# </pre>
#
# ### Block distance / Taxicab distance
# That is simply the number of block we need to walk to get there
# That is the total x distance + total y distance
# So the formula is to take the absolute values of both co-ordinates,
# and add them
# `abs(x) + abs(y)`

# Get the input data from a file called `input.txt` in the same folder.
# The file contains the tokens seperated by comma(,).
with open('./input.txt', 'r') as f:
    data = (x.strip() for x in f.read().split(','))

# Use namedtuples, because they're so nice ;)
# Actually, use them because they are still tuples, look like class-objects,
# and give more semantic context to the code.

# In this case, the Turn is LEFT and RIGHT.
from collections import namedtuple
Turns = namedtuple('Turns', ('left', 'right'))
turns = Turns('L', 'R')

# A VectorPoint is a point with a direction
# I use them to plot the point on the graph, and also to represent the
# direction of movement.
VectorPoint = namedtuple('VectorPoint', ('x', 'y'))
# When turning, we apply this mask (the logic if above).
mask_left = VectorPoint(-1, 1)
mask_right = VectorPoint(1, -1)
# The direction is the starting face, which the problem describes as being
# **NORTH**.
direction = VectorPoint(0, 1)
# The point to be tracked, this is the position on graph.
point = VectorPoint(0, 0)

for token in data:
    # Tokenize the token into turn and number of blocks.
    # The first letter represents the direction to turn to, and will only be
    # 'L' for left, and 'R' for right.
    # The numbers after that are the number of blocks to walk.
    turn, blocks = token[:1], int(token[1:])
    # Get mask based on direction to turn
    if turn == turns.left:
        mask = mask_left
    if turn == turns.right:
        mask = mask_right
    # The direction is the swapped direction, with the mask applied.
    # So the previous `(x,y)` becomes `(y,x) * mask(x,y)`.
    direction = VectorPoint(direction.y * mask.x, direction.x * mask.y)
    # The point is now the number of blocks added with the direction applied.
    point = VectorPoint(
        point.x + blocks * direction.x,
        point.y + blocks * direction.y)

# The final distance from origin is the distance of x and y axis.
distance = abs(point.x) + abs(point.y)
print(distance)
