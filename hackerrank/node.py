"""
Node Module

Used by binary tree or linked list.
"""


class Node:
    """The generic node of a tree or linked list"""

    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.value == other.value
        return NotImplemented

    def __repr__(self) -> str:
        left = self.left.value if self.left else None
        right = self.right.value if self.right else None
        return f"{{{self.value}: [{left}, {right}]}}"
