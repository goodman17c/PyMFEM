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
    from . import _tmop_amr
else:
    import _tmop_amr

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _tmop_amr.SWIG_PyInstanceMethod_New
_swig_new_static_method = _tmop_amr.SWIG_PyStaticMethod_New

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

MFEM_VERSION = _tmop_amr.MFEM_VERSION
MFEM_VERSION_STRING = _tmop_amr.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _tmop_amr.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _tmop_amr.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _tmop_amr.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _tmop_amr.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _tmop_amr.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _tmop_amr.MFEM_VERSION_PATCH
import mfem._ser.tmop
import mfem._ser.intrules
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.gridfunc
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.symmat
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.fe_base
import mfem._ser.fe_fixed_order
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.fe_h1
import mfem._ser.fe_nd
import mfem._ser.fe_rt
import mfem._ser.fe_l2
import mfem._ser.fe_nurbs
import mfem._ser.fe_pos
import mfem._ser.fe_ser
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.std_vectors
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.nonlinearform
import mfem._ser.bilinearform
import mfem._ser.estimators
class TMOPRefinerEstimator(mfem._ser.estimators.AnisotropicErrorEstimator):
    r"""Proxy of C++ mfem::TMOPRefinerEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, mesh_, nlf_, order_, amrmetric_):
        r"""__init__(TMOPRefinerEstimator self, Mesh mesh_, NonlinearForm nlf_, int order_, int amrmetric_) -> TMOPRefinerEstimator"""
        _tmop_amr.TMOPRefinerEstimator_swiginit(self, _tmop_amr.new_TMOPRefinerEstimator(mesh_, nlf_, order_, amrmetric_))
    __swig_destroy__ = _tmop_amr.delete_TMOPRefinerEstimator

    def GetLocalErrors(self):
        r"""GetLocalErrors(TMOPRefinerEstimator self) -> Vector"""
        return _tmop_amr.TMOPRefinerEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_tmop_amr.TMOPRefinerEstimator_GetLocalErrors)

    def GetAnisotropicFlags(self):
        r"""GetAnisotropicFlags(TMOPRefinerEstimator self) -> intArray"""
        return _tmop_amr.TMOPRefinerEstimator_GetAnisotropicFlags(self)
    GetAnisotropicFlags = _swig_new_instance_method(_tmop_amr.TMOPRefinerEstimator_GetAnisotropicFlags)

    def SetEnergyScalingFactor(self, scale):
        r"""SetEnergyScalingFactor(TMOPRefinerEstimator self, double scale)"""
        return _tmop_amr.TMOPRefinerEstimator_SetEnergyScalingFactor(self, scale)
    SetEnergyScalingFactor = _swig_new_instance_method(_tmop_amr.TMOPRefinerEstimator_SetEnergyScalingFactor)

    def SetSpatialIndicator(self, spat_gf_, spat_gf_critical_=0.5):
        r"""SetSpatialIndicator(TMOPRefinerEstimator self, GridFunction spat_gf_, double spat_gf_critical_=0.5)"""
        return _tmop_amr.TMOPRefinerEstimator_SetSpatialIndicator(self, spat_gf_, spat_gf_critical_)
    SetSpatialIndicator = _swig_new_instance_method(_tmop_amr.TMOPRefinerEstimator_SetSpatialIndicator)

    def SetSpatialIndicatorCritical(self, val_):
        r"""SetSpatialIndicatorCritical(TMOPRefinerEstimator self, double val_)"""
        return _tmop_amr.TMOPRefinerEstimator_SetSpatialIndicatorCritical(self, val_)
    SetSpatialIndicatorCritical = _swig_new_instance_method(_tmop_amr.TMOPRefinerEstimator_SetSpatialIndicatorCritical)

    def Reset(self):
        r"""Reset(TMOPRefinerEstimator self)"""
        return _tmop_amr.TMOPRefinerEstimator_Reset(self)
    Reset = _swig_new_instance_method(_tmop_amr.TMOPRefinerEstimator_Reset)

# Register TMOPRefinerEstimator in _tmop_amr:
_tmop_amr.TMOPRefinerEstimator_swigregister(TMOPRefinerEstimator)

class TMOPDeRefinerEstimator(mfem._ser.estimators.ErrorEstimator):
    r"""Proxy of C++ mfem::TMOPDeRefinerEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, mesh_, nlf_):
        r"""__init__(TMOPDeRefinerEstimator self, Mesh mesh_, NonlinearForm nlf_) -> TMOPDeRefinerEstimator"""
        _tmop_amr.TMOPDeRefinerEstimator_swiginit(self, _tmop_amr.new_TMOPDeRefinerEstimator(mesh_, nlf_))
    __swig_destroy__ = _tmop_amr.delete_TMOPDeRefinerEstimator

    def GetLocalErrors(self):
        r"""GetLocalErrors(TMOPDeRefinerEstimator self) -> Vector"""
        return _tmop_amr.TMOPDeRefinerEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_tmop_amr.TMOPDeRefinerEstimator_GetLocalErrors)

    def Reset(self):
        r"""Reset(TMOPDeRefinerEstimator self)"""
        return _tmop_amr.TMOPDeRefinerEstimator_Reset(self)
    Reset = _swig_new_instance_method(_tmop_amr.TMOPDeRefinerEstimator_Reset)

