#!/usr/bin/env python3
""" Cracking the Coding Interview 1.2
    Check that two strings are permutations of each other """

def is_perm_sort(s1, s2):
    """ Sort both and compare
        O(a log(a) + b log(b)) """
    return sorted(s1) == sorted(s2)

from collections import defaultdict as df
def is_perm_hash(s1, s2):
    """ With hashes we need O(a+b) space
        but we achieve O(a+b) time """
    # Alternative: use two heaps
    if len(s1) != len(s2):
        return False
    hash1 = df(int)
    hash2 = df(int)
    for c1, c2 in zip(s1, s2):
        hash1[c1] += 1
        hash2[c2] += 1
    for c in s1:
        if hash1[c] != hash2[c]:
            return False
    return True

if __name__ == '__main__':
    s1 = "abcdefgh"
    s2 = "fgacedhb"
    s3 = "abckrfhg"
    assert(is_perm_sort(s1, s2))
    assert(not is_perm_sort(s1, s3))
    assert(is_perm_hash(s1, s2))
    assert(not is_perm_hash(s1, s3))
