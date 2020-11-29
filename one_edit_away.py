#!/usr/bin/env python3
""" CCI 1.5
    Given two strings, write a function to check
        they're no more than two edis away
        Possible edits: Insert, Remove, Replace one character """

def one_away(s1, s2):
    n_larger = len(s1)
    n_smaller = len(s2)
    if n_larger < n_smaller:
        n_larger, n_smaller = n_smaller, n_larger
        s_larger = s2
        s_smaller = s1
    else:
        s_larger = s1
        s_smaller = s2
    n_diff = n_larger - n_smaller
    # Number of edits
    n_edits = 0
    if n_diff == 0:
        # Same size, only one replacement allowed
        for c1, c2 in zip(s_larger, s_smaller):
            if c1 != c2:
                n_edits += 1
                if n_edits > 1:
                    return False
        return True
    elif n_diff == 1:
        # One char of difference, only one insert allowed
        i_smaller = 0
        # Iterate only through the smaller string
        for i_larger in range(n_smaller):
            if s_larger[i_larger] != s_smaller[i_smaller]:
                n_edits += 1
                if n_edits > 1:
                    return False
            else:
                # but don't advance the index to the smaller one
                # unless the characters match
                i_smaller += 1
        return True
    else:
        # More than two characters of difference
        return False

if __name__ == '__main__':
    s0 = 'pale'
    s1 = 'pales' # One inserted
    s2 = 'ple' # One removed
    s3 = 'bale' # One replaced
    s4 = 'bake' # Two away!!

    assert(one_away(s0, s1))
    assert(one_away(s0, s2))
    assert(one_away(s0, s3))
    assert(not one_away(s0, s4))
