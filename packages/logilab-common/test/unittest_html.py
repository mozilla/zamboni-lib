# -*- coding: utf-8 -*-
"""unittests for logilab.common.html

:organization: Logilab
:copyright: 2001-2010 LOGILAB S.A. (Paris, FRANCE), license is LGPL v2.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: GNU Lesser General Public License, v2.1 - http://www.gnu.org/licenses
"""

__docformat__ = "restructuredtext en"

from logilab.common.testlib import TestCase, unittest_main
from logilab.common.tree import Node

from logilab.common import html

tree = ('root', (
    ('child_1_1', (
    ('child_2_1', ()), ('child_2_2', (
    ('child_3_1', ()),
    ('child_3_2', ()),
    ('child_3_3', ()),
    )))),
    ('child_1_2', (('child_2_3', ()),))))

generated_html = """\
<table class="tree">
<tr><td class="tree_cell" rowspan="2"><div class="tree_cell">root</div></td><td class="tree_cell_1_1">&nbsp;</td><td class="tree_cell_1_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="tree_cell">child_1_1</div></td><td class="tree_cell_1_1">&nbsp;</td><td class="tree_cell_1_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="tree_cell">child_2_1</div></td><td class="tree_cell_0_1">&nbsp;</td><td class="tree_cell_0_2">&nbsp;</td><td rowspan="2">&nbsp;</td></tr>
<tr><td class="tree_cell_1_3">&nbsp;</td><td class="tree_cell_1_4">&nbsp;</td><td class="tree_cell_1_3">&nbsp;</td><td class="tree_cell_1_4">&nbsp;</td><td class="tree_cell_0_3">&nbsp;</td><td class="tree_cell_0_4">&nbsp;</td></tr>
<tr><td rowspan="2">&nbsp;</td><td class="tree_cell_2_1">&nbsp;</td><td class="tree_cell_2_2">&nbsp;</td><td rowspan="2">&nbsp;</td><td class="tree_cell_4_1">&nbsp;</td><td class="tree_cell_4_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="selected tree_cell">child_2_2</div></td><td class="tree_cell_1_1">&nbsp;</td><td class="tree_cell_1_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="tree_cell">child_3_1</div></td></tr>
<tr><td class="tree_cell_2_3">&nbsp;</td><td class="tree_cell_2_4">&nbsp;</td><td class="tree_cell_4_3">&nbsp;</td><td class="tree_cell_4_4">&nbsp;</td><td class="tree_cell_1_3">&nbsp;</td><td class="tree_cell_1_4">&nbsp;</td></tr>
<tr><td rowspan="2">&nbsp;</td><td class="tree_cell_2_1">&nbsp;</td><td class="tree_cell_2_2">&nbsp;</td><td rowspan="2">&nbsp;</td><td class="tree_cell_0_1">&nbsp;</td><td class="tree_cell_0_2">&nbsp;</td><td rowspan="2">&nbsp;</td><td class="tree_cell_3_1">&nbsp;</td><td class="tree_cell_3_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="tree_cell">child_3_2</div></td></tr>
<tr><td class="tree_cell_2_3">&nbsp;</td><td class="tree_cell_2_4">&nbsp;</td><td class="tree_cell_0_3">&nbsp;</td><td class="tree_cell_0_4">&nbsp;</td><td class="tree_cell_3_3">&nbsp;</td><td class="tree_cell_3_4">&nbsp;</td></tr>
<tr><td rowspan="2">&nbsp;</td><td class="tree_cell_2_1">&nbsp;</td><td class="tree_cell_2_2">&nbsp;</td><td rowspan="2">&nbsp;</td><td class="tree_cell_0_1">&nbsp;</td><td class="tree_cell_0_2">&nbsp;</td><td rowspan="2">&nbsp;</td><td class="tree_cell_4_1">&nbsp;</td><td class="tree_cell_4_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="tree_cell">child_3_3</div></td></tr>
<tr><td class="tree_cell_2_3">&nbsp;</td><td class="tree_cell_2_4">&nbsp;</td><td class="tree_cell_0_3">&nbsp;</td><td class="tree_cell_0_4">&nbsp;</td><td class="tree_cell_4_3">&nbsp;</td><td class="tree_cell_4_4">&nbsp;</td></tr>
<tr><td rowspan="2">&nbsp;</td><td class="tree_cell_4_1">&nbsp;</td><td class="tree_cell_4_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="tree_cell">child_1_2</div></td><td class="tree_cell_5_1">&nbsp;</td><td class="tree_cell_5_2">&nbsp;</td><td class="tree_cell" rowspan="2"><div class="tree_cell">child_2_3</div></td><td class="tree_cell_0_1">&nbsp;</td><td class="tree_cell_0_2">&nbsp;</td><td rowspan="2">&nbsp;</td></tr>
<tr><td class="tree_cell_4_3">&nbsp;</td><td class="tree_cell_4_4">&nbsp;</td><td class="tree_cell_5_3">&nbsp;</td><td class="tree_cell_5_4">&nbsp;</td><td class="tree_cell_0_3">&nbsp;</td><td class="tree_cell_0_4">&nbsp;</td></tr>
</table>\
"""

def make_tree(tupletree):
    n = Node(tupletree[0])
    for child in tupletree[1]:
        n.append(make_tree(child))
    return n

class UIlibHTMLGenerationTC(TestCase):
    """ a basic tree node, caracterised by an id"""
    def setUp(self):
        """ called before each test from this class """
        self.o = make_tree(tree)

    def test_generated_html(self):
        s = html.render_HTML_tree(self.o, selected_node="child_2_2")
        self.assertTextEqual(s, generated_html)


if __name__ == '__main__':
    unittest_main()
