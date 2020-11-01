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
    from . import _complex_operator
else:
    import _complex_operator

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _complex_operator.SWIG_PyInstanceMethod_New
_swig_new_static_method = _complex_operator.SWIG_PyStaticMethod_New

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

import mfem._ser.vector
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.operators
import mfem._ser.sparsemat
import mfem._ser.matrix
import mfem._ser.densemat
class ComplexOperator(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::ComplexOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    HERMITIAN = _complex_operator.ComplexOperator_HERMITIAN
    
    BLOCK_SYMMETRIC = _complex_operator.ComplexOperator_BLOCK_SYMMETRIC
    
    __swig_destroy__ = _complex_operator.delete_ComplexOperator

    def hasRealPart(self):
        r"""hasRealPart(ComplexOperator self) -> bool"""
        return _complex_operator.ComplexOperator_hasRealPart(self)
    hasRealPart = _swig_new_instance_method(_complex_operator.ComplexOperator_hasRealPart)

    def hasImagPart(self):
        r"""hasImagPart(ComplexOperator self) -> bool"""
        return _complex_operator.ComplexOperator_hasImagPart(self)
    hasImagPart = _swig_new_instance_method(_complex_operator.ComplexOperator_hasImagPart)

    def real(self, *args):
        r"""
        real(ComplexOperator self) -> Operator
        real(ComplexOperator self) -> Operator
        """
        return _complex_operator.ComplexOperator_real(self, *args)
    real = _swig_new_instance_method(_complex_operator.ComplexOperator_real)

    def imag(self, *args):
        r"""
        imag(ComplexOperator self) -> Operator
        imag(ComplexOperator self) -> Operator
        """
        return _complex_operator.ComplexOperator_imag(self, *args)
    imag = _swig_new_instance_method(_complex_operator.ComplexOperator_imag)

    def Mult(self, x, y):
        r"""Mult(ComplexOperator self, Vector x, Vector y)"""
        return _complex_operator.ComplexOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_complex_operator.ComplexOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(ComplexOperator self, Vector x, Vector y)"""
        return _complex_operator.ComplexOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_complex_operator.ComplexOperator_MultTranspose)

    def GetType(self):
        r"""GetType(ComplexOperator self) -> mfem::Operator::Type"""
        return _complex_operator.ComplexOperator_GetType(self)
    GetType = _swig_new_instance_method(_complex_operator.ComplexOperator_GetType)

    def GetConvention(self):
        r"""GetConvention(ComplexOperator self) -> mfem::ComplexOperator::Convention"""
        return _complex_operator.ComplexOperator_GetConvention(self)
    GetConvention = _swig_new_instance_method(_complex_operator.ComplexOperator_GetConvention)

    def __init__(self, Op_Real, Op_Imag, ownReal=False, ownImag=False, hermitan=True):
        r"""__init__(ComplexOperator self, Operator Op_Real, Operator Op_Imag, bool ownReal=False, bool ownImag=False, bool hermitan=True) -> ComplexOperator"""

        self._parts = [Op_Real, Op_Imag]
        if ownReal:
           assert Op_Real.thisown != 0, "Real Op is not owned by passed object"
           Op_Real.thisown = 0
        if ownImag:
           assert Op_Real.thisown != 0, "Imag Op is not owned by passed object"     
           Op_Imag.thisown = 0


        _complex_operator.ComplexOperator_swiginit(self, _complex_operator.new_ComplexOperator(Op_Real, Op_Imag, ownReal, ownImag, hermitan))

# Register ComplexOperator in _complex_operator:
_complex_operator.ComplexOperator_swigregister(ComplexOperator)

class ComplexSparseMatrix(ComplexOperator):
    r"""Proxy of C++ mfem::ComplexSparseMatrix class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(ComplexSparseMatrix self, SparseMatrix A_Real, SparseMatrix A_Imag, bool ownReal, bool ownImag, mfem::ComplexOperator::Convention convention=HERMITIAN) -> ComplexSparseMatrix"""
        _complex_operator.ComplexSparseMatrix_swiginit(self, _complex_operator.new_ComplexSparseMatrix(*args, **kwargs))

    def real(self, *args):
        r"""
        real(ComplexSparseMatrix self) -> SparseMatrix
        real(ComplexSparseMatrix self) -> SparseMatrix
        """
        return _complex_operator.ComplexSparseMatrix_real(self, *args)
    real = _swig_new_instance_method(_complex_operator.ComplexSparseMatrix_real)

    def imag(self, *args):
        r"""
        imag(ComplexSparseMatrix self) -> SparseMatrix
        imag(ComplexSparseMatrix self) -> SparseMatrix
        """
        return _complex_operator.ComplexSparseMatrix_imag(self, *args)
    imag = _swig_new_instance_method(_complex_operator.ComplexSparseMatrix_imag)

    def GetSystemMatrix(self):
        r"""GetSystemMatrix(ComplexSparseMatrix self) -> SparseMatrix"""
        return _complex_operator.ComplexSparseMatrix_GetSystemMatrix(self)
    GetSystemMatrix = _swig_new_instance_method(_complex_operator.ComplexSparseMatrix_GetSystemMatrix)

    def GetType(self):
        r"""GetType(ComplexSparseMatrix self) -> mfem::Operator::Type"""
        return _complex_operator.ComplexSparseMatrix_GetType(self)
    GetType = _swig_new_instance_method(_complex_operator.ComplexSparseMatrix_GetType)
    __swig_destroy__ = _complex_operator.delete_ComplexSparseMatrix

# Register ComplexSparseMatrix in _complex_operator:
_complex_operator.ComplexSparseMatrix_swigregister(ComplexSparseMatrix)



