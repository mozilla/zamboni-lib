# unit tests for the cache module

from logilab.common.testlib import TestCase, unittest_main
from logilab.common.graph import get_cycles, has_path

class getCyclesTC(TestCase):

    def test_known0(self):
        self.assertEqual(get_cycles({1:[2], 2:[3], 3:[1]}), [[1, 2, 3]])

    def test_known1(self):
        self.assertEqual(get_cycles({1:[2], 2:[3], 3:[1, 4], 4:[3]}), [[1, 2, 3], [3, 4]])

    def test_known2(self):
        self.assertEqual(get_cycles({1:[2], 2:[3], 3:[0], 0:[]}), [])


class hasPathTC(TestCase):

    def test_direct_connection(self):
        self.assertEquals(has_path({'A': ['B'], 'B': ['A']}, 'A', 'B'), ['B'])

    def test_indirect_connection(self):
        self.assertEquals(has_path({'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}, 'A', 'C'), ['B', 'C'])

    def test_no_connection(self):
        self.assertEquals(has_path({'A': ['B'], 'B': ['A']}, 'A', 'C'), None)

    def test_cycle(self):
        self.assertEquals(has_path({'A': ['A']}, 'A', 'B'), None)

if __name__ == "__main__":
    unittest_main()
