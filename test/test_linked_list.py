"""
Linked List Unit Tests
"""
from hackerrank.linked_list import LinkedList
from hackerrank.node import Node


class TestLinkedList:

    def test_empty_list(self):
        a_list = LinkedList()
        assert a_list.is_empty()

    def test_list_with_one_element(self):
        a_list = LinkedList()
        elem_1 = Node(1)
        a_list.push(elem_1)
        assert a_list.next() == elem_1

    def test_next_with_empty_list(self):
        a_list = LinkedList()
        assert not a_list.next()

    def test_rnext_with_empty_list(self):
        a_list = LinkedList()
        assert not a_list.rnext()

    def test_list_with_two_elements(self):
        elem_1 = Node(1)
        elem_2 = Node(2)
        a_list = LinkedList()
        a_list.push(elem_1)
        a_list.push(elem_2)
        assert a_list.next() == elem_1
        assert a_list.next() == elem_2
        assert a_list.rnext() == elem_1
        assert a_list.rnext() == elem_2

    def test_pop_with_no_elements(self):
        a_list = LinkedList()
        assert not a_list.pop()

    def test_pop_with_one_element(self):
        a_list = LinkedList()
        elem_1 = Node(1)
        a_list.push(elem_1)
        element = a_list.pop()
        assert elem_1 == element

    def test_pop_with_two_elements(self):
        a_list = LinkedList()
        elem_1 = Node(1)
        elem_2 = Node(2)
        a_list.push(elem_1)
        a_list.push(elem_2)
        assert len(a_list) == 2
        a_list.pop()
        assert len(a_list) == 1
        element = a_list.pop()
        assert len(a_list) == 0
        assert elem_2 == element

    def test_list_len_with_empty_list(self):
        a_list = LinkedList()
        assert len(a_list) == 0

    def test_list_len(self):
        a_list = LinkedList()
        for i in range(5):
            a_list.push(Node(i))
        assert len(a_list) == 5

    def test_list_iter(self):
        a_list = LinkedList()
        for i in range(5):
            a_list.push(Node(i))
        for index, e in enumerate(a_list):
            assert isinstance(e, Node)
        assert index == 4
        counter = 0
        for e in a_list:
            counter += 1
            assert isinstance(e, Node)
        assert counter == 5
