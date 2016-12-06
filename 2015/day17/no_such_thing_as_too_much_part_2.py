#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" --- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time.
To fit it all into your refrigerator,
you'll need to move it into smaller containers.
You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.
If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5

Filling all containers entirely,
how many different combinations of containers
can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen,
another load of eggnog arrives!
The shipping and receiving department is requesting
as many containers as you can spare.

Find the minimum number of containers
that can exactly fit all 150 liters of eggnog.
How many different ways can you fill that number of
containers and still hold exactly 150 litres?

In the example above,
the minimum number of containers was two.
There were three ways to use that many containers,
and so the answer there would be 3. """


# get container sizes from input
# first line is the volume of eggnog
with open('./input.txt', 'r') as f:
    eggnog = int(f.readline())
    containers = [int(line) for line in f.readlines()]


# iterate over all possibilities  of different combinations
# and if any of their sum is the volume of eggnog,
# increase the number of possibilties
# if there are any such possibilities, save their minimum value
# this will be used later to calculate the minimum out of all minimums

possibilities = []

from itertools import combinations
for i in range(2, len(containers)):
    arrangements = [
        len(arrangement)
        for arrangement in combinations(containers, i)
        if sum(arrangement) == eggnog]
    if arrangements:
        possibilities.append(min(arrangements))


# calculate the minimum
# then get all combinations that satiffy the sum and length condition
# calculate their sum
minimum = min(possibilities)
possibilities = 0
for i in range(2, len(containers)):
    possibilities += len([
        arrangement
        for arrangement in combinations(containers, i)
        if sum(arrangement) == eggnog and len(arrangement) == minimum])

print(possibilities)
