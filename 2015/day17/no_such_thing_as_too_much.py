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
can exactly fit all 150 liters of eggnog? """


# get container sizes from input
# first line is the volume of eggnog
with open('./input.txt', 'r') as f:
    eggnog = int(f.readline())
    containers = [int(line) for line in f.readlines()]


# iterate over all possibilities  of different combinations
# and if any of their sum is the volume of eggnog,
# increase the number of possibilties

possibilities = 0

from itertools import combinations
for i in range(2, len(containers)):
    possibilities += len([
        arrangement
        for arrangement in combinations(containers, i)
        if sum(arrangement) == eggnog])

print(possibilities)
