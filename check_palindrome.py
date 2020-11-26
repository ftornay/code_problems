#!/usr/bin/env python3
""" CCI 1.4 Palindrome permuation
Given a string, write a function to check
if it's the permutation of a palindrome """

from collections import defaultdict as df
def check_pal(s):
    """ Check whether a string has the features of a palindrome """
    counts = df(int)
    len_without_spaces = 0
    # Count all nonspaces
    for c in s:
        if c != ' ':
            counts[c.lower()] += 1
            len_without_spaces += 1
    # Now find out how many chars occur an odd number of times
    odd_chars = 0
    for c in counts:
        if counts[c] % 2 != 0:
            odd_chars += 1
    # If string length is even there must be no odd counts
    if len_without_spaces % 2 == 0 and odd_chars == 0:
        return True
    # If string is odd there must be exactly one odd count
    if len_without_spaces % 2 != 0 and odd_chars == 1:
        return True
    # Else, it's not a palindrome
    return False

if __name__ == '__main__':
    s1 = "Tact Coa"
    s2 = "Hola al"
    s3 = "Assssscsssssa"
    assert(check_pal(s1))
    assert(not check_pal(s2))
    assert(check_pal(s3))
