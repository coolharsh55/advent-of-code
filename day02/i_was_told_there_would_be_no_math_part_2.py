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
How many total square feet of wrapping paper should they order?

--- Part Two ---

The elves are also running low on ribbon.
Ribbon is all the same width,
so they only have to worry about the length they need to order,
which they would again like to be exact.

The ribbon required to wrap a present
is the shortest distance around its sides,
or the smallest perimeter of any one face.
Each present also requires a bow made out of ribbon as well;
the feet of ribbon required for the perfect bow is
equal to the cubic feet of volume of the present.
Don't ask how they tie the bow, though; they'll never tell.

For example:

 - A present with dimensions 2x3x4 requires
    2+2+3+3 = 10 feet of ribbon to wrap the present
    plus 2*3*4 = 24 feet of ribbon for the bow,
    for a total of 34 feet.
 - A present with dimensions 1x1x10 requires
    1+1+1+1 = 4 feet of ribbon to wrap the present
    plus 1*1*10 = 10 feet of ribbon for the bow,
    for a total of 14 feet.

How many total feet of ribbon should they order? """


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
    return tuple(int(value) for value in line.split('x'))


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


def calculate_ribbon(length, width, height):
    """Calculate length of ribbon required to wrap the package"""

    # Ribbon required to wrap around the package is
    # the permeter around the two shortest sides
    # List comprehension saves the sum of all possible
    # side combinations.
    from itertools import combinations
    ribbon_length = [
        2 * (x + y)
        for x, y in
        combinations((length, width, height), 2)]

    # Select the minimum of the calculated lengths as the
    # length of ribbon required to wrap around the present
    ribbon_length = min(ribbon_length)

    # Length of ribbon required for the bow is the volume of the package
    ribbon_length += length * width * height

    return ribbon_length


def get_answer(filename):
    """Calculate answer for the puzzle"""

    packing_paper = 0
    ribbon_length = 0

    # Get text from file one line at time
    # parse_input returns a tuple,
    # which is unpacked for the arguments to calculate_area
    with open(filename, 'r') as f:
        for line in read_input(f):
            package_dimensions = parse_input(line)
            packing_paper += calculate_area(*package_dimensions)
            ribbon_length += calculate_ribbon(*package_dimensions)

    return packing_paper, ribbon_length


if __name__ == '__main__':

    packing_paper, ribbon_length = get_answer('./input.txt')
    print(
        "{PAPER} sq.ft of packing_paper, {RIBBON} ft of ribbon.".format(
            PAPER=packing_paper, RIBBON=ribbon_length))
