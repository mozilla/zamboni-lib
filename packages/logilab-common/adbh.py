"""Helpers for DBMS specific (advanced or non standard) functionalities.
"""
__docformat__ = "restructuredtext en"

from warnings import warn
warn('this module is deprecated, use logilab.database instead',
     DeprecationWarning, stacklevel=1)

from logilab.database import (FunctionDescr, get_db_helper as get_adv_func_helper,
                        _GenericAdvFuncHelper,
                        _ADV_FUNC_HELPER_DIRECTORY as ADV_FUNC_HELPER_DIRECTORY)
from logilab.common.decorators import monkeypatch

@monkeypatch(_GenericAdvFuncHelper, 'func_sqlname')
@classmethod
def func_sqlname(cls, funcname):
    funcdef = cls.function_description(funcname)
    return funcdef.name_mapping.get(cls.backend_name, funcname)
