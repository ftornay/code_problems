#!/usr/bin/env python3
""" Cracking the Coding Interview 1.1
    Does string contain all unique characters? """

def is_unique_hash(s):
    """ Using a hash
        O(n) """
    d = {}
    for c in s:
        if c in d:
            # Checking if key in dict is O(1)!!!
            return False
        else:
            d[c] = 1
    return True

def is_unique_sort(s):
    """ Sort the string first
        O(n log(n)) """
    # To avoid extra space
    # use an in-place sorting algorithm
    s_sorted = sorted(s)
    prev = ''
    for c in s_sorted:
        if c == prev:
            return False
        prev = c
    return True

def is_unique_bits(s):
    """ Use a bit array instead of hash
            to save space
            O(n) """
    bit_ar = 0
    for c in s:
        # Python's bignums have unlimited range
        # implemented by using C structs
        # In C we would set up a struct/array of integers
        # large enough to contain all possible characters
        # 128 bits if we assume ASCII strings
        mask = 1 << ord(c)
        if mask & bit_ar != 0:
            # Bit set, it's a duplicate!
            return False
        else:
            # Set the bit
            bit_ar |= mask
    return True

if __name__ == '__main__':
    s_unique = "abcdefgh"
    s_repeat = "abcdefbcaf"
    assert(is_unique_hash(s_unique))
    assert(not is_unique_hash(s_repeat))
    assert(is_unique_sort(s_unique))
    assert(not is_unique_sort(s_repeat))
    assert(is_unique_bits(s_unique))
    assert(not is_unique_bits(s_repeat))
