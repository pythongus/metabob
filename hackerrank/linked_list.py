"""
A double linked list with head of the list.

The value of the head of the list does not count as an element of the
list.
"""
from typing import Optional
from hackerrank.node import Node


class LinkedList:
    """The implementation of a linked list."""

    def __init__(self):
        self.head = Node(None)
        self.head.left = self.head.right
        self._current_node = self.head
        self._len = 0
        self._index = 0

    def is_empty(self) -> bool:
        """Checks for the emptiness of the list"""
        return self.head.right is None

    def push(self, element: Node):
        """Appends an element to the end of the list."""
        last_element = self.head.left
        if last_element:
            last_element.right = element
            element.left = last_element
        self.head.left = element
        element.right = self.head
        if self.is_empty():
            self.head.right = element
            element.left = self.head
        self._len += 1

    def next(self) -> Optional[Node]:
        """A next element is always to the right of the current
        element."""
        if self._current_node:
            self._current_node = self._current_node.right
            return self._current_node if self._current_node != self.head else self.head.right
        return None

    def rnext(self) -> Optional[Node]:
        """Next element to the left of the current element of the list"""
        if self._current_node:
            self._current_node = self._current_node.left
            return self._current_node if self._current_node != self.head else self.head.left
        return None

    def pop(self):
        """Returns the last element of the linked list, removing it
        from the list itself. Returns None if the list is empty.
        """
        if self.head:
            self._len -= 1
            return self.head.left
        return None

    def __len__(self):
        return self._len

    def __iter__(self):
        if self._current_node == self.head:
            self._current_node = self.head.right
        while self._current_node != self.head:
            element = self._current_node
            self._current_node = self._current_node.right
            yield element

        self._current_node = self.head.right
