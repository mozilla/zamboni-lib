"""unit tests for the decorators module
"""

from logilab.common.testlib import TestCase, unittest_main
from logilab.common.decorators import monkeypatch, cached

class DecoratorsTC(TestCase):

    def test_monkeypatch_with_same_name(self):
        class MyClass: pass
        @monkeypatch(MyClass)
        def meth1(self):
            return 12
        self.assertEquals([attr for attr in dir(MyClass) if attr[:2] != '__'],
                          ['meth1'])
        inst = MyClass()
        self.assertEquals(inst.meth1(), 12)

    def test_monkeypatch_with_custom_name(self):
        class MyClass: pass
        @monkeypatch(MyClass, 'foo')
        def meth2(self, param):
            return param + 12
        self.assertEquals([attr for attr in dir(MyClass) if attr[:2] != '__'],
                          ['foo'])
        inst = MyClass()
        self.assertEquals(inst.foo(4), 16)

    def test_cached_preserves_docstrings(self):
        class Foo(object):
            @cached
            def foo(self):
                """ what's up doc ? """
            def bar(self, zogzog):
                """ what's up doc ? """
            bar = cached(bar, 1)
            @cached
            def quux(self, zogzog):
                """ what's up doc ? """
        self.assertEquals(Foo.foo.__doc__, """ what's up doc ? """)
        self.assertEquals(Foo.bar.__doc__, """ what's up doc ? """)
        self.assertEquals(Foo.quux.__doc__, """ what's up doc ? """)

if __name__ == '__main__':
    unittest_main()
