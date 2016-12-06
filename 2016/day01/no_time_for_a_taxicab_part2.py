#!/usr/bin/env python3

__author__ = "Harshvardhan Pandit"
__license__ = "MIT"

# # Day 1: No Time for a Taxicab
# [link](http://adventofcode.com/2016/day/1)
#
# ## Part Two
#
# Then, you notice the instructions continue
# on the back of the Recruiting Document.
# Easter Bunny HQ is actually at the first location you visit twice.

# For example, if your instructions are
# `R8, R4, R4, R8`,
# the first location you **visit twice** is `4 blocks away, due East`.

# _How many blocks away is the first location you visit twice?_

# ## Solution logic
#
# As per the previous solution, this looks to be a trivial problem.
# We only have to check when we visit the place twice, so there has to be
# some way to check whether we have been to the place, which means we need
# to store the point we have been on the graph.
#
# For this, we will use a `set` to store the points, and check at every
# iteration, whether we have been to that point.
# The naive solution would be to store every point we visit, so it merely
# becomes a problem of sifting through searches (binary search would suffice).
# But to make it more efficient, we only store the **paths**,
# and check if the current movement cross any of the previous paths.
#
# ### Basic Geometry
#
# Let's use the property of points lying on a line segment. Suppose we have the
# line segment `AB`, and a point `P` lies on the line, then the sum of the
# distance of `P` from `A` and `P` to `B`
# is equal to the distance from `A` to `B`. Or specified as:
#
#   `AB` = `AP` + `PB`
#
# So we save every point we end up at, as endpoints, and check if the movement
# is along the path by checking for every point in the saved set.
#
# Another interesting observation in terms of optimisation, is that if the
# point does lie on the line, then one of the axis co-ordinates will be the
# same in all three points `(A, B, C)`. This is true in this case because all
# movesments are in the single direction along a grid. So we can eliminate
# points which do not satisfy this condition.


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

# A path contains two points, `A` and `B`.
Path = namedtuple('Path', ('A', 'B'))
# Paths will save all visited paths.
paths = set()

last_point = point

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

    # Check if we have visited the path. To do that, we must first identify
    # whether we have moved along the X-axis or the Y-axis.
    # The `movement_mask` represents the mask applied to the last point to
    # iterate over to the current point. This gives us every point along the
    # path. The mask takes care of negatives and direction, and helps keep
    # the logic clear.
    if point.x == last_point.x:
        # This is along the Y-axis.
        # Check whether we are moving towards the top or the bottom.
        # If the y attribute is increasing, we are moving towards the top,
        # otherwise towards bottom.
        if point.y > last_point.y:
            movement_mask = VectorPoint(0, 1)
        else:
            movement_mask = VectorPoint(0, -1)
    else:
        # This is along the X-axis.
        # Check whether we are moving towards the left or the right.
        # If the x attribute is increasing, we are moving thowards the right,
        # otherwise towards left.
        if point.x > last_point.x:
            movement_mask = VectorPoint(1, 0)
        else:
            movement_mask = VectorPoint(-1, 0)

    last_point_holder = last_point
    # Now iterate through each point along the path
    while last_point.x != point.x or last_point.y != point.y:
        # Move the point
        last_point = VectorPoint(
            last_point.x + movement_mask.x,
            last_point.y + movement_mask.y)
        # Create a flag
        for path in paths:
            # Check if there are any common co-ordinates on this path.
            # If the condition is satisfied,
            # found a point lying in the intersecting path
            if path.A.x == last_point.x and path.B.x == last_point.x:
                if abs(path.A.y - last_point.y)\
                        + abs(last_point.y - path.B.y)\
                        == abs(path.A.y - path.B.y):
                    break
            if path.A.y == last_point.y and path.B.y == last_point.y:
                if abs(path.A.x - last_point.x)\
                        + abs(last_point.x - path.B.x)\
                        == abs(path.A.x - path.B.x):
                    break
        else:
            # No paths match, move ahead.
            continue
        # Some path is found. Stop searching.
        break
    else:
        # Save the path.
        # `last_point = point` at this juncture
        path = Path(last_point_holder, point)
        last_point = point
        paths.add(path)
        continue
    # We found a path that has been visited
    distance = abs(last_point.x) + abs(last_point.y)
    print(distance)
    break
else:
    print(0)
