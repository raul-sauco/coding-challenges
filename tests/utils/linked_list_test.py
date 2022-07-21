from utils.linked_list import LinkedList


# Test the LinkedList data structure.
class TestLinkedList:

    # Test that we can create a linked list from a list and the values are the expected ones
    def testCreateFromList(args):
        ll = LinkedList.fromList([1, 2, 3]).getHead()
        assert ll.val == 1
        assert ll.next is not None
        assert ll.next.val == 2
        assert ll.next.next.val == 3

    def testFindMiddleWithEvenSize(args):
        ll: LinkedList = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7, 8])
        middle = ll.findMiddle()
        assert middle.val == 4
        assert middle.next.val == 5

    def testFindMiddleWithUnevenSize(args):
        ll: LinkedList = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7])
        middle = ll.findMiddle()
        assert middle.val == 4
        assert middle.next.val == 5

    def testFindMiddleWithSizeOne(args):
        ll: LinkedList = LinkedList.fromList([1])
        middle = ll.findMiddle()
        assert middle.val == 1
        assert middle.next is None

    def testFindMiddleWithSizeTwo(args):
        ll: LinkedList = LinkedList.fromList([1, 2])
        middle = ll.findMiddle()
        assert middle.val == 1
        assert middle.next.val == 2

    def testSerialize(args):
        ll: LinkedList = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7])
        assert ll.toList() == [1, 2, 3, 4, 5, 6, 7]

    def testSplitEvenSize(ars):
        ll: LinkedList = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7, 8])
        fh, sh = ll.split()
        assert fh.toList() == [1, 2, 3, 4]
        assert sh.toList() == [5, 6, 7, 8]

    def testSplitUnevenSize(ars):
        ll: LinkedList = LinkedList.fromList([1, 2, 3, 4, 5, 6, 7])
        fh, sh = ll.split()
        assert fh.toList() == [1, 2, 3, 4]
        assert sh.toList() == [5, 6, 7]

    def testReverse(ars):
        assert LinkedList.fromList([1, 2, 3, 4, 5, 6, 7, 8]).reverse().toList() == [8, 7, 6, 5, 4, 3, 2, 1]
        assert LinkedList.fromList([1, 2]).reverse().toList() == [2, 1]
        assert LinkedList.fromList([1]).reverse().toList() == [1]
