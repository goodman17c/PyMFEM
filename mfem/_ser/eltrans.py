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
    from . import _eltrans
else:
    import _eltrans

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _eltrans.SWIG_PyInstanceMethod_New
_swig_new_static_method = _eltrans.SWIG_PyStaticMethod_New

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

class OutStream(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, out):
        _eltrans.OutStream_swiginit(self, _eltrans.new_OutStream(out))

    def SetStream(self, out):
        return _eltrans.OutStream_SetStream(self, out)
    SetStream = _swig_new_instance_method(_eltrans.OutStream_SetStream)

    def Enable(self):
        return _eltrans.OutStream_Enable(self)
    Enable = _swig_new_instance_method(_eltrans.OutStream_Enable)

    def Disable(self):
        return _eltrans.OutStream_Disable(self)
    Disable = _swig_new_instance_method(_eltrans.OutStream_Disable)

    def IsEnabled(self):
        return _eltrans.OutStream_IsEnabled(self)
    IsEnabled = _swig_new_instance_method(_eltrans.OutStream_IsEnabled)
    __swig_destroy__ = _eltrans.delete_OutStream

# Register OutStream in _eltrans:
_eltrans.OutStream_swigregister(OutStream)


def MakeParFilename(*args, **kwargs):
    return _eltrans.MakeParFilename(*args, **kwargs)
