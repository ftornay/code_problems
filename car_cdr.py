#!/usr/bin/env python3
""" cons(a, b) constructs a pair
car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4 """

def cons(a, b):
    """ Given this implementation of cons, implement car and cdr """
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    """ Returns first element of pair
        or None if there is not any """
    first = lambda a, b: a
    try:
        return pair(first)
    except: # If pair not callable
        return None

def cdr(pair):
    """ Returns last element of pair
        or None if there is not any """
    last = lambda a, b: b
    try:
        return pair(last)
    except: # If pair not callable
        return None

if __name__ == '__main__':
    assert(car(cons(3,4)) == 3)
    assert(cdr(cons(3,4)) == 4)
