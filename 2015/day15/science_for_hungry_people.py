#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" --- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients.
You make a list of the remaining ingredients
you could use to finish the recipe (your puzzle input)
and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately,
and you have to be accurate so you can reproduce your results in the future.
The total score of a cookie can be found by adding up each of the properties
(negative totals become 0) and then multiplying together
everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon
(because the amounts of each ingredient must add up to 100)
would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76,
ignoring calories for now) results in a total score of 62842880,
which happens to be the best score possible given these ingredients.
If any properties had produced a negative total,
it would have instead become zero,
causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties,
what is the total score of the highest-scoring cookie you can make? """


from operator import mul
from functools import reduce

# create ingredient tuple
from collections import namedtuple
Ingredient = namedtuple(
    'Ingredient',
    ['capacity', 'durability', 'flavor', 'texture', 'calories'])

# ingredients parsed from input
ingredients = []

# parse input and get ingredients
import re
pattern = re.compile(r'-?\d+')
with open('./input.txt', 'r') as f:
    for line in f.readlines():
        ingredients.append(Ingredient(*map(int, pattern.findall(line))))

# recipes (batches of ingredients)
recipes = []


def score(variations, ingredients):
    """Calculate score for given recipe.
    Variations provide numbers for each ingredient,
    ingredients supply the ingredient attributes. """

    # total score for this recipe
    total = []

    # combine same attrib from different ingredients
    # e.g. all capacity in one tuple, all durability in another
    attrib_scores = zip(*ingredients)

    # zip(attrib, variations) will create a two-item tuple for
    # each attribute of ingredient over the selected variation
    # e.g. (capacity, i), (durability, i), etc... for i,j,k,l
    # then multiply two items to get the score for that attribute
    for attrib in attrib_scores:
        total.append([x[0] * x[1] for x in zip(attrib, variations)])

    # summation of same attribute over different ingredients
    next = list(map(sum, total))

    # calories value, currently not required, hence removed
    # calories = next[-1]
    next = next[:-1]

    # if any of the values of attributes are negative, set them to 0
    next = list(map(lambda x: max(x, 0), next))

    # calculate total score by multiplying different attributes
    return reduce(mul, next)


# reach 100 permutations of each ingredient quantity
for i in range(0, 101):
    for j in range(0, 101 - i):
        for k in range(0, 101 - i - j):
            l = 100 - k - j - i
            recipes.append(score([i, j, k, l], ingredients))

# print the maximum scored recipe
print(max(recipes))
