#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins
(very similar to bitcoins) to use as gifts for all the
economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which,
in hexadecimal, start with at least five zeroes.
The input to the MD5 hash is some secret key
(your puzzle input, given below) followed by a number in decimal.
To mine AdventCoins, you must find Santa the lowest positive number
(no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef,
the answer is 609043, because the MD5 hash of abcdef609043
starts with five zeroes (000001dbbfa...),
and it is the lowest such number to do so.

If your secret key is pqrstuv,
the lowest number it combines with to make an MD5 hash
starting with five zeroes is 1048970;
that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

--- Part Two ---

Now find one that starts with six zeroes. """


def calculate_md5(text):
    """Calculate the MD5 hash for the give text"""

    import hashlib
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def check_required_hash(md5_hash):
    """Check if the Md5 hash satisfies the required conditions"""

    # Check if MD5 hash starts with 6 zeroes
    if md5_hash.find('000000') == 0:
        return True
    return False


def get_answer(filename):
    """Get answer for which number satisfies Md5 hash"""

    # Read text from file
    with open(filename, 'r') as f:
        text = f.readline().strip()

    # Set starting number to 0.
    # Calculate MD5 hash for each number, and check
    # if it satisfies the required condition.
    # Increment number otherwise.
    number = 0
    while True:
        md5_hash = calculate_md5(text + str(number))
        if check_required_hash(md5_hash):
            break
        else:
            number += 1

    return number


if __name__ == '__main__':

    number = get_answer('./input.txt')
    print(number)
