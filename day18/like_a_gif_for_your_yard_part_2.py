#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" --- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter:
now, at most ten thousand lights are allowed.
You arrange them in a 100x100 grid.

Never one to let you down,
Santa again mails you instructions on the ideal lighting configuration.
With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included
initial configuration (your puzzle input).
A # means "on", and a . means "off".

Then, animate your grid in steps,
where each step decides the next configuration based on the current one.
Each light's next state (either on or off) depends on its current state
and the current states of the eight lights adjacent to it
(including diagonals).
Lights on the edge of the grid might have fewer than eight neighbors;
the missing ones always count as "off".

For example, in a simplified 6x6 grid,
the light marked A has the neighbors numbered 1 through 8,
and the light marked B, which is on an edge,
only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on
its current state (on or off)
plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on,
and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on,
and stays off otherwise.
All of the lights update simultaneously;
they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights,
given your initial configuration,
how many lights are on after 100 steps?

--- Part Two ---

You flip the instructions over;
Santa goes on to point out that this is all just an
implementation of Conway's Game of Life.
At least, it was, until you notice that something's wrong
with the grid of lights you bought:
four lights, one in each corner, are stuck on and can't be turned off.
 The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights,
given your initial configuration,
but with the four corners always in the on state,
how many lights are on after 100 steps? """


# read and create lights as a set
# where only those co-ordinates are stored
# that correspond to lights that are ON
with open('./input.txt', 'r') as f:
    lights = {
        (x, y)  # co-ordinate
        # enumerate file, line by line
        for y, line in enumerate(f)
        # enumerate line, character by character
        for x, char in enumerate(line.strip())
        # only if it is on, as '#' in file
        if char == '#'}
    lights.add((0, 0))
    lights.add((0, 99))
    lights.add((99, 0))
    lights.add((99, 99))


def neighbours(x, y):
    """Calculate no of neighbours that are ON"""

    # retrurn sum of ON neighbours in vicinity
    # identified by x+1 -> x-1; y+1 -> y-1
    # except where the light itself, identified by (x, y)
    return sum([
        (i, j) in lights  # check if light is ON
        for i in (x - 1, x, x + 1)  # positions around
        for j in (y - 1, y, y + 1)  # positions around
        if (i, j) != (x, y)])  # skip the light itself


# iterate the process 100 times
for i in range(0, 100):
    # calculate lights set
    lights = {
        (x, y)  # co-ordinate for ON light
        for x in range(0, 100)  # row 100
        for y in range(0, 100)  # col 100
        # keep light ON if it has ON neighbours between 2 and 3
        if (x, y) in lights and 2 <= neighbours(x, y) <= 3
        # switch light ON if it has ON neighbours exactly 3
        or (x, y) not in lights and neighbours(x, y) == 3
    }
    lights.add((0, 0))
    lights.add((0, 99))
    lights.add((99, 0))
    lights.add((99, 99))


# print number of ON lights
print(len(lights))
