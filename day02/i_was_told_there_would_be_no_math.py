#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper,
and so they need to submit an order for more.
They have a list of the dimensions (length l, width w, and height h)
of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism),
which makes calculating the required wrapping paper for each
gift a little easier: find the surface area of the box,
which is 2*l*w + 2*w*h + 2*h*l.
The elves also need a little extra paper for each present:
the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires
2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper
plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires
2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper
plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet.
How many total square feet of wrapping paper should they order? """


# Each line of the input is of the form (length)x(width)x(height).


def read_input(fileobject):
    """Read input line by line"""

    # Use generator to return one line at a time
    while True:
        line = fileobject.readline()
        if not line:
            break
        yield line


def parse_input(line):
    """Parse length, width, and height from line"""

    # Split the line by character 'x'
    # Parse them into ints
    return (int(value) for value in line.split('x'))


def calculate_area(length, width, height):
    """Calculate the area of wrapping paper required"""

    # Calculate area of package one side at a time
    # Uses itertools.combinations to create combinations of two
    # sides from length, width and height.
    # List comprehension is used to calculate area from the combination
    # by multiplying the two sides in the combination.
    from itertools import combinations
    package_side_areas = [
        x * y
        for x, y in
        combinations((length, width, height), 2)]

    # Package size is twice the sum of areas
    # (each side is present twice on the opposite sides of the package)
    package_area = 2 * sum(package_side_areas)

    # Slack is the area with the smallest side.
    package_area += min(package_side_areas)

    return package_area


def get_answer(filename):
    """Calculate answer for the puzzle"""

    packing_paper = 0

    # Get text from file one line at time
    # parse_input returns a tuple,
    # which is unpacked for the arguments to calculate_area
    with open(filename, 'r') as f:
        for line in read_input(f):
            packing_paper += calculate_area(*parse_input(line))

    return packing_paper


if __name__ == '__main__':

    packing_paper = get_answer('./input.txt')
    print(packing_paper)
