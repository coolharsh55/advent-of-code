#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format.
That's where you come in.

They have a JSON document which contains a variety of things:
arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings.
Your first job is to simply find all of the numbers throughout the document
and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document? """


def add(value):
    """add the value of the number in the object value"""

    # declare the total number sum as a global variable
    # saves recreating the variable on the stack everytime
    global number_sum

    # if the value is an int, add it
    if type(value) == int:
        number_sum += value
        return

    # if the value is a list or a dict,
    # create a reference to iteration of its values
    if type(value) == list:
        numbers = value
    elif type(value) == dict:
        numbers = value.values()
        # ignore if any of the values are 'red'
        if 'red' in numbers:
            return
    else:
        return

    # for iteration, add the value by calling this function recursively
    for item in numbers:
        add(item)


# read and convert input to json
import json
with open('./input.txt', 'r') as f:
    data = json.load(f)

# add the ints in document
number_sum = 0
add(list(data.values()))

# print answer
print(number_sum)
