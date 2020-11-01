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
    from . import _geom
else:
    import _geom

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _geom.SWIG_PyInstanceMethod_New
_swig_new_static_method = _geom.SWIG_PyStaticMethod_New

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

import mfem._ser.intrules
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.densemat
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
class Geometry(object):
    r"""Proxy of C++ mfem::Geometry class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    INVALID = _geom.Geometry_INVALID
    
    POINT = _geom.Geometry_POINT
    
    SEGMENT = _geom.Geometry_SEGMENT
    
    TRIANGLE = _geom.Geometry_TRIANGLE
    
    SQUARE = _geom.Geometry_SQUARE
    
    TETRAHEDRON = _geom.Geometry_TETRAHEDRON
    
    CUBE = _geom.Geometry_CUBE
    
    PRISM = _geom.Geometry_PRISM
    
    NUM_GEOMETRIES = _geom.Geometry_NUM_GEOMETRIES
    
    NumGeom = _geom.Geometry_NumGeom
    
    MaxDim = _geom.Geometry_MaxDim
    
    Name = property(_geom.Geometry_Name_get, _geom.Geometry_Name_set, doc=r"""Name : a(mfem::Geometry::NumGeom).p.q(const).char""")

    def __init__(self):
        r"""__init__(Geometry self) -> Geometry"""
        _geom.Geometry_swiginit(self, _geom.new_Geometry())
    __swig_destroy__ = _geom.delete_Geometry

    def GetVertices(self, GeomType):
        r"""GetVertices(Geometry self, int GeomType) -> IntegrationRule"""
        return _geom.Geometry_GetVertices(self, GeomType)
    GetVertices = _swig_new_instance_method(_geom.Geometry_GetVertices)

    def GetCenter(self, GeomType):
        r"""GetCenter(Geometry self, int GeomType) -> IntegrationPoint"""
        return _geom.Geometry_GetCenter(self, GeomType)
    GetCenter = _swig_new_instance_method(_geom.Geometry_GetCenter)

    @staticmethod
    def GetRandomPoint(GeomType, ip):
        r"""GetRandomPoint(int GeomType, IntegrationPoint ip)"""
        return _geom.Geometry_GetRandomPoint(GeomType, ip)
    GetRandomPoint = _swig_new_static_method(_geom.Geometry_GetRandomPoint)

    @staticmethod
    def CheckPoint(*args):
        r"""
        CheckPoint(int GeomType, IntegrationPoint ip) -> bool
        CheckPoint(int GeomType, IntegrationPoint ip, double eps) -> bool
        """
        return _geom.Geometry_CheckPoint(*args)
    CheckPoint = _swig_new_static_method(_geom.Geometry_CheckPoint)

    @staticmethod
    def ProjectPoint(*args):
        r"""
        ProjectPoint(int GeomType, IntegrationPoint beg, IntegrationPoint end) -> bool
        ProjectPoint(int GeomType, IntegrationPoint ip) -> bool
        """
        return _geom.Geometry_ProjectPoint(*args)
    ProjectPoint = _swig_new_static_method(_geom.Geometry_ProjectPoint)

    def GetGeomToPerfGeomJac(self, GeomType):
        r"""GetGeomToPerfGeomJac(Geometry self, int GeomType) -> DenseMatrix"""
        return _geom.Geometry_GetGeomToPerfGeomJac(self, GeomType)
    GetGeomToPerfGeomJac = _swig_new_instance_method(_geom.Geometry_GetGeomToPerfGeomJac)

    def GetPerfGeomToGeomJac(self, GeomType):
        r"""GetPerfGeomToGeomJac(Geometry self, int GeomType) -> DenseMatrix"""
        return _geom.Geometry_GetPerfGeomToGeomJac(self, GeomType)
    GetPerfGeomToGeomJac = _swig_new_instance_method(_geom.Geometry_GetPerfGeomToGeomJac)

    def GetPerfPointMat(self, GeomType, pm):
        r"""GetPerfPointMat(Geometry self, int GeomType, DenseMatrix pm)"""
        return _geom.Geometry_GetPerfPointMat(self, GeomType, pm)
    GetPerfPointMat = _swig_new_instance_method(_geom.Geometry_GetPerfPointMat)

    def JacToPerfJac(self, GeomType, J, PJ):
        r"""JacToPerfJac(Geometry self, int GeomType, DenseMatrix J, DenseMatrix PJ)"""
        return _geom.Geometry_JacToPerfJac(self, GeomType, J, PJ)
    JacToPerfJac = _swig_new_instance_method(_geom.Geometry_JacToPerfJac)

    def NumBdr(self, GeomType):
        r"""NumBdr(Geometry self, int GeomType) -> int"""
        return _geom.Geometry_NumBdr(self, GeomType)
    NumBdr = _swig_new_instance_method(_geom.Geometry_NumBdr)

# Register Geometry in _geom:
_geom.Geometry_swigregister(Geometry)
cvar = _geom.cvar
Geometry.NumBdrArray = _geom.cvar.Geometry_NumBdrArray
Geometry.Volume = _geom.cvar.Geometry_Volume
Geometry.Dimension = _geom.cvar.Geometry_Dimension
Geometry.DimStart = _geom.cvar.Geometry_DimStart
Geometry.NumVerts = _geom.cvar.Geometry_NumVerts
Geometry.NumEdges = _geom.cvar.Geometry_NumEdges
Geometry.NumFaces = _geom.cvar.Geometry_NumFaces

def Geometry_GetRandomPoint(GeomType, ip):
    r"""Geometry_GetRandomPoint(int GeomType, IntegrationPoint ip)"""
    return _geom.Geometry_GetRandomPoint(GeomType, ip)
Geometry_GetRandomPoint = _geom.Geometry_GetRandomPoint

def Geometry_CheckPoint(*args):
    r"""
    Geometry_CheckPoint(int GeomType, IntegrationPoint ip) -> bool
    Geometry_CheckPoint(int GeomType, IntegrationPoint ip, double eps) -> bool
    """
    return _geom.Geometry_CheckPoint(*args)
Geometry_CheckPoint = _geom.Geometry_CheckPoint

def Geometry_ProjectPoint(*args):
    r"""
    Geometry_ProjectPoint(int GeomType, IntegrationPoint beg, IntegrationPoint end) -> bool
    Geometry_ProjectPoint(int GeomType, IntegrationPoint ip) -> bool
    """
    return _geom.Geometry_ProjectPoint(*args)
Geometry_ProjectPoint = _geom.Geometry_ProjectPoint

class RefinedGeometry(object):
    r"""Proxy of C++ mfem::RefinedGeometry class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Times = property(_geom.RefinedGeometry_Times_get, _geom.RefinedGeometry_Times_set, doc=r"""Times : int""")
    ETimes = property(_geom.RefinedGeometry_ETimes_get, _geom.RefinedGeometry_ETimes_set, doc=r"""ETimes : int""")
    RefPts = property(_geom.RefinedGeometry_RefPts_get, doc=r"""RefPts : mfem::IntegrationRule""")
    RefGeoms = property(_geom.RefinedGeometry_RefGeoms_get, _geom.RefinedGeometry_RefGeoms_set, doc=r"""RefGeoms : mfem::Array<(int)>""")
    RefEdges = property(_geom.RefinedGeometry_RefEdges_get, _geom.RefinedGeometry_RefEdges_set, doc=r"""RefEdges : mfem::Array<(int)>""")
    NumBdrEdges = property(_geom.RefinedGeometry_NumBdrEdges_get, _geom.RefinedGeometry_NumBdrEdges_set, doc=r"""NumBdrEdges : int""")
    Type = property(_geom.RefinedGeometry_Type_get, _geom.RefinedGeometry_Type_set, doc=r"""Type : int""")

    def __init__(self, NPts, NRefG, NRefE, NBdrE=0):
        r"""__init__(RefinedGeometry self, int NPts, int NRefG, int NRefE, int NBdrE=0) -> RefinedGeometry"""
        _geom.RefinedGeometry_swiginit(self, _geom.new_RefinedGeometry(NPts, NRefG, NRefE, NBdrE))
    __swig_destroy__ = _geom.delete_RefinedGeometry

