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

How many strings are nice? """


def has_bad_strings(text):
    """Check if the text has any of the bad strings"""

    bad_strings = ['ab', 'cd', 'pq', 'xy']

    # Return True if any of the bad strings are in text,
    # otherwise return False
    if any(string in text for string in bad_strings):
        return True

    return False


def has_double_letters(text):
    """Check if text has any double letters"""

    # Check if any two successive letters are the same,
    # and return True if they are, of False if there aren't any.
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return True

    return False


def has_required_vowels(text, no_of_vowels=3):
    """Check if there are the required number of vowels"""

    # Set up vowels and vowel count
    vowels = 'aeiou'
    vowel_count = 0

    # count vowels in text until it reaches no_of_vowels,
    # at which point, return True, or return False otherwise
    for character in text:
        if character in vowels:
            vowel_count += 1
            if vowel_count == no_of_vowels:
                return True

    return False


def string_is_nice(text):
    """Check if a string is nice(True) or naughty(False)"""

    # String is naughty if it has any of the bad strings
    if has_bad_strings(text):
        return False

    # Check string has double letters
    if not has_double_letters(text):
        return False

    # Check string has required number of vowels = 3
    if not has_required_vowels(text):
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
