"""unit tests for logilab.common.deprecation"""

import warnings

from logilab.common.testlib import TestCase, unittest_main
from logilab.common import deprecation

def moving_target():
    pass

class RawInputTC(TestCase):

    # XXX with 2.6 we could test warnings
    # http://docs.python.org/library/warnings.html#testing-warnings
    # instead we just make sure it does not crash
    def setUp(self):
        warnings.simplefilter("ignore")
    def tearDown(self):
        warnings.simplefilter("default")

    def mk_func(self):
        def any_func():
            pass
        return any_func

    def test_class_deprecated(self):
        class AnyClass:
            __metaclass__ = deprecation.class_deprecated

    def test_deprecated_func(self):
        any_func = deprecation.deprecated()(self.mk_func())
        any_func()
        any_func = deprecation.deprecated('message')(self.mk_func())
        any_func()

    def test_deprecated_decorator(self):
        @deprecation.deprecated_function
        def any_func():
            pass
        any_func()

        @deprecation.deprecated()
        def any_func():
            pass
        any_func()

        @deprecation.deprecated('message')
        def any_func():
            pass
        any_func()

    def test_moved(self):
        # this test needs l.c.test.__init__
        module = 'logilab.common.test.unittest_deprecation'
        any_func = deprecation.moved(module, 'moving_target')
        any_func()

if __name__ == '__main__':
    unittest_main()
