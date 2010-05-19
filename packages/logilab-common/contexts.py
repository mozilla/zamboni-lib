"""A few useful context managers

:copyright: 2008 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: GNU Lesser General Public License, v2.1 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"

import sys

if sys.version_info < (2, 5):
    raise ImportError("python >= 2.5 is required to import logilab.common.contexts")

import os
import tempfile
import shutil

class tempdir(object):

    def __enter__(self):
        self.path = tempfile.mkdtemp()
        return self.path

    def __exit__(self, exctype, value, traceback):
        # rmtree in all cases
        shutil.rmtree(self.path)
        return traceback is None


class pushd(object):
    def __init__(self, directory):
        self.directory = directory

    def __enter__(self):
        self.cwd = os.getcwd()
        os.chdir(self.directory)
        return self.directory

    def __exit__(self, exctype, value, traceback):
        os.chdir(self.cwd)

