#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" --- Day 11: Corporate Policy ---

Santa's previous password expired,
and he needs help choosing a new one.

To help him remember his new password after the old one expires,
Santa has devised a method of coming up with a password
based on the previous one.
Corporate policy dictates that passwords must be exactly
eight lowercase letters (for security reasons),
so he finds his new password by incrementing his old password string
repeatedly until it is valid.

Incrementing is just like counting with numbers:
xx, xy, xz, ya, yb, and so on.
Increase the rightmost letter one step; if it was z,
it wraps around to a,
and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa,
a new Security-Elf recently started,
and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters,
like abc, bcd, cde, and so on, up to xyz.
They cannot skip letters; abd doesn't count.

Passwords may not contain the letters i, o, or l,
as these letters can be mistaken for other characters
and are therefore confusing.

Passwords must contain at least two different,
non-overlapping pairs of letters,
like aa, bb, or zz.

For example:

hijklmmn meets the first requirement (because it contains the straight hij)
but fails the second requirement requirement (because it contains i and l).

abbceffg meets the third requirement (because it repeats bb and ff)
but fails the first requirement.

abbcegjk fails the third requirement,
because it only has one double letter (bb).

The next password after abcdefgh is abcdffaa.

The next password after ghijklmn is ghjaabcc,
because you eventually skip all the passwords that start with ghi...,
since i is not allowed.

Given Santa's current password (your puzzle input),
what should his next password be?

--- Part Two ---

Santa's password expired again. What's the next one? """


import re


def has_bad_letters(password):
    """Check if password string has any of the bad characters"""

    if 'i' in password:
        return True
    if 'o' in password:
        return True
    if 'l' in password:
        return True
    return False


def has_double_pair(password):
    """Check if password has two pairs of repeating letters"""

    # reconvert the password character array to string
    password = ''.join([chr(c) for c in password])

    # pattern matches all repeating characters twice
    pattern = r'(.)\1'

    if len(re.findall(pattern, password)) < 2:
        return False
    return True


def has_consecutive_letters(password):
    """Check if password has three consecutive sequenced letters"""

    # Check each set of three letters to see if they differ by 1
    # in their ascii code
    for i in range(len(password) - 2):
        if ((password[i] - password[i + 1] == -1) and
                (password[i + 1] - password[i + 2] == -1)):
            return True
    return False


def increment(password):
    """ Increment the password string.
    Will increase the right-most character by 1,
    and if it wraps around back to a,
    will move to the character on the left. """

    # Iterate over the password string right to left
    # i goes from 0 to len(p) - 1
    # Therefore, j = -1 - i will go from len(p) -1 to 0
    for i in range(len(password)):

        # Increment and wrap character within the range a-z
        # p[-1 - i] + 1 : increment character by 1
        # - 97 : substract from 'a' to get relative position
        # % 26 : keep it within 0 - 25 the character range
        # + 97 : add 'a' again to make it an ascii letter
        # This increments the range from 97 to 122 (97 + 26)
        # and then wraps it back to 97 instead of 123
        password[-1 - i] = 97 + (password[-1 - i] + 1 - 97) % 26

        # check if character has wrapped by checking if it is 'a'
        # because 'z' -> 'a'
        # If character has not wrapped, break the loop
        if password[-1 - i] != 97:
            break

    return password


def find_password(password):
    """Find the next password given the current password string"""

    # Convert the password into a character array
    password = [ord(c) for c in password]

    # Continue as long as there's no valid password
    while True:

        # increment password
        password = increment(password)

        # check if it has bad letters
        if has_bad_letters(password):
            continue

        # check if it has consecutive letters
        if not has_consecutive_letters(password):
            continue

        # check if it has double pair of repeating characters
        if not has_double_pair(password):
            continue

        # if it satisfies all the conditions, break the loop
        break

    # return the string form of the password
    return ''.join([chr(c) for c in password])


# read password string from input file
with open('./input.txt', 'r') as f:
    password = f.readline().strip()


# get next password
password = find_password(password)
# the last password expired, find another one
password = find_password(password)
print(password)