# Register TMOPDeRefinerEstimator in _tmop_amr:
_tmop_amr.TMOPDeRefinerEstimator_swigregister(TMOPDeRefinerEstimator)

class TMOPHRSolver(object):
    r"""Proxy of C++ mfem::TMOPHRSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, mesh_, nlf_, tmopns_, x_, move_bnd_, hradaptivity_, mesh_poly_deg_, amr_metric_id_, hr_iter_=5, h_per_r_iter_=1):
        r"""__init__(TMOPHRSolver self, Mesh mesh_, NonlinearForm nlf_, mfem::TMOPNewtonSolver & tmopns_, GridFunction x_, bool move_bnd_, bool hradaptivity_, int mesh_poly_deg_, int amr_metric_id_, int hr_iter_=5, int h_per_r_iter_=1) -> TMOPHRSolver"""
        _tmop_amr.TMOPHRSolver_swiginit(self, _tmop_amr.new_TMOPHRSolver(mesh_, nlf_, tmopns_, x_, move_bnd_, hradaptivity_, mesh_poly_deg_, amr_metric_id_, hr_iter_, h_per_r_iter_))

    def Mult(self):
        r"""Mult(TMOPHRSolver self)"""
        return _tmop_amr.TMOPHRSolver_Mult(self)
    Mult = _swig_new_instance_method(_tmop_amr.TMOPHRSolver_Mult)

    def AddGridFunctionForUpdate(self, gf):
        r"""AddGridFunctionForUpdate(TMOPHRSolver self, GridFunction gf)"""
        return _tmop_amr.TMOPHRSolver_AddGridFunctionForUpdate(self, gf)
    AddGridFunctionForUpdate = _swig_new_instance_method(_tmop_amr.TMOPHRSolver_AddGridFunctionForUpdate)

    def AddFESpaceForUpdate(self, fes):
        r"""AddFESpaceForUpdate(TMOPHRSolver self, FiniteElementSpace fes)"""
        return _tmop_amr.TMOPHRSolver_AddFESpaceForUpdate(self, fes)
    AddFESpaceForUpdate = _swig_new_instance_method(_tmop_amr.TMOPHRSolver_AddFESpaceForUpdate)
    __swig_destroy__ = _tmop_amr.delete_TMOPHRSolver

    def SetHRAdaptivityIterations(self, iter):
        r"""SetHRAdaptivityIterations(TMOPHRSolver self, int iter)"""
        return _tmop_amr.TMOPHRSolver_SetHRAdaptivityIterations(self, iter)
    SetHRAdaptivityIterations = _swig_new_instance_method(_tmop_amr.TMOPHRSolver_SetHRAdaptivityIterations)

    def SetHAdaptivityIterations(self, iter):
        r"""SetHAdaptivityIterations(TMOPHRSolver self, int iter)"""
        return _tmop_amr.TMOPHRSolver_SetHAdaptivityIterations(self, iter)
    SetHAdaptivityIterations = _swig_new_instance_method(_tmop_amr.TMOPHRSolver_SetHAdaptivityIterations)

# Register TMOPHRSolver in _tmop_amr:
_tmop_amr.TMOPHRSolver_swigregister(TMOPHRSolver)



