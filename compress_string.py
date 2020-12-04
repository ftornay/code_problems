#!/usr/bin/env python3
""" CCI 1.6
    Basic string compression using the counts of repeated characters:
"""

def compress_string(s):
    """ Naive approach but it works in O(n) """
    aux_list = []
    cur_char = 0
    index = 0
    len_s = len(s)
    while index < len_s:
        cur_char = s[index]
        count = 0 
        while  index < len_s and s[index] == cur_char:
            count += 1
            index += 1
        aux_list.append(cur_char)
        aux_list.append(str(count))
    if len(aux_list) < len_s:
        return ''.join(aux_list)
    else:
        return s

if __name__ == '__main__':
    s = 'aabcccccaaa'
    s_compress = 'a2b1c5a3'
    assert(compress_string(s) == s_compress)