# Register RefinedGeometry in _geom:
_geom.RefinedGeometry_swigregister(RefinedGeometry)

class GeometryRefiner(object):
    r"""Proxy of C++ mfem::GeometryRefiner class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(GeometryRefiner self) -> GeometryRefiner"""
        _geom.GeometryRefiner_swiginit(self, _geom.new_GeometryRefiner())

    def SetType(self, t):
        r"""SetType(GeometryRefiner self, int const t)"""
        return _geom.GeometryRefiner_SetType(self, t)
    SetType = _swig_new_instance_method(_geom.GeometryRefiner_SetType)

    def GetType(self):
        r"""GetType(GeometryRefiner self) -> int"""
        return _geom.GeometryRefiner_GetType(self)
    GetType = _swig_new_instance_method(_geom.GeometryRefiner_GetType)

    def Refine(self, Geom, Times, ETimes=1):
        r"""Refine(GeometryRefiner self, mfem::Geometry::Type Geom, int Times, int ETimes=1) -> RefinedGeometry"""
        return _geom.GeometryRefiner_Refine(self, Geom, Times, ETimes)
    Refine = _swig_new_instance_method(_geom.GeometryRefiner_Refine)

    def RefineInterior(self, Geom, Times):
        r"""RefineInterior(GeometryRefiner self, mfem::Geometry::Type Geom, int Times) -> IntegrationRule"""
        return _geom.GeometryRefiner_RefineInterior(self, Geom, Times)
    RefineInterior = _swig_new_instance_method(_geom.GeometryRefiner_RefineInterior)

    def GetRefinementLevelFromPoints(self, Geom, Npts):
        r"""GetRefinementLevelFromPoints(GeometryRefiner self, mfem::Geometry::Type Geom, int Npts) -> int"""
        return _geom.GeometryRefiner_GetRefinementLevelFromPoints(self, Geom, Npts)
    GetRefinementLevelFromPoints = _swig_new_instance_method(_geom.GeometryRefiner_GetRefinementLevelFromPoints)

    def GetRefinementLevelFromElems(self, geom, Npts):
        r"""GetRefinementLevelFromElems(GeometryRefiner self, mfem::Geometry::Type geom, int Npts) -> int"""
        return _geom.GeometryRefiner_GetRefinementLevelFromElems(self, geom, Npts)
    GetRefinementLevelFromElems = _swig_new_instance_method(_geom.GeometryRefiner_GetRefinementLevelFromElems)
    __swig_destroy__ = _geom.delete_GeometryRefiner

# Register GeometryRefiner in _geom:
_geom.GeometryRefiner_swigregister(GeometryRefiner)


GlobGeometryRefiner = cvar.GlobGeometryRefiner

