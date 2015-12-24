#!/usr/bin/python3
# -*- coding: utf-8 -*-

# author: coolharsh55
# Harshvardhan J. Pandit

""" --- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy,
Santa has them deliver some presents by hand, door-to-door.
He sends them down a street with infinite houses numbered sequentially:
1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too,
and delivers presents to houses based on that number:

The first Elf (number 1) delivers presents to every house:
1, 2, 3, 4, 5, ....
The second Elf (number 2) delivers presents to every second house:
2, 4, 6, 8, 10, ....
Elf number 3 delivers presents to every third house:
3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1.
Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1,
which delivers 1 * 10 = 10 presents.
The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4,
for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents
as the number in your puzzle input? """

# get the target presents to check for
# divide it by ten to make calculation simpler
# since each elf drops ten presents at each house
# so, house 4 has (10 + 20 + 40) = 70
# which is (1 + 2 + 4) * 10 = 70
# which can be calculated by using (1 + 2 + 4) = 7
#
# the set of presents received by each house
# is the set of factors (unique) including 1 and house no
#
# therefore, by calculating the factors gives us what elves
# will be dropping presents at that house

with open('./input.txt', 'r') as f:
    target_presents = int(f.readline().strip()) // 10

import math
from itertools import chain

# iterate from 1 to target number of presents
for house_no in range(1, target_presents):
    # get the number of presents at this house
    # number of presents is the sum of all factors of this house no
    presents = sum(set(
        # chaining is used to get a single list
        # from the tuple produced in list comprehension
        chain.from_iterable(
            # get the two factors, (x, y) where x * y = house_no
            (i, house_no // i)
            # iterate only upto the square root of house_no
            # as the max factor will be its square root
            for i in range(1, math.ceil(math.sqrt(house_no) + 1))
            # check that i being iterate divides house_no completely
            if house_no % i == 0)))
    # check if presents for this house are the required no of presents
    if presents >= target_presents:
        break

print(house_no)
