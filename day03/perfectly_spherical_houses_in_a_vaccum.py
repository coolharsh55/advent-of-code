#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house
at his starting location, and then an elf at the North Pole
calls him via radio and tells him where to move next.
Moves are always exactly one house to the
north (^), south (v), east (>), or west (<).
After each move,
he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog,
and so his directions are a little off,
and Santa ends up visiting some houses more than once.
How many houses receive at least one present?

For example:

> delivers presents to 2 houses:
one at the starting location, and one to the east.

^>v< delivers presents to 4 houses in a square,
including twice to the house at his starting/ending location.

^v^v^v^v^v delivers a bunch of presents
to some very lucky children at only 2 houses. """


def get_next_direction(text):
    """Parse direction from filename, returning one direction at a time"""

    # Translate each character into a move across
    # the Cartesian plane
    # ^ North moves +1 in Y-axis
    # v South moves -1 in Y-axis
    # > East moves +1 in X-axis
    # < West moves -1 in Y-axis
    # Any other character is a non-move, represented by None
    for character in text:
        if character == '^':
            yield (0, 1)
        elif character == 'v':
            yield (0, -1)
        elif character == '>':
            yield (1, 0)
        elif character == '<':
            yield (-1, 0)
        else:
            yield (None, None)


def get_answer(filename):
    """Calculate number of houses with one present"""

    # Open and read the text from the file
    with open(filename, 'r') as f:
        text = f.read()

    # Set initial position to 0, 0 origin
    position = (0, 0)
    # Houses is a set, therefore, all elements in it are unique.
    # Storing the co-ordinates of the houses Santa visits in a set
    # allows getting a list of houses Santa has visited,
    # and therefore have at least one present.
    houses = set()
    # Add the starting house located at 0, 0 origin
    houses.add(position)

    # Iterate over each move,
    # and add the house to the set.
    # The set takes care of uniqueness constraint,
    # and will only add the house position if it is not present already.
    for x, y in get_next_direction(text):
        # If the character is a non-move, ignore it
        if x is None:
            continue

        # Use zip to combine same-axis elements from the two tuples
        # USe map with sum to add them together to get the new co-ordinates
        position = tuple(map(sum, zip(position, (x, y))))
        houses.add(position)

    return len(houses)


if __name__ == '__main__':

    houses_with_one_present = get_answer('./input.txt')
    print(houses_with_one_present)