MakeParFilename = _eltrans.MakeParFilename
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.densemat
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.intrules
import mfem._ser.sparsemat
class ElementTransformation(object):
    r"""Proxy of C++ mfem::ElementTransformation class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    ELEMENT = _eltrans.ElementTransformation_ELEMENT
    
    BDR_ELEMENT = _eltrans.ElementTransformation_BDR_ELEMENT
    
    EDGE = _eltrans.ElementTransformation_EDGE
    
    FACE = _eltrans.ElementTransformation_FACE
    
    BDR_FACE = _eltrans.ElementTransformation_BDR_FACE
    
    Attribute = property(_eltrans.ElementTransformation_Attribute_get, _eltrans.ElementTransformation_Attribute_set, doc=r"""Attribute : int""")
    ElementNo = property(_eltrans.ElementTransformation_ElementNo_get, _eltrans.ElementTransformation_ElementNo_set, doc=r"""ElementNo : int""")
    ElementType = property(_eltrans.ElementTransformation_ElementType_get, _eltrans.ElementTransformation_ElementType_set, doc=r"""ElementType : int""")

    def Reset(self):
        r"""Reset(ElementTransformation self)"""
        return _eltrans.ElementTransformation_Reset(self)
    Reset = _swig_new_instance_method(_eltrans.ElementTransformation_Reset)

    def SetIntPoint(self, ip):
        r"""SetIntPoint(ElementTransformation self, IntegrationPoint ip)"""
        return _eltrans.ElementTransformation_SetIntPoint(self, ip)
    SetIntPoint = _swig_new_instance_method(_eltrans.ElementTransformation_SetIntPoint)

    def GetIntPoint(self):
        r"""GetIntPoint(ElementTransformation self) -> IntegrationPoint"""
        return _eltrans.ElementTransformation_GetIntPoint(self)
    GetIntPoint = _swig_new_instance_method(_eltrans.ElementTransformation_GetIntPoint)

    def Transform(self, *args):
        from .vector import Vector
        from .intrules import IntegrationPoint
        if isinstance(args[0], IntegrationPoint):
            vec = Vector()
            _eltrans.ElementTransformation_Transform(self, args[0], vec)
            ret = vec.GetDataArray().copy()
            return ret
        else:
            return _eltrans.ElementTransformation_Transform(self, *args)



    def Jacobian(self):
        r"""Jacobian(ElementTransformation self) -> DenseMatrix"""
        return _eltrans.ElementTransformation_Jacobian(self)
    Jacobian = _swig_new_instance_method(_eltrans.ElementTransformation_Jacobian)

    def Hessian(self):
        r"""Hessian(ElementTransformation self) -> DenseMatrix"""
        return _eltrans.ElementTransformation_Hessian(self)
    Hessian = _swig_new_instance_method(_eltrans.ElementTransformation_Hessian)

    def Weight(self):
        r"""Weight(ElementTransformation self) -> double"""
        return _eltrans.ElementTransformation_Weight(self)
    Weight = _swig_new_instance_method(_eltrans.ElementTransformation_Weight)

    def AdjugateJacobian(self):
        r"""AdjugateJacobian(ElementTransformation self) -> DenseMatrix"""
        return _eltrans.ElementTransformation_AdjugateJacobian(self)
    AdjugateJacobian = _swig_new_instance_method(_eltrans.ElementTransformation_AdjugateJacobian)

    def InverseJacobian(self):
        r"""InverseJacobian(ElementTransformation self) -> DenseMatrix"""
        return _eltrans.ElementTransformation_InverseJacobian(self)
    InverseJacobian = _swig_new_instance_method(_eltrans.ElementTransformation_InverseJacobian)

    def Order(self):
        r"""Order(ElementTransformation self) -> int"""
        return _eltrans.ElementTransformation_Order(self)
    Order = _swig_new_instance_method(_eltrans.ElementTransformation_Order)

    def OrderJ(self):
        r"""OrderJ(ElementTransformation self) -> int"""
        return _eltrans.ElementTransformation_OrderJ(self)
    OrderJ = _swig_new_instance_method(_eltrans.ElementTransformation_OrderJ)

    def OrderW(self):
        r"""OrderW(ElementTransformation self) -> int"""
        return _eltrans.ElementTransformation_OrderW(self)
    OrderW = _swig_new_instance_method(_eltrans.ElementTransformation_OrderW)

    def OrderGrad(self, fe):
        r"""OrderGrad(ElementTransformation self, FiniteElement fe) -> int"""
        return _eltrans.ElementTransformation_OrderGrad(self, fe)
    OrderGrad = _swig_new_instance_method(_eltrans.ElementTransformation_OrderGrad)

    def GetGeometryType(self):
        r"""GetGeometryType(ElementTransformation self) -> mfem::Geometry::Type"""
        return _eltrans.ElementTransformation_GetGeometryType(self)
    GetGeometryType = _swig_new_instance_method(_eltrans.ElementTransformation_GetGeometryType)

    def GetDimension(self):
        r"""GetDimension(ElementTransformation self) -> int"""
        return _eltrans.ElementTransformation_GetDimension(self)
    GetDimension = _swig_new_instance_method(_eltrans.ElementTransformation_GetDimension)

    def GetSpaceDim(self):
        r"""GetSpaceDim(ElementTransformation self) -> int"""
        return _eltrans.ElementTransformation_GetSpaceDim(self)
    GetSpaceDim = _swig_new_instance_method(_eltrans.ElementTransformation_GetSpaceDim)

    def TransformBack(self, pt, ip):
        r"""TransformBack(ElementTransformation self, Vector pt, IntegrationPoint ip) -> int"""
        return _eltrans.ElementTransformation_TransformBack(self, pt, ip)
    TransformBack = _swig_new_instance_method(_eltrans.ElementTransformation_TransformBack)
    __swig_destroy__ = _eltrans.delete_ElementTransformation

# Register ElementTransformation in _eltrans:
_eltrans.ElementTransformation_swigregister(ElementTransformation)
cvar = _eltrans.cvar
out = cvar.out
err = cvar.err

class InverseElementTransformation(object):
    r"""Proxy of C++ mfem::InverseElementTransformation class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Center = _eltrans.InverseElementTransformation_Center
    
    ClosestPhysNode = _eltrans.InverseElementTransformation_ClosestPhysNode
    
    ClosestRefNode = _eltrans.InverseElementTransformation_ClosestRefNode
    
    GivenPoint = _eltrans.InverseElementTransformation_GivenPoint
    
    Newton = _eltrans.InverseElementTransformation_Newton
    
    NewtonSegmentProject = _eltrans.InverseElementTransformation_NewtonSegmentProject
    
    NewtonElementProject = _eltrans.InverseElementTransformation_NewtonElementProject
    
    Inside = _eltrans.InverseElementTransformation_Inside
    
    Outside = _eltrans.InverseElementTransformation_Outside
    
    Unknown = _eltrans.InverseElementTransformation_Unknown
    

    def __init__(self, Trans=None):
        r"""__init__(InverseElementTransformation self, ElementTransformation Trans=None) -> InverseElementTransformation"""
        _eltrans.InverseElementTransformation_swiginit(self, _eltrans.new_InverseElementTransformation(Trans))
    __swig_destroy__ = _eltrans.delete_InverseElementTransformation

    def SetTransformation(self, Trans):
        r"""SetTransformation(InverseElementTransformation self, ElementTransformation Trans)"""
        return _eltrans.InverseElementTransformation_SetTransformation(self, Trans)
    SetTransformation = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetTransformation)

    def SetInitialGuessType(self, itype):
        r"""SetInitialGuessType(InverseElementTransformation self, mfem::InverseElementTransformation::InitGuessType itype)"""
        return _eltrans.InverseElementTransformation_SetInitialGuessType(self, itype)
    SetInitialGuessType = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetInitialGuessType)

    def SetInitialGuess(self, init_ip):
        r"""SetInitialGuess(InverseElementTransformation self, IntegrationPoint init_ip)"""
        return _eltrans.InverseElementTransformation_SetInitialGuess(self, init_ip)
    SetInitialGuess = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetInitialGuess)

    def SetInitGuessPointsType(self, q_type):
        r"""SetInitGuessPointsType(InverseElementTransformation self, int q_type)"""
        return _eltrans.InverseElementTransformation_SetInitGuessPointsType(self, q_type)
    SetInitGuessPointsType = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetInitGuessPointsType)

    def SetInitGuessRelOrder(self, order):
        r"""SetInitGuessRelOrder(InverseElementTransformation self, int order)"""
        return _eltrans.InverseElementTransformation_SetInitGuessRelOrder(self, order)
    SetInitGuessRelOrder = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetInitGuessRelOrder)

    def SetSolverType(self, stype):
        r"""SetSolverType(InverseElementTransformation self, mfem::InverseElementTransformation::SolverType stype)"""
        return _eltrans.InverseElementTransformation_SetSolverType(self, stype)
    SetSolverType = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetSolverType)

    def SetMaxIter(self, max_it):
        r"""SetMaxIter(InverseElementTransformation self, int max_it)"""
        return _eltrans.InverseElementTransformation_SetMaxIter(self, max_it)
    SetMaxIter = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetMaxIter)

    def SetReferenceTol(self, ref_sp_tol):
        r"""SetReferenceTol(InverseElementTransformation self, double ref_sp_tol)"""
        return _eltrans.InverseElementTransformation_SetReferenceTol(self, ref_sp_tol)
    SetReferenceTol = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetReferenceTol)

    def SetPhysicalRelTol(self, phys_rel_tol):
        r"""SetPhysicalRelTol(InverseElementTransformation self, double phys_rel_tol)"""
        return _eltrans.InverseElementTransformation_SetPhysicalRelTol(self, phys_rel_tol)
    SetPhysicalRelTol = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetPhysicalRelTol)

    def SetElementTol(self, el_tol):
        r"""SetElementTol(InverseElementTransformation self, double el_tol)"""
        return _eltrans.InverseElementTransformation_SetElementTol(self, el_tol)
    SetElementTol = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetElementTol)

    def SetPrintLevel(self, pr_level):
        r"""SetPrintLevel(InverseElementTransformation self, int pr_level)"""
        return _eltrans.InverseElementTransformation_SetPrintLevel(self, pr_level)
    SetPrintLevel = _swig_new_instance_method(_eltrans.InverseElementTransformation_SetPrintLevel)

    def FindClosestPhysPoint(self, pt, ir):
        r"""FindClosestPhysPoint(InverseElementTransformation self, Vector pt, IntegrationRule ir) -> int"""
        return _eltrans.InverseElementTransformation_FindClosestPhysPoint(self, pt, ir)
    FindClosestPhysPoint = _swig_new_instance_method(_eltrans.InverseElementTransformation_FindClosestPhysPoint)

    def FindClosestRefPoint(self, pt, ir):
        r"""FindClosestRefPoint(InverseElementTransformation self, Vector pt, IntegrationRule ir) -> int"""
        return _eltrans.InverseElementTransformation_FindClosestRefPoint(self, pt, ir)
    FindClosestRefPoint = _swig_new_instance_method(_eltrans.InverseElementTransformation_FindClosestRefPoint)

    def Transform(self, pt, ip):
        r"""Transform(InverseElementTransformation self, Vector pt, IntegrationPoint ip) -> int"""
        return _eltrans.InverseElementTransformation_Transform(self, pt, ip)
    Transform = _swig_new_instance_method(_eltrans.InverseElementTransformation_Transform)

