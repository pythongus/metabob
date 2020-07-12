import json
import sys


def min_values(root_node):
   def min_values(root_node):
    a, b = None, None
    if root_node is not None:
        if root_node.left is not None and root_node.right is not None:
            a, b = root_node.left.value, root_node.right.value
            if a is not None and b is not None:
                if a > b:
                    a, b = b, a
        elif root_node.left is None and root_node.right is not None:
            b = root_node.right.value
        elif root_node.right is None and root_node.left is not None:
            b = root_node.left.value

    return a,  b


class Node():
    left = None
    right = None
    value = None

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    @classmethod
    def from_json(cls, j):
        if j is None:
            return None
        return Node(value=j.get('value'), left=Node.from_json(j.get('left')), right=Node.from_json(j.get('right')))

print(min_values(Node.from_json(json.loads(sys.stdin.read().strip()))))
