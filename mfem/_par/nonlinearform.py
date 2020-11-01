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
    from . import _nonlinearform
else:
    import _nonlinearform

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _nonlinearform.SWIG_PyInstanceMethod_New
_swig_new_static_method = _nonlinearform.SWIG_PyStaticMethod_New

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

import mfem._par.operators
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.array
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.matrix
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilinearform
import mfem._par.nonlininteg
class NonlinearForm(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::NonlinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, f):
        r"""__init__(NonlinearForm self, FiniteElementSpace f) -> NonlinearForm"""
        _nonlinearform.NonlinearForm_swiginit(self, _nonlinearform.new_NonlinearForm(f))

    def SetAssemblyLevel(self, assembly_level):
        r"""SetAssemblyLevel(NonlinearForm self, mfem::AssemblyLevel assembly_level)"""
        return _nonlinearform.NonlinearForm_SetAssemblyLevel(self, assembly_level)
    SetAssemblyLevel = _swig_new_instance_method(_nonlinearform.NonlinearForm_SetAssemblyLevel)

    def FESpace(self, *args):
        r"""
        FESpace(NonlinearForm self) -> FiniteElementSpace
        FESpace(NonlinearForm self) -> FiniteElementSpace
        """
        return _nonlinearform.NonlinearForm_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_nonlinearform.NonlinearForm_FESpace)

    def AddDomainIntegrator(self, nlfi):
        r"""AddDomainIntegrator(NonlinearForm self, NonlinearFormIntegrator nlfi)"""

        #    if not hasattr(self, "_integrators"): self._integrators = []
        #    self._integrators.append(nlfi)
        nlfi.thisown=0 


        return _nonlinearform.NonlinearForm_AddDomainIntegrator(self, nlfi)


    def GetDNFI(self, *args):
        r"""
        GetDNFI(NonlinearForm self) -> mfem::Array< mfem::NonlinearFormIntegrator * >
        GetDNFI(NonlinearForm self) -> mfem::Array< mfem::NonlinearFormIntegrator * > const *
        """
        return _nonlinearform.NonlinearForm_GetDNFI(self, *args)
    GetDNFI = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetDNFI)

    def AddInteriorFaceIntegrator(self, nlfi):
        r"""AddInteriorFaceIntegrator(NonlinearForm self, NonlinearFormIntegrator nlfi)"""

        #    if not hasattr(self, "_integrators"): self._integrators = []
        #    self._integrators.append(nlfi)
        nlfi.thisown=0 


        return _nonlinearform.NonlinearForm_AddInteriorFaceIntegrator(self, nlfi)


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(NonlinearForm self, NonlinearFormIntegrator nlfi)
        AddBdrFaceIntegrator(NonlinearForm self, NonlinearFormIntegrator nfi, intArray bdr_marker)
        """

        #    if not hasattr(self, "_integrators"): self._integrators = []
        #    self._integrators.append(nlfi)
        nlfi = args[0]
        nlfi.thisown=0 


        return _nonlinearform.NonlinearForm_AddBdrFaceIntegrator(self, *args)


    def SetEssentialBC(self, bdr_attr_is_ess, rhs=None):
        r"""SetEssentialBC(NonlinearForm self, intArray bdr_attr_is_ess, Vector rhs=None)"""
        return _nonlinearform.NonlinearForm_SetEssentialBC(self, bdr_attr_is_ess, rhs)
    SetEssentialBC = _swig_new_instance_method(_nonlinearform.NonlinearForm_SetEssentialBC)

    def SetEssentialVDofs(self, ess_vdofs_list):
        r"""SetEssentialVDofs(NonlinearForm self, intArray ess_vdofs_list)"""
        return _nonlinearform.NonlinearForm_SetEssentialVDofs(self, ess_vdofs_list)
    SetEssentialVDofs = _swig_new_instance_method(_nonlinearform.NonlinearForm_SetEssentialVDofs)

    def SetEssentialTrueDofs(self, ess_tdof_list):
        r"""SetEssentialTrueDofs(NonlinearForm self, intArray ess_tdof_list)"""
        return _nonlinearform.NonlinearForm_SetEssentialTrueDofs(self, ess_tdof_list)
    SetEssentialTrueDofs = _swig_new_instance_method(_nonlinearform.NonlinearForm_SetEssentialTrueDofs)

    def GetEssentialTrueDofs(self):
        r"""GetEssentialTrueDofs(NonlinearForm self) -> intArray"""
        return _nonlinearform.NonlinearForm_GetEssentialTrueDofs(self)
    GetEssentialTrueDofs = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetEssentialTrueDofs)

    def GetGridFunctionEnergy(self, x):
        r"""GetGridFunctionEnergy(NonlinearForm self, Vector x) -> double"""
        return _nonlinearform.NonlinearForm_GetGridFunctionEnergy(self, x)
    GetGridFunctionEnergy = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetGridFunctionEnergy)

    def GetEnergy(self, x):
        r"""GetEnergy(NonlinearForm self, Vector x) -> double"""
        return _nonlinearform.NonlinearForm_GetEnergy(self, x)
    GetEnergy = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetEnergy)

    def Mult(self, x, y):
        r"""Mult(NonlinearForm self, Vector x, Vector y)"""
        return _nonlinearform.NonlinearForm_Mult(self, x, y)
    Mult = _swig_new_instance_method(_nonlinearform.NonlinearForm_Mult)

    def GetGradient(self, x):
        r"""GetGradient(NonlinearForm self, Vector x) -> Operator"""
        return _nonlinearform.NonlinearForm_GetGradient(self, x)
    GetGradient = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetGradient)

    def Update(self):
        r"""Update(NonlinearForm self)"""
        return _nonlinearform.NonlinearForm_Update(self)
    Update = _swig_new_instance_method(_nonlinearform.NonlinearForm_Update)

    def Setup(self):
        r"""Setup(NonlinearForm self)"""
        return _nonlinearform.NonlinearForm_Setup(self)
    Setup = _swig_new_instance_method(_nonlinearform.NonlinearForm_Setup)

    def GetProlongation(self):
        r"""GetProlongation(NonlinearForm self) -> Operator"""
        return _nonlinearform.NonlinearForm_GetProlongation(self)
    GetProlongation = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetProlongation)

    def GetRestriction(self):
        r"""GetRestriction(NonlinearForm self) -> Operator"""
        return _nonlinearform.NonlinearForm_GetRestriction(self)
    GetRestriction = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetRestriction)
    __swig_destroy__ = _nonlinearform.delete_NonlinearForm

    def GetGradientMatrix(self, x):
        r"""GetGradientMatrix(NonlinearForm self, Vector x) -> SparseMatrix"""
        return _nonlinearform.NonlinearForm_GetGradientMatrix(self, x)
    GetGradientMatrix = _swig_new_instance_method(_nonlinearform.NonlinearForm_GetGradientMatrix)

# Register NonlinearForm in _nonlinearform:
_nonlinearform.NonlinearForm_swigregister(NonlinearForm)

class BlockNonlinearForm(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::BlockNonlinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(BlockNonlinearForm self) -> BlockNonlinearForm
        __init__(BlockNonlinearForm self, mfem::Array< mfem::FiniteElementSpace * > & f) -> BlockNonlinearForm
        """
        _nonlinearform.BlockNonlinearForm_swiginit(self, _nonlinearform.new_BlockNonlinearForm(*args))

    def FESpace(self, *args):
        r"""
        FESpace(BlockNonlinearForm self, int k) -> FiniteElementSpace
        FESpace(BlockNonlinearForm self, int k) -> FiniteElementSpace
        """
        return _nonlinearform.BlockNonlinearForm_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_FESpace)

    def SetSpaces(self, f):
        r"""SetSpaces(BlockNonlinearForm self, mfem::Array< mfem::FiniteElementSpace * > & f)"""
        return _nonlinearform.BlockNonlinearForm_SetSpaces(self, f)
    SetSpaces = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_SetSpaces)

    def GetBlockOffsets(self):
        r"""GetBlockOffsets(BlockNonlinearForm self) -> intArray"""
        return _nonlinearform.BlockNonlinearForm_GetBlockOffsets(self)
    GetBlockOffsets = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_GetBlockOffsets)

    def GetBlockTrueOffsets(self):
        r"""GetBlockTrueOffsets(BlockNonlinearForm self) -> intArray"""
        return _nonlinearform.BlockNonlinearForm_GetBlockTrueOffsets(self)
    GetBlockTrueOffsets = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_GetBlockTrueOffsets)

    def AddDomainIntegrator(self, nlfi):
        r"""AddDomainIntegrator(BlockNonlinearForm self, BlockNonlinearFormIntegrator nlfi)"""

        #    if not hasattr(self, "_integrators"): self._integrators = []
        #    self._integrators.append(nlfi)
        nlfi.thisown=0 


        return _nonlinearform.BlockNonlinearForm_AddDomainIntegrator(self, nlfi)


    def AddInteriorFaceIntegrator(self, nlfi):
        r"""AddInteriorFaceIntegrator(BlockNonlinearForm self, BlockNonlinearFormIntegrator nlfi)"""

        #    if not hasattr(self, "_integrators"): self._integrators = []
        #    self._integrators.append(nlfi)
        nlfi.thisown=0 


        return _nonlinearform.BlockNonlinearForm_AddInteriorFaceIntegrator(self, nlfi)


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(BlockNonlinearForm self, BlockNonlinearFormIntegrator nlfi)
        AddBdrFaceIntegrator(BlockNonlinearForm self, BlockNonlinearFormIntegrator nlfi, intArray bdr_marker)
        """

        #    if not hasattr(self, "_integrators"): self._integrators = []
        #    self._integrators.append(nlfi)
        nlfi = args[0]
        nlfi.thisown=0 


        return _nonlinearform.BlockNonlinearForm_AddBdrFaceIntegrator(self, *args)


    def SetEssentialBC(self, bdr_attr_is_ess, rhs):
        r"""SetEssentialBC(BlockNonlinearForm self, mfem::Array< mfem::Array< int > * > const & bdr_attr_is_ess, mfem::Array< mfem::Vector * > & rhs)"""
        return _nonlinearform.BlockNonlinearForm_SetEssentialBC(self, bdr_attr_is_ess, rhs)
    SetEssentialBC = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_SetEssentialBC)

    def GetEnergy(self, x):
        r"""GetEnergy(BlockNonlinearForm self, Vector x) -> double"""
        return _nonlinearform.BlockNonlinearForm_GetEnergy(self, x)
    GetEnergy = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_GetEnergy)

    def Mult(self, x, y):
        r"""Mult(BlockNonlinearForm self, Vector x, Vector y)"""
        return _nonlinearform.BlockNonlinearForm_Mult(self, x, y)
    Mult = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_Mult)

    def GetGradient(self, x):
        r"""GetGradient(BlockNonlinearForm self, Vector x) -> Operator"""
        return _nonlinearform.BlockNonlinearForm_GetGradient(self, x)
    GetGradient = _swig_new_instance_method(_nonlinearform.BlockNonlinearForm_GetGradient)
    __swig_destroy__ = _nonlinearform.delete_BlockNonlinearForm

# Register BlockNonlinearForm in _nonlinearform:
_nonlinearform.BlockNonlinearForm_swigregister(BlockNonlinearForm)