# Register InverseElementTransformation in _eltrans:
_eltrans.InverseElementTransformation_swigregister(InverseElementTransformation)

class IsoparametricTransformation(ElementTransformation):
    r"""Proxy of C++ mfem::IsoparametricTransformation class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(IsoparametricTransformation self) -> IsoparametricTransformation"""
        _eltrans.IsoparametricTransformation_swiginit(self, _eltrans.new_IsoparametricTransformation())

    def SetFE(self, FE):
        r"""SetFE(IsoparametricTransformation self, FiniteElement FE)"""
        return _eltrans.IsoparametricTransformation_SetFE(self, FE)
    SetFE = _swig_new_instance_method(_eltrans.IsoparametricTransformation_SetFE)

    def GetFE(self):
        r"""GetFE(IsoparametricTransformation self) -> FiniteElement"""
        return _eltrans.IsoparametricTransformation_GetFE(self)
    GetFE = _swig_new_instance_method(_eltrans.IsoparametricTransformation_GetFE)

    def SetPointMat(self, pm):
        r"""SetPointMat(IsoparametricTransformation self, DenseMatrix pm)"""
        return _eltrans.IsoparametricTransformation_SetPointMat(self, pm)
    SetPointMat = _swig_new_instance_method(_eltrans.IsoparametricTransformation_SetPointMat)

    def GetPointMat(self, *args):
        r"""
        GetPointMat(IsoparametricTransformation self) -> DenseMatrix
        GetPointMat(IsoparametricTransformation self) -> DenseMatrix
        """
        return _eltrans.IsoparametricTransformation_GetPointMat(self, *args)
    GetPointMat = _swig_new_instance_method(_eltrans.IsoparametricTransformation_GetPointMat)

    def SetIdentityTransformation(self, GeomType):
        r"""SetIdentityTransformation(IsoparametricTransformation self, mfem::Geometry::Type GeomType)"""
        return _eltrans.IsoparametricTransformation_SetIdentityTransformation(self, GeomType)
    SetIdentityTransformation = _swig_new_instance_method(_eltrans.IsoparametricTransformation_SetIdentityTransformation)

    def Transform(self, *args):
        from .vector import Vector
        from .intrules import IntegrationPoint
        if isinstance(args[0], IntegrationPoint):
            vec = Vector()
            _eltrans.ElementTransformation_Transform(self, args[0], vec)
            ret = vec.GetDataArray().copy()
            return ret
        else:
            return _eltrans.ElementTransformation_Transform(self, *args)



    def Order(self):
        r"""Order(IsoparametricTransformation self) -> int"""
        return _eltrans.IsoparametricTransformation_Order(self)
    Order = _swig_new_instance_method(_eltrans.IsoparametricTransformation_Order)

    def OrderJ(self):
        r"""OrderJ(IsoparametricTransformation self) -> int"""
        return _eltrans.IsoparametricTransformation_OrderJ(self)
    OrderJ = _swig_new_instance_method(_eltrans.IsoparametricTransformation_OrderJ)

    def OrderW(self):
        r"""OrderW(IsoparametricTransformation self) -> int"""
        return _eltrans.IsoparametricTransformation_OrderW(self)
    OrderW = _swig_new_instance_method(_eltrans.IsoparametricTransformation_OrderW)

    def OrderGrad(self, fe):
        r"""OrderGrad(IsoparametricTransformation self, FiniteElement fe) -> int"""
        return _eltrans.IsoparametricTransformation_OrderGrad(self, fe)
    OrderGrad = _swig_new_instance_method(_eltrans.IsoparametricTransformation_OrderGrad)

    def GetSpaceDim(self):
        r"""GetSpaceDim(IsoparametricTransformation self) -> int"""
        return _eltrans.IsoparametricTransformation_GetSpaceDim(self)
    GetSpaceDim = _swig_new_instance_method(_eltrans.IsoparametricTransformation_GetSpaceDim)

    def TransformBack(self, v, ip):
        r"""TransformBack(IsoparametricTransformation self, Vector v, IntegrationPoint ip) -> int"""
        return _eltrans.IsoparametricTransformation_TransformBack(self, v, ip)
    TransformBack = _swig_new_instance_method(_eltrans.IsoparametricTransformation_TransformBack)
    __swig_destroy__ = _eltrans.delete_IsoparametricTransformation

    def FinalizeTransformation(self):
        r"""FinalizeTransformation(IsoparametricTransformation self)"""
        return _eltrans.IsoparametricTransformation_FinalizeTransformation(self)
    FinalizeTransformation = _swig_new_instance_method(_eltrans.IsoparametricTransformation_FinalizeTransformation)

