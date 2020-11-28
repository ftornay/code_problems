#!/usr/bin/env python3
""" Serialize tree into string and deserialize it """
import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return "None"
    left = serialize(root.left)
    right = serialize(root.right)
    return "(" + root.val + " " + left + " " + right + ")" 

def deserialize(string):
    if string == "None":
        return None
    pat = re.compile(r'^\(([^\s]+)\s((\(.+\))|None)\s((\(.+\))|None)\)$')
    m = re.match(pat, string)
    if m is None:
        raise ValueError("Unrecognized string format")
    val = m.group(1)
    left = deserialize(m.group(2))
    right = deserialize(m.group(4))
    return Node(val, left, right)

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    string = serialize(node)
    print(string)
    new_node = deserialize(string)
    assert deserialize(serialize(node)).left.left.val == 'left.left'
