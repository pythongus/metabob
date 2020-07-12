"""
Linked List Unit Tests
"""
from hackerrank.linked_list import LinkedList


def test_empty_list():
    a_list = LinkedList()
    assert a_list.is_empty()


def test_list_with_one_element():
    a_list = LinkedList(1)
    assert a_list.head.value == 1
    assert not a_list.next_element()
    assert not a_list.previous_element()
