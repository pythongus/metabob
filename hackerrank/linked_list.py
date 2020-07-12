"""
Binary Tree Module
"""
from typing import Optional
from hackerrank.node import Node


class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head
        self._current_node = head

    def is_empty(self) -> bool:
        return self.head is None

    def next_element(self) -> Optional[Node]:
        if self._current_node:
            node = self._current_node
            self._current_node = self._current_node.right
            return node
        return None

    def previous_element(self) -> Optional[Node]:
        if self._current_node:
            node = self._current_node
            self._current_node = self._current_node.left
            return node
        return None
