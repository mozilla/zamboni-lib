"""Help to generate SQL strings usable by the Python DB-API.

:author: Logilab
:copyright: 2000-2008 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: GNU Lesser General Public License, v2.1 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"


from warnings import warn
warn('this module is deprecated, use logilab.database instead',
     DeprecationWarning, stacklevel=1)
from logilab.database.sqlgen import *
