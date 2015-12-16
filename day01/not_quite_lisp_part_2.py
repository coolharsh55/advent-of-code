#!/usr/bin/python
# -*- coding: utf-8 -*-

"""--- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas,
but his weather machine's "snow" function
is powered by stars, and he's fresh out!
To save Christmas,
he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles.
Two puzzles will be made available on each day in the advent calendar;
the second puzzle is unlocked when you complete the first.
Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building,
but he can't find the right floor -
the directions he got are a little confusing.
He starts on the ground floor (floor 0) and
then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor,
and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep;
he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

--- Part Two ---

Now, given the same instructions, find the position of the
first character that causes him to enter the basement (floor -1).
The first character in the instructions has position 1,
the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character
that causes Santa to first enter the basement?"""


def _file_read(filename):
    """Read file and return text"""

    # Open and read file to get text.
    with open(filename, 'r') as f:
        text = f.read()

    return text


def _file_parse(text):
    """Parse text character by character"""

    # Return characters from text one at a time.
    for character in text:
        yield character


def get_answer():
    """Calculate answer to the question"""

    # Read the contents of the file.
    text = _file_read('./input.txt')

    # Set the initial floor to 0 for GROUND FLOOR
    floor = 0

    # Set position of character when floor is BASEMENT
    basment_position = 0

    # Iterate over each character,
    # if it's ( then go one floor up
    # if it's ) then go one floor down
    # else ignore
    for index, character in enumerate(_file_parse(text)):
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1
        else:
            pass
        # If the basement position has not been set,
        # check if the current floor is the basement
        # and save it if it is.
        # The index in enumeration starts from 0,
        # so we add 1 since the starting character position is 1.
        if not basment_position:
            if floor == -1:
                basment_position = index + 1

    return floor, basment_position


if __name__ == '__main__':

    floor, basment_position = get_answer()
    print('Santa is at floor {}.'.format(floor))
    print(
        'Santa reaches the basement at character {}'.format(basment_position))