# Register IsoparametricTransformation in _eltrans:
_eltrans.IsoparametricTransformation_swigregister(IsoparametricTransformation)

class IntegrationPointTransformation(object):
    r"""Proxy of C++ mfem::IntegrationPointTransformation class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Transf = property(_eltrans.IntegrationPointTransformation_Transf_get, _eltrans.IntegrationPointTransformation_Transf_set, doc=r"""Transf : mfem::IsoparametricTransformation""")

    def Transform(self, *args):
        r"""
        Transform(IntegrationPointTransformation self, IntegrationPoint arg2, IntegrationPoint arg3)
        Transform(IntegrationPointTransformation self, IntegrationRule arg2, IntegrationRule arg3)
        """
        return _eltrans.IntegrationPointTransformation_Transform(self, *args)
    Transform = _swig_new_instance_method(_eltrans.IntegrationPointTransformation_Transform)

    def __init__(self):
        r"""__init__(IntegrationPointTransformation self) -> IntegrationPointTransformation"""
        _eltrans.IntegrationPointTransformation_swiginit(self, _eltrans.new_IntegrationPointTransformation())
    __swig_destroy__ = _eltrans.delete_IntegrationPointTransformation

# Register IntegrationPointTransformation in _eltrans:
_eltrans.IntegrationPointTransformation_swigregister(IntegrationPointTransformation)

class FaceElementTransformations(IsoparametricTransformation):
    r"""Proxy of C++ mfem::FaceElementTransformations class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    HAVE_ELEM1 = _eltrans.FaceElementTransformations_HAVE_ELEM1
    
    HAVE_ELEM2 = _eltrans.FaceElementTransformations_HAVE_ELEM2
    
    HAVE_LOC1 = _eltrans.FaceElementTransformations_HAVE_LOC1
    
    HAVE_LOC2 = _eltrans.FaceElementTransformations_HAVE_LOC2
    
    HAVE_FACE = _eltrans.FaceElementTransformations_HAVE_FACE
    
    Elem1No = property(_eltrans.FaceElementTransformations_Elem1No_get, _eltrans.FaceElementTransformations_Elem1No_set, doc=r"""Elem1No : int""")
    Elem2No = property(_eltrans.FaceElementTransformations_Elem2No_get, _eltrans.FaceElementTransformations_Elem2No_set, doc=r"""Elem2No : int""")
    FaceGeom = property(_eltrans.FaceElementTransformations_FaceGeom_get, _eltrans.FaceElementTransformations_FaceGeom_set, doc=r"""FaceGeom : r.mfem::Geometry::Type""")
    Elem1 = property(_eltrans.FaceElementTransformations_Elem1_get, _eltrans.FaceElementTransformations_Elem1_set, doc=r"""Elem1 : p.mfem::ElementTransformation""")
    Elem2 = property(_eltrans.FaceElementTransformations_Elem2_get, _eltrans.FaceElementTransformations_Elem2_set, doc=r"""Elem2 : p.mfem::ElementTransformation""")
    Face = property(_eltrans.FaceElementTransformations_Face_get, _eltrans.FaceElementTransformations_Face_set, doc=r"""Face : p.mfem::ElementTransformation""")
    Loc1 = property(_eltrans.FaceElementTransformations_Loc1_get, _eltrans.FaceElementTransformations_Loc1_set, doc=r"""Loc1 : mfem::IntegrationPointTransformation""")
    Loc2 = property(_eltrans.FaceElementTransformations_Loc2_get, _eltrans.FaceElementTransformations_Loc2_set, doc=r"""Loc2 : mfem::IntegrationPointTransformation""")

    def __init__(self):
        r"""__init__(FaceElementTransformations self) -> FaceElementTransformations"""
        _eltrans.FaceElementTransformations_swiginit(self, _eltrans.new_FaceElementTransformations())

    def SetGeometryType(self, g):
        r"""SetGeometryType(FaceElementTransformations self, mfem::Geometry::Type g)"""
        return _eltrans.FaceElementTransformations_SetGeometryType(self, g)
    SetGeometryType = _swig_new_instance_method(_eltrans.FaceElementTransformations_SetGeometryType)

    def GetConfigurationMask(self):
        r"""GetConfigurationMask(FaceElementTransformations self) -> int"""
        return _eltrans.FaceElementTransformations_GetConfigurationMask(self)
    GetConfigurationMask = _swig_new_instance_method(_eltrans.FaceElementTransformations_GetConfigurationMask)

    def SetIntPoint(self, face_ip):
        r"""SetIntPoint(FaceElementTransformations self, IntegrationPoint face_ip)"""
        return _eltrans.FaceElementTransformations_SetIntPoint(self, face_ip)
    SetIntPoint = _swig_new_instance_method(_eltrans.FaceElementTransformations_SetIntPoint)

    def SetAllIntPoints(self, face_ip):
        r"""SetAllIntPoints(FaceElementTransformations self, IntegrationPoint face_ip)"""
        return _eltrans.FaceElementTransformations_SetAllIntPoints(self, face_ip)
    SetAllIntPoints = _swig_new_instance_method(_eltrans.FaceElementTransformations_SetAllIntPoints)

    def GetElement1IntPoint(self):
        r"""GetElement1IntPoint(FaceElementTransformations self) -> IntegrationPoint"""
        return _eltrans.FaceElementTransformations_GetElement1IntPoint(self)
    GetElement1IntPoint = _swig_new_instance_method(_eltrans.FaceElementTransformations_GetElement1IntPoint)

    def GetElement2IntPoint(self):
        r"""GetElement2IntPoint(FaceElementTransformations self) -> IntegrationPoint"""
        return _eltrans.FaceElementTransformations_GetElement2IntPoint(self)
    GetElement2IntPoint = _swig_new_instance_method(_eltrans.FaceElementTransformations_GetElement2IntPoint)

    def Transform(self, *args):
        from .vector import Vector
        from .intrules import IntegrationPoint
        if isinstance(args[0], IntegrationPoint):
            vec = Vector()
            _eltrans.ElementTransformation_Transform(self, args[0], vec)
            ret = vec.GetDataArray().copy()
            return ret
        else:
            return _eltrans.ElementTransformation_Transform(self, *args)



    def GetElement1Transformation(self):
        r"""GetElement1Transformation(FaceElementTransformations self) -> ElementTransformation"""
        return _eltrans.FaceElementTransformations_GetElement1Transformation(self)
    GetElement1Transformation = _swig_new_instance_method(_eltrans.FaceElementTransformations_GetElement1Transformation)

    def GetElement2Transformation(self):
        r"""GetElement2Transformation(FaceElementTransformations self) -> ElementTransformation"""
        return _eltrans.FaceElementTransformations_GetElement2Transformation(self)
    GetElement2Transformation = _swig_new_instance_method(_eltrans.FaceElementTransformations_GetElement2Transformation)

    def GetIntPoint1Transformation(self):
        r"""GetIntPoint1Transformation(FaceElementTransformations self) -> IntegrationPointTransformation"""
        return _eltrans.FaceElementTransformations_GetIntPoint1Transformation(self)
    GetIntPoint1Transformation = _swig_new_instance_method(_eltrans.FaceElementTransformations_GetIntPoint1Transformation)

    def GetIntPoint2Transformation(self):
        r"""GetIntPoint2Transformation(FaceElementTransformations self) -> IntegrationPointTransformation"""
        return _eltrans.FaceElementTransformations_GetIntPoint2Transformation(self)
    GetIntPoint2Transformation = _swig_new_instance_method(_eltrans.FaceElementTransformations_GetIntPoint2Transformation)

    def CheckConsistency(self, *args, **kwargs):
        r"""CheckConsistency(FaceElementTransformations self, int print_level=0, std::ostream & out=out) -> double"""
        return _eltrans.FaceElementTransformations_CheckConsistency(self, *args, **kwargs)
    CheckConsistency = _swig_new_instance_method(_eltrans.FaceElementTransformations_CheckConsistency)
    __swig_destroy__ = _eltrans.delete_FaceElementTransformations

# Register FaceElementTransformations in _eltrans:
_eltrans.FaceElementTransformations_swigregister(FaceElementTransformations)



