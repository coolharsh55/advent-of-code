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
as the number in your puzzle input?

--- Part Two ---

The Elves decide they don't want to visit an infinite number of houses.
Instead, each Elf will stop after delivering presents to 50 houses.
To make up for it, they decide to deliver presents
equal to eleven times their number at each house.

With these changes,
what is the new lowest house number of the house to get at least
as many presents as the number in your puzzle input?"""

# the set of presents received by each house
# is the set of factors (unique) including 1 and house no
# therefore, by calculating the factors gives us what elves
# will be dropping presents at that house
# then, we only choose those elves (factors)
# whose division results in a number not greater than 50

from itertools import permutations
import math

# read input and get target presents
# divide it by 11 to reduce the number of calculations
# since each elf drops 11 presents at a stop
with open('./input.txt', 'r') as f:
    target_presents = math.ceil(int(f.readline().strip()) // 11)


# prime numbers cached
# reduces calculations required to generate them again
primes = {2, }


def gen_primes(num):

    """Generate prime numbers (if not exist) below given number"""

    # get latest prime, and add 1 to calculate towards next prime
    n = max(primes) + 1

    # continue till number is a prime,
    # or goes greater than given number
    while n <= num:

        # start with the assumption that the number is a prime
        is_prime = True

        for p in primes:
            # if the number is greater than square of greatest prime,
            # it is a prime itself by this point
            if p * p > n:
                break
            # if a number is divisible by another prime,
            # it isn't a prime
            if n % p == 0:
                is_prime = False
                break

        # if the number is a prime, add it to the cache
        if is_prime:
            primes.add(n)

        # increment number
        n += 1


def gen_factors(num):
    """Generate all factors for the given number"""

    # generate all primes upto the square root of the number.
    # the maximum factor of number cannot be greater than its square root
    num_sqrt = math.ceil(math.sqrt(num))
    gen_primes(num_sqrt)

    # initialise factor as an empty set
    factors = set()

    # get all prime factors of this number
    # lesser than the square root of the number
    prime_factors = {
        x for x in primes
        if num % x == 0 and x <= num_sqrt}

    # add every prime, its divided quotient as factors
    # check and add the square of the prime as a factor as well
    for p in prime_factors:
        factors.add(num // p)
        factors.add(p)
        if num % (p * p) == 0:
            factors.add(p * p)
            factors.add(num // (p * p))

    # flag to mark if the factors need to undergo another permutation
    redo = True

    # while there are still more permutations to be done, contine
    while redo:

        redo = False

        # for every pair of factors, check if their product is also a factor
        for x, y in permutations(factors, 2):
            n = x * y
            # not divisible means not a factor
            if num % n != 0:
                continue
            # products greater than square root cannot be factors
            if n <= num_sqrt:
                # check if it isn't in factors,
                # if no, then it's a new factor,
                # continue the permutations
                if n not in factors:
                    redo = True

                # add the factor and its divided quotient
                factors.add(n)
                factors.add(num // n)

    # check if squares of factors are also factors
    for x in [x for x in factors]:
        n = x * x
        # if number is not divisible, it's not a factor
        if num % n != 0:
            continue
        # if number is greater than square root, it's not a factor
        if n <= num_sqrt:
            factors.add(n)
            factors.add(num // n)

    # add 1 and number itself as factors
    factors.add(1)
    factors.add(num)

    return factors


def get_presents(num):
    """Get number of presents for given house no"""

    # get all factors of number
    factors = gen_factors(num)

    # selected factors where only those elves
    # who have not yet dropped 50 presents will be selected
    selected = []
    for n in factors:
        if num // n <= 50:
            selected.append(n)

    # return sum of all factors
    return sum(selected)


# start at house 1
house_no = 1

# check presents for every house after that until we have a house
# whose presents are at least as many as target presents
while True:
    presents = get_presents(house_no)
    if presents >= target_presents:
        break
    house_no += 1

print(house_no)
