#!/usr/bin/env python3
""" Cracking the coding interview 1.3
Replace spaces in a string with %20
"""

def str2l(s):
    """ Strings are immutable in Python
        To meet the requirements of the exercise
        we pass the string as a list with enough space
        at the end """
    n_spc = 0
    for c in s:
        if c == ' ':
            n_spc += 1
    list_out = list(s) + [''] * 2*n_spc
    return list_out, len(s)

def URLify(url_s, len_s):
    """ We change the string in_place to save space """
    # Find the spaces
    n_spaces = 0
    for c in url_s:
        if c == ' ':
            n_spaces += 1
    # We need to know to which place to copy
    end_copy = len_s
    # Positions we need to skip
    displacement = n_spaces * 2
    # We move back from space to space
    for i in range(len(url_s), 0, -1):
        if url_s[i-1] == ' ':
            pos_space = i-1
            copy_to = pos_space + displacement + 1
            copy_to_end = copy_to + end_copy - pos_space - 1
            # Copy from space position to last space or end of string
            url_s[copy_to:copy_to_end] = url_s[pos_space+1:end_copy]
            url_s[copy_to-3] = '%'
            url_s[copy_to-2] = '2'
            url_s[copy_to-1] = '0'
            displacement -= 2
            end_copy = pos_space

if __name__ == '__main__':
    s1 = 'Hola adiós'
    s2 = "Let's test how this works"
    s3 = "Mr John Smith "
    strings = [s1, s2, s3]
    for s in strings:
        # Convert to list
        l_s, n = str2l(s)
        URLify(l_s, n)
        # Convert back to string and print
        print(''.join(l_s))
