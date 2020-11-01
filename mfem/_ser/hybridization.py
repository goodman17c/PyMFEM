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
    from . import _hybridization
else:
    import _hybridization

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _hybridization.SWIG_PyInstanceMethod_New
_swig_new_static_method = _hybridization.SWIG_PyStaticMethod_New

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

import mfem._ser.fespace
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.mesh
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.bilininteg
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.linearform
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.handle
import mfem._ser.restriction
class Hybridization(object):
    r"""Proxy of C++ mfem::Hybridization class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, fespace, c_fespace):
        r"""__init__(Hybridization self, FiniteElementSpace fespace, FiniteElementSpace c_fespace) -> Hybridization"""
        _hybridization.Hybridization_swiginit(self, _hybridization.new_Hybridization(fespace, c_fespace))
    __swig_destroy__ = _hybridization.delete_Hybridization

    def SetConstraintIntegrator(self, c_integ):
        r"""SetConstraintIntegrator(Hybridization self, BilinearFormIntegrator c_integ)"""
        return _hybridization.Hybridization_SetConstraintIntegrator(self, c_integ)
    SetConstraintIntegrator = _swig_new_instance_method(_hybridization.Hybridization_SetConstraintIntegrator)

    def Init(self, ess_tdof_list):
        r"""Init(Hybridization self, intArray ess_tdof_list)"""
        return _hybridization.Hybridization_Init(self, ess_tdof_list)
    Init = _swig_new_instance_method(_hybridization.Hybridization_Init)

    def AssembleMatrix(self, el, A):
        r"""AssembleMatrix(Hybridization self, int el, DenseMatrix A)"""
        return _hybridization.Hybridization_AssembleMatrix(self, el, A)
    AssembleMatrix = _swig_new_instance_method(_hybridization.Hybridization_AssembleMatrix)

    def AssembleBdrMatrix(self, bdr_el, A):
        r"""AssembleBdrMatrix(Hybridization self, int bdr_el, DenseMatrix A)"""
        return _hybridization.Hybridization_AssembleBdrMatrix(self, bdr_el, A)
    AssembleBdrMatrix = _swig_new_instance_method(_hybridization.Hybridization_AssembleBdrMatrix)

    def Finalize(self):
        r"""Finalize(Hybridization self)"""
        return _hybridization.Hybridization_Finalize(self)
    Finalize = _swig_new_instance_method(_hybridization.Hybridization_Finalize)

    def GetMatrix(self):
        r"""GetMatrix(Hybridization self) -> SparseMatrix"""
        return _hybridization.Hybridization_GetMatrix(self)
    GetMatrix = _swig_new_instance_method(_hybridization.Hybridization_GetMatrix)

    def ReduceRHS(self, b, b_r):
        r"""ReduceRHS(Hybridization self, Vector b, Vector b_r)"""
        return _hybridization.Hybridization_ReduceRHS(self, b, b_r)
    ReduceRHS = _swig_new_instance_method(_hybridization.Hybridization_ReduceRHS)

    def ComputeSolution(self, b, sol_r, sol):
        r"""ComputeSolution(Hybridization self, Vector b, Vector sol_r, Vector sol)"""
        return _hybridization.Hybridization_ComputeSolution(self, b, sol_r, sol)
    ComputeSolution = _swig_new_instance_method(_hybridization.Hybridization_ComputeSolution)

    def Reset(self):
        r"""Reset(Hybridization self)"""
        return _hybridization.Hybridization_Reset(self)
    Reset = _swig_new_instance_method(_hybridization.Hybridization_Reset)

# Register Hybridization in _hybridization:
_hybridization.Hybridization_swigregister(Hybridization)



