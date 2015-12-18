#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his
text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only),
like aei, xazegov, or aeiouaeiouaeiou.

It contains at least one letter that appears twice in a row,
like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy,
even if they are part of one of the other requirements.

For example:

ugknbfddgicrmopn is nice because it has at least three vowels
(u...i...o...), a double letter (...dd...),
and none of the disallowed substrings.

aaa is nice because it has at least three vowels and a double letter,
even though the letters used by different rules overlap.

jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model
of determining whether a string is naughty or nice.
None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice
in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
but not like aaa (aa, but it overlaps).

It contains at least one letter
which repeats with exactly one letter between them,
like xyx, abcdefeghi (efe), or even aaa.

For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
and a letter that repeats with exactly one letter between them (zxz).

xxyxx is nice because it has a pair that appears twice
and a letter that repeats with one between,
even though the letters used by each rule overlap.

uurcxstgmygtbstg is naughty because it has a pair (tg)
but no repeat with a single letter between them.

ieodomkazucvgmuy is naughty because it has a repeating letter
with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules? """


def has_double_pair(text):
    """Check if a string has a pair appearing twice without overlapping"""

    # Go over each pair of letters, and see if they occur more than once.
    # The string.count method checks only for non-overlapping strings.
    # Return True if there are two or more, False otherwise.
    for i in range(len(text) - 3):
        if text.count("{}{}".format(text[i], text[i + 1])) >= 2:
            return True

    return False


def has_repeating_letter(text):
    """Check if a string has a repeating letter with one letter in between"""

    # Check every combination of three letters
    # and see if the first and third are the same.
    # If there is any such combination, return True, False otherwise.
    for i in range(len(text) - 2):
        if text[i] == text[i + 2]:
            return True

    return False


def string_is_nice(text):
    """Check if a string is nice(True) or naughty(False)"""

    # String is naughty if
    # it doesn't have any repeating but non-overlapping pair
    if not has_double_pair(text):
        return False

    # String is naughty if
    # it doesn't have any repeating letters with one letter between them
    if not has_repeating_letter(text):
        return False

    # String satisfies all conditions, therefore it is nice
    return True


def get_answer(filename):
    """Check number of nice strings in file"""

    nice_strings = 0

    # Iterate over every line and check if string is nice,
    # increment counter if it is.
    with open(filename, 'r') as f:
        for line in f.readlines():
            if string_is_nice(line):
                nice_strings += 1

    return nice_strings


if __name__ == '__main__':

    nice_strings = get_answer('./input.txt')
    print(nice_strings)
