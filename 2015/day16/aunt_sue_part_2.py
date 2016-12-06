#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" --- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift,
and you'd like to send her a thank you card.
However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person,
you need to figure out which Aunt Sue
(which you conveniently number 1 to 500, for sanity) gave you the gift.
You open the present and, as luck would have it,
good ol' Aunt Sue got you a My First Crime Scene Analysis Machine!
Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short)
can detect a few specific compounds in a given sample,
as well as how many distinct kinds of those compounds there are.
According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog:
    samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these.
You put the wrapping from the gift into the MFCSAM.
It beeps inquisitively at you a few times and
then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue.
Things missing from your list aren't zero -
you simply don't remember the value.

What is the number of the Sue that got you the gift?

--- Part Two ---

As you're about to send the thank you note,
something in the MFCSAM's instructions catches your eye.
Apparently, it has an outdated retroencabulator,
and so the output from the machine isn't exact values -
some of them indicate ranges.

In particular, the cats and trees readings indicates that there
are greater than that many
(due to the unpredictable nuclear decay of cat dander and tree pollen),
while the pomeranians and goldfish readings indicate that
there are fewer than that many
(due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?"""


# output of the MSCSAM
mfcsam = {}

# input patterns
import re
pattern_mfcsam = re.compile(r'(\w+): (\d)+')
pattern_inputs = re.compile(
    r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

# open and read input
with open('./input.txt', 'r') as f:

    # first 10 lines contain MFCSAM output
    for i in range(10):
        line = f.readline()
        attrib, val = pattern_mfcsam.match(line).groups()
        mfcsam[attrib] = int(val)

    # read and parse Aunt Sue characteristics
    # If they are equal to the one by MFCSAM, break the loop
    # For cats and trees, the input should be greater
    # For pomeranians and goldfish, it should be lesser
    for line in f.readlines():
        attribs = list(pattern_inputs.match(line).groups())
        aunt_no = attribs[0]
        attribs = attribs[1:]
        for i in range(0, len(attribs), 2):
            if attribs[i] == 'cats' or attribs[i] == 'trees':
                if mfcsam[attribs[i]] >= int(attribs[i + 1]):
                    break
            elif attribs[i] == 'pomeranians' or attribs[i] == 'goldfish':
                if mfcsam[attribs[i]] <= int(attribs[i + 1]):
                    break
            else:
                if mfcsam[attribs[i]] != int(attribs[i + 1]):
                    break
        else:
            break

# Print the Aunt no
print(aunt_no)
