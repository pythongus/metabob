"""
Binary Tree Module
"""
from hackerrank.node import Node


class Tree:

    def __init__(self, root: Node):
        self.root = root
        self.height = 2 if any([root.left, root.right]) else 1

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height

    def depth_first_search(self, a_node: Node) -> bool:
        right_nodes = []
        node = self.root
        found = False
        while node and not found:
            if node.right:
                right_nodes.append(node.right)
            if node == a_node:
                found = True
            elif node.left:
                node = node.left
            else:
                node = right_nodes.pop()

        return found
