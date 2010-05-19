"""Bases class for interfaces to provide 'light' interface handling.

 TODO:
  _ implements a check method which check that an object implements the
    interface
  _ Attribute objects

  This module requires at least python 2.2

:copyright: 2000-2010 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: GNU Lesser General Public License, v2.1 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"

from types import ListType, TupleType

class Interface(object):
    """Base class for interfaces."""
    def is_implemented_by(cls, instance):
        return implements(instance, cls)
    is_implemented_by = classmethod(is_implemented_by)


def implements(obj, interface):
    """Return true if the give object (maybe an instance or class) implements
    the interface.
    """
    kimplements = getattr(obj, '__implements__', ())
    if not isinstance(kimplements, (list, tuple)):
        kimplements = (kimplements,)
    for implementedinterface in kimplements:
        if issubclass(implementedinterface, interface):
            return True
    return False


def extend(klass, interface, _recurs=False):
    """Add interface to klass'__implements__ if not already implemented in.

    If klass is subclassed, ensure subclasses __implements__ it as well.

    NOTE: klass should be e new class.
    """
    if not implements(klass, interface):
        try:
            kimplements = klass.__implements__
            kimplementsklass = type(kimplements)
            kimplements = list(kimplements)
        except AttributeError:
            kimplementsklass = tuple
            kimplements = []
        kimplements.append(interface)
        klass.__implements__ = kimplementsklass(kimplements)
        for subklass in klass.__subclasses__():
            extend(subklass, interface, _recurs=True)
    elif _recurs:
        for subklass in klass.__subclasses__():
            extend(subklass, interface, _recurs=True)
