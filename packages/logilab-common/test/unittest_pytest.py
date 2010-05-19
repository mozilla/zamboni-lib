from os.path import join
from logilab.common.testlib import TestCase, unittest_main
from logilab.common.pytest import *

class ModuleFunctionTC(TestCase):
    def test_this_is_testdir(self):
        self.assertTrue(this_is_a_testdir("test"))
        self.assertTrue(this_is_a_testdir("tests"))
        self.assertTrue(this_is_a_testdir("unittests"))
        self.assertTrue(this_is_a_testdir("unittest"))
        self.assertFalse(this_is_a_testdir("unit"))
        self.assertFalse(this_is_a_testdir("units"))
        self.assertFalse(this_is_a_testdir("undksjhqfl"))
        self.assertFalse(this_is_a_testdir("this_is_not_a_dir_test"))
        self.assertFalse(this_is_a_testdir("this_is_not_a_testdir"))
        self.assertFalse(this_is_a_testdir("unittestsarenothere"))
        self.assertTrue(this_is_a_testdir(join("coincoin","unittests")))
        self.assertFalse(this_is_a_testdir(join("unittests","spongebob")))

    def test_this_is_testfile(self):
        self.assertTrue(this_is_a_testfile("test.py"))
        self.assertTrue(this_is_a_testfile("testbabar.py"))
        self.assertTrue(this_is_a_testfile("unittest_celestine.py"))
        self.assertTrue(this_is_a_testfile("smoketest.py"))
        self.assertFalse(this_is_a_testfile("test.pyc"))
        self.assertFalse(this_is_a_testfile("zephir_test.py"))
        self.assertFalse(this_is_a_testfile("smoketest.pl"))
        self.assertFalse(this_is_a_testfile("unittest"))
        self.assertTrue(this_is_a_testfile(join("coincoin","unittest_bibi.py")))
        self.assertFalse(this_is_a_testfile(join("unittest","spongebob.py")))

if __name__ == '__main__':
    unittest_main()
