"""
Tests for the XML challenge # 2.
"""
import xml.etree.ElementTree as etree
import pytest

XML1 = """<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
</feed>"""
XML2 = """<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
    <author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>"""
XML3 = """<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
    <author gender='male'>Harsh</author>
    <question type='hard'>
      <text>XML 1</text>
    </question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>"""
maxdepth = 0


def root(xml):
    tree = etree.ElementTree(etree.fromstring(xml))
    return tree.getroot()


def test_maxdepth_1():
    depth(root(XML1), 0)
    assert maxdepth == 1


def test_maxdepth_2():
    depth(root(XML2), 0)
    assert maxdepth == 2


def test_maxdepth_3():
    depth(root(XML3), 0)
    assert maxdepth == 3


def depth(elem, level):

    def check_depth(elem, depth):
        global maxdepth
        if not len(elem):
            if depth > maxdepth:
                maxdepth = depth
        else:
            check_depth(elem[1:], depth)
            check_depth(elem[0], depth + 1)

    check_depth(elem, level)
