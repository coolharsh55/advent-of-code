#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house
decorating contest year after year,
you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year,
Santa has mailed you instructions
on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction;
the lights at each corner are at 0,0, 0,999, 999,999, and 999,0.
The instructions include whether to turn on, turn off,
or toggle various inclusive ranges given as coordinate pairs.
Each coordinate pair represents opposite corners of a rectangle, inclusive;
a coordinate pair like 0,0 through 2,2
therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year,
all you have to do is set up your lights by doing the
instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off
(or leave off) the middle four lights.

After following the instructions, how many lights are lit? """


def get_answer(filename):
    """Get the number of lit lights"""

    # Set up lights as a 2D matrix of boolean values,
    # with True representing ON and False representing OFF.
    # The lights are OFF at start (False).
    lights = [[False for x in range(0, 1000)] for x in range(0, 1000)]

    # The commands for managing light.
    commands = {
        'toggle': lambda x, y: not lights[x][y],
        'turn off': lambda x, y: False,
        'turn on': lambda x, y: True,
    }

    # Use regex to parse the line and get commands and light ranges.
    import re
    pattern = r'^([a-zA-Z]+ *[a-zA-Z]*) (\d+),(\d+) through (\d+),(\d+)'

    # Iterate over each line in the input, parse it,
    # and use the commands dictionary
    # to apply the operation on the lights matrix.
    with open(filename, 'r') as f:
        for line in f.readlines():
            parsed = re.match(pattern, line)
            command, start_x, start_y, end_x, end_y = parsed.groups()
            for x in range(int(start_x), int(end_x) + 1):
                for y in range(int(start_y), int(end_y) + 1):
                    lights[x][y] = commands[command](x, y)

    # Return count of all lights that are ON (True) in the 2D matrix
    # by adding all counts in each 1D matrix.
    return sum([x.count(True) for x in lights])

if __name__ == '__main__':

    answer = get_answer('./input.txt')
    print(answer)
