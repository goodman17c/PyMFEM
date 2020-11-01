# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _stable3d
else:
    import _stable3d

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _stable3d.SWIG_PyInstanceMethod_New
_swig_new_static_method = _stable3d.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._par.element
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.densemat
import mfem._par.vector
import mfem._par.operators
import mfem._par.matrix
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
class STable3DNode(object):
    r"""Proxy of C++ mfem::STable3DNode class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Prev = property(_stable3d.STable3DNode_Prev_get, _stable3d.STable3DNode_Prev_set, doc=r"""Prev : p.mfem::STable3DNode""")
    Column = property(_stable3d.STable3DNode_Column_get, _stable3d.STable3DNode_Column_set, doc=r"""Column : int""")
    Floor = property(_stable3d.STable3DNode_Floor_get, _stable3d.STable3DNode_Floor_set, doc=r"""Floor : int""")
    Number = property(_stable3d.STable3DNode_Number_get, _stable3d.STable3DNode_Number_set, doc=r"""Number : int""")

    def __init__(self):
        r"""__init__(STable3DNode self) -> STable3DNode"""
        _stable3d.STable3DNode_swiginit(self, _stable3d.new_STable3DNode())
    __swig_destroy__ = _stable3d.delete_STable3DNode

# Register STable3DNode in _stable3d:
_stable3d.STable3DNode_swigregister(STable3DNode)

class STable3D(object):
    r"""Proxy of C++ mfem::STable3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nr):
        r"""__init__(STable3D self, int nr) -> STable3D"""
        _stable3d.STable3D_swiginit(self, _stable3d.new_STable3D(nr))

    def Push(self, r, c, f):
        r"""Push(STable3D self, int r, int c, int f) -> int"""
        return _stable3d.STable3D_Push(self, r, c, f)
    Push = _swig_new_instance_method(_stable3d.STable3D_Push)

    def Index(self, r, c, f):
        r"""Index(STable3D self, int r, int c, int f) -> int"""
        return _stable3d.STable3D_Index(self, r, c, f)
    Index = _swig_new_instance_method(_stable3d.STable3D_Index)

    def Push4(self, r, c, f, t):
        r"""Push4(STable3D self, int r, int c, int f, int t) -> int"""
        return _stable3d.STable3D_Push4(self, r, c, f, t)
    Push4 = _swig_new_instance_method(_stable3d.STable3D_Push4)

    def __call__(self, *args):
        r"""
        __call__(STable3D self, int r, int c, int f) -> int
        __call__(STable3D self, int r, int c, int f, int t) -> int
        """
        return _stable3d.STable3D___call__(self, *args)
    __call__ = _swig_new_instance_method(_stable3d.STable3D___call__)

    def NumberOfElements(self):
        r"""NumberOfElements(STable3D self) -> int"""
        return _stable3d.STable3D_NumberOfElements(self)
    NumberOfElements = _swig_new_instance_method(_stable3d.STable3D_NumberOfElements)
    __swig_destroy__ = _stable3d.delete_STable3D

    def Print(self, *args):
        r"""
        Print(STable3D self, std::ostream & out=out)
        Print(STable3D self, char const * file, int precision=8)
        """
        return _stable3d.STable3D_Print(self, *args)
    Print = _swig_new_instance_method(_stable3d.STable3D_Print)

# Register STable3D in _stable3d:
_stable3d.STable3D_swigregister(STable3D)



