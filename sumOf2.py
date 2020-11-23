#!/usr/bin/env python3
""" Return True if two numbers in a list add up to a given one """

def sumOf2(values, sum):
    """ Direct solution, double loop -> quadratic """
    for i, v1 in enumerate(values):
        for v2 in values[i+1:]:
            if v1+v2 == sum:
                return True
    return False

def sumOf2Set(values, sum):
    """ First solution to make it linear: Store in a hash set """
    setV = set(values) # Issue!!! There can't be any duplicates
    for v in values:
        dif = sum-v # Is the required difference in the list?
        if dif == v:
            # We need a duplicate!
            # But there aren't
            # Don't use the same number
            continue
        if dif in setV:
            return True
    return False

def sumOf2Dict(values, sum):
    """ To deal with duplicates, store frequencies in hash """
    dictV = dict()
    for v in values:
        if v in dictV:
            dictV[v] += 1
        else:
            dictV[v] = 1
    for v in values:
        dif = sum-v # Is the required difference in the list?
        if dif in dictV:
            if dif == v:
                # We need a duplicate, check that there is one
                if dictV[v] >= 2:
                    return True
            else:
                return True
    return False

if __name__ == "__main__":
    numbers = [10, 15, 3, 7]
    print(f"Numbers: {numbers}")
    first = 18
    print(f"Do two of those sum up to {first}?")
    print(sumOf2(numbers, first), sumOf2Set(numbers, first), sumOf2Dict(numbers, first))
    second = 20
    print(f"Do two of those sum up to {second}?")
    print(sumOf2(numbers, second), sumOf2Set(numbers, second), sumOf2Dict(numbers, second))
    double = 14
    print(f"Try {double}, the double of an existing number")
    print(sumOf2(numbers, double), sumOf2Set(numbers, double), sumOf2Dict(numbers, double))
    print("Let's add a second 7, now it should be true, but the set solution fails")
    numbers.append(7)
    print(sumOf2(numbers, double), sumOf2Set(numbers, double), sumOf2Dict(numbers, double))
