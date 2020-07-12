"""
Binary Tree Unit Tests
"""
from hackerrank.node import Node
from hackerrank.binary_tree import Tree


def test_create_node():
    node = Node(1, Node(2), Node(3))
    assert node.value == 1
    assert node.left.value == 2
    assert node.right.value == 3


def test_tree_heigh_1():
    tree = Tree(Node(1))
    assert tree.height == 1


def test_tree_heigh_2():
    tree = Tree(Node(1, Node(2), Node(3)))
    assert tree.height == 2


def test_depth_first_search_1():
    tree = Tree(Node(1))
    assert tree.depth_first_search(Node(1))


def test_depth_first_search_2():
    tree = Tree(Node(1, Node(2), Node(3)))
    assert tree.depth_first_search(Node(2))


def test_depth_first_search_3():
    tree = Tree(Node(1, Node(2), Node(3)))
    assert tree.depth_first_search(Node(3))
