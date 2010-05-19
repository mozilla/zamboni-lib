# -*- coding: utf-8 -*-
"""XML utilities.

This module contains useful functions for parsing and using XML data. For the
moment, there is only one function that can parse the data inside a processing
instruction and return a Python dictionary.

:copyright: 2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: GNU Lesser General Public License, v2.1 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"

import re

RE_DOUBLE_QUOTE = re.compile('([\w\-\.]+)="([^"]+)"')
RE_SIMPLE_QUOTE = re.compile("([\w\-\.]+)='([^']+)'")

def parse_pi_data(pi_data):
    """
    Utility function that parses the data contained in an XML
    processing instruction and returns a dictionary of keywords and their
    associated values (most of the time, the processing instructions contain
    data like ``keyword="value"``, if a keyword is not associated to a value,
    for example ``keyword``, it will be associated to ``None``).

    :param pi_data: data contained in an XML processing instruction.
    :type pi_data: unicode

    :returns: Dictionary of the keywords (Unicode strings) associated to
              their values (Unicode strings) as they were defined in the
              data.
    :rtype: dict
    """
    results = {}
    for elt in pi_data.split():
        if RE_DOUBLE_QUOTE.match(elt):
            kwd, val = RE_DOUBLE_QUOTE.match(elt).groups()
        elif RE_SIMPLE_QUOTE.match(elt):
            kwd, val = RE_SIMPLE_QUOTE.match(elt).groups()
        else:
            kwd, val = elt, None
        results[kwd] = val
    return results
