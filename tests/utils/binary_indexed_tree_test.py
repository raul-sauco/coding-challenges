from utils.binary_indexed_tree import BinaryIndexedTree


# Test the binary indexed tree data structure.
class TestBinaryIndexedTree:
    def testCreateFromList(args):
        values = [3, 10, 0, 7, 1, -13, 6, -5, 16, 7, 3, -9]
        sums = [3, 13, 13, 20, 21, 8, 14, 9, 25, 32, 35, 26]

        bit = BinaryIndexedTree.fromList(values)
        for i in range(len(values)):
            assert bit.getSum(i) == sums[i]

    def testGetSum(args):
        # Create an empty binary indexed tree with 0 positions.
        bit = BinaryIndexedTree(8)
        # Add 3 at index 2
        bit.update(2, 3)
        # Add 4 at index 3
        bit.update(3, 4)

        assert bit.getSum(2) == 3
        assert bit.getSum(3) == 7

    def testUpdate(args):
        values = [3, 10, 0, 7, 1, -13, 6, -5, 16, 7, 3, -9]
        bit = BinaryIndexedTree.fromList(values)

        # Update the value at index 9
        bit.update(9, -30)

        # Expect the sum [0:9] to have been updated.
        assert bit.getSum(10) == 5

    def testGetRangeSum(args):
        values = [3, 10, 0, 7, 1, -13, 6, -5, 16, 7, 3, -9]
        bit = BinaryIndexedTree.fromList(values)
        assert bit.getRangeSum(4, 8) == -11
