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
    from . import _intrules
else:
    import _intrules

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _intrules.SWIG_PyInstanceMethod_New
_swig_new_static_method = _intrules.SWIG_PyStaticMethod_New

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


import mfem._ser.array
import mfem._ser.mem_manager
class IntegrationPointArray(object):
    r"""Proxy of C++ mfem::Array< mfem::IntegrationPoint > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _intrules.delete_IntegrationPointArray

    def GetData(self, *args):
        r"""
        GetData(IntegrationPointArray self) -> IntegrationPoint
        GetData(IntegrationPointArray self) -> IntegrationPoint
        """
        return _intrules.IntegrationPointArray_GetData(self, *args)
    GetData = _swig_new_instance_method(_intrules.IntegrationPointArray_GetData)

    def GetMemory(self, *args):
        r"""
        GetMemory(IntegrationPointArray self) -> mfem::Memory< mfem::IntegrationPoint >
        GetMemory(IntegrationPointArray self) -> mfem::Memory< mfem::IntegrationPoint > const &
        """
        return _intrules.IntegrationPointArray_GetMemory(self, *args)
    GetMemory = _swig_new_instance_method(_intrules.IntegrationPointArray_GetMemory)

    def UseDevice(self):
        r"""UseDevice(IntegrationPointArray self) -> bool"""
        return _intrules.IntegrationPointArray_UseDevice(self)
    UseDevice = _swig_new_instance_method(_intrules.IntegrationPointArray_UseDevice)

    def OwnsData(self):
        r"""OwnsData(IntegrationPointArray self) -> bool"""
        return _intrules.IntegrationPointArray_OwnsData(self)
    OwnsData = _swig_new_instance_method(_intrules.IntegrationPointArray_OwnsData)

    def StealData(self, p):
        r"""StealData(IntegrationPointArray self, mfem::IntegrationPoint ** p)"""
        return _intrules.IntegrationPointArray_StealData(self, p)
    StealData = _swig_new_instance_method(_intrules.IntegrationPointArray_StealData)

    def LoseData(self):
        r"""LoseData(IntegrationPointArray self)"""
        return _intrules.IntegrationPointArray_LoseData(self)
    LoseData = _swig_new_instance_method(_intrules.IntegrationPointArray_LoseData)

    def MakeDataOwner(self):
        r"""MakeDataOwner(IntegrationPointArray self)"""
        return _intrules.IntegrationPointArray_MakeDataOwner(self)
    MakeDataOwner = _swig_new_instance_method(_intrules.IntegrationPointArray_MakeDataOwner)

    def Size(self):
        r"""Size(IntegrationPointArray self) -> int"""
        return _intrules.IntegrationPointArray_Size(self)
    Size = _swig_new_instance_method(_intrules.IntegrationPointArray_Size)

    def SetSize(self, *args):
        r"""
        SetSize(IntegrationPointArray self, int nsize)
        SetSize(IntegrationPointArray self, int nsize, IntegrationPoint initval)
        SetSize(IntegrationPointArray self, int nsize, mfem::MemoryType mt)
        """
        return _intrules.IntegrationPointArray_SetSize(self, *args)
    SetSize = _swig_new_instance_method(_intrules.IntegrationPointArray_SetSize)

    def Capacity(self):
        r"""Capacity(IntegrationPointArray self) -> int"""
        return _intrules.IntegrationPointArray_Capacity(self)
    Capacity = _swig_new_instance_method(_intrules.IntegrationPointArray_Capacity)

    def Reserve(self, capacity):
        r"""Reserve(IntegrationPointArray self, int capacity)"""
        return _intrules.IntegrationPointArray_Reserve(self, capacity)
    Reserve = _swig_new_instance_method(_intrules.IntegrationPointArray_Reserve)

    def Append(self, *args):
        r"""
        Append(IntegrationPointArray self, IntegrationPoint el) -> int
        Append(IntegrationPointArray self, IntegrationPoint els, int nels) -> int
        Append(IntegrationPointArray self, IntegrationPointArray els) -> int
        """
        return _intrules.IntegrationPointArray_Append(self, *args)
    Append = _swig_new_instance_method(_intrules.IntegrationPointArray_Append)

    def Prepend(self, el):
        r"""Prepend(IntegrationPointArray self, IntegrationPoint el) -> int"""
        return _intrules.IntegrationPointArray_Prepend(self, el)
    Prepend = _swig_new_instance_method(_intrules.IntegrationPointArray_Prepend)

    def Last(self, *args):
        r"""
        Last(IntegrationPointArray self) -> IntegrationPoint
        Last(IntegrationPointArray self) -> IntegrationPoint
        """
        return _intrules.IntegrationPointArray_Last(self, *args)
    Last = _swig_new_instance_method(_intrules.IntegrationPointArray_Last)

    def DeleteLast(self):
        r"""DeleteLast(IntegrationPointArray self)"""
        return _intrules.IntegrationPointArray_DeleteLast(self)
    DeleteLast = _swig_new_instance_method(_intrules.IntegrationPointArray_DeleteLast)

    def DeleteAll(self):
        r"""DeleteAll(IntegrationPointArray self)"""
        return _intrules.IntegrationPointArray_DeleteAll(self)
    DeleteAll = _swig_new_instance_method(_intrules.IntegrationPointArray_DeleteAll)

    def Copy(self, copy):
        r"""Copy(IntegrationPointArray self, IntegrationPointArray copy)"""
        return _intrules.IntegrationPointArray_Copy(self, copy)
    Copy = _swig_new_instance_method(_intrules.IntegrationPointArray_Copy)

    def MakeRef(self, *args):
        r"""
        MakeRef(IntegrationPointArray self, IntegrationPoint arg2, int arg3)
        MakeRef(IntegrationPointArray self, IntegrationPointArray master)
        """
        return _intrules.IntegrationPointArray_MakeRef(self, *args)
    MakeRef = _swig_new_instance_method(_intrules.IntegrationPointArray_MakeRef)

    def GetSubArray(self, offset, sa_size, sa):
        r"""GetSubArray(IntegrationPointArray self, int offset, int sa_size, IntegrationPointArray sa)"""
        return _intrules.IntegrationPointArray_GetSubArray(self, offset, sa_size, sa)
    GetSubArray = _swig_new_instance_method(_intrules.IntegrationPointArray_GetSubArray)

    def begin(self, *args):
        r"""
        begin(IntegrationPointArray self) -> IntegrationPoint
        begin(IntegrationPointArray self) -> IntegrationPoint
        """
        return _intrules.IntegrationPointArray_begin(self, *args)
    begin = _swig_new_instance_method(_intrules.IntegrationPointArray_begin)

    def end(self, *args):
        r"""
        end(IntegrationPointArray self) -> IntegrationPoint
        end(IntegrationPointArray self) -> IntegrationPoint
        """
        return _intrules.IntegrationPointArray_end(self, *args)
    end = _swig_new_instance_method(_intrules.IntegrationPointArray_end)

    def MemoryUsage(self):
        r"""MemoryUsage(IntegrationPointArray self) -> std::size_t"""
        return _intrules.IntegrationPointArray_MemoryUsage(self)
    MemoryUsage = _swig_new_instance_method(_intrules.IntegrationPointArray_MemoryUsage)

    def Read(self, on_dev=True):
        r"""Read(IntegrationPointArray self, bool on_dev=True) -> IntegrationPoint"""
        return _intrules.IntegrationPointArray_Read(self, on_dev)
    Read = _swig_new_instance_method(_intrules.IntegrationPointArray_Read)

    def HostRead(self):
        r"""HostRead(IntegrationPointArray self) -> IntegrationPoint"""
        return _intrules.IntegrationPointArray_HostRead(self)
    HostRead = _swig_new_instance_method(_intrules.IntegrationPointArray_HostRead)

    def Write(self, on_dev=True):
        r"""Write(IntegrationPointArray self, bool on_dev=True) -> IntegrationPoint"""
        return _intrules.IntegrationPointArray_Write(self, on_dev)
    Write = _swig_new_instance_method(_intrules.IntegrationPointArray_Write)

    def HostWrite(self):
        r"""HostWrite(IntegrationPointArray self) -> IntegrationPoint"""
        return _intrules.IntegrationPointArray_HostWrite(self)
    HostWrite = _swig_new_instance_method(_intrules.IntegrationPointArray_HostWrite)

    def ReadWrite(self, on_dev=True):
        r"""ReadWrite(IntegrationPointArray self, bool on_dev=True) -> IntegrationPoint"""
        return _intrules.IntegrationPointArray_ReadWrite(self, on_dev)
    ReadWrite = _swig_new_instance_method(_intrules.IntegrationPointArray_ReadWrite)

    def HostReadWrite(self):
        r"""HostReadWrite(IntegrationPointArray self) -> IntegrationPoint"""
        return _intrules.IntegrationPointArray_HostReadWrite(self)
    HostReadWrite = _swig_new_instance_method(_intrules.IntegrationPointArray_HostReadWrite)

    def __init__(self, *args):
        r"""
        __init__(IntegrationPointArray self) -> IntegrationPointArray
        __init__(IntegrationPointArray self, mfem::MemoryType mt) -> IntegrationPointArray
        __init__(IntegrationPointArray self, int asize) -> IntegrationPointArray
        __init__(IntegrationPointArray self, int asize, mfem::MemoryType mt) -> IntegrationPointArray
        __init__(IntegrationPointArray self, IntegrationPoint data_) -> IntegrationPointArray
        __init__(IntegrationPointArray self, IntegrationPointArray src) -> IntegrationPointArray
        __init__(IntegrationPointArray self, void * List_or_Tuple) -> IntegrationPointArray
        """
        _intrules.IntegrationPointArray_swiginit(self, _intrules.new_IntegrationPointArray(*args))

    def __setitem__(self, i, v):
        r"""__setitem__(IntegrationPointArray self, int i, IntegrationPoint v)"""

        i = int(i)


        return _intrules.IntegrationPointArray___setitem__(self, i, v)


    def Assign(self, *args):
        r"""
        Assign(IntegrationPointArray self, IntegrationPoint arg2)
        Assign(IntegrationPointArray self, IntegrationPoint a)
        """
        return _intrules.IntegrationPointArray_Assign(self, *args)
    Assign = _swig_new_instance_method(_intrules.IntegrationPointArray_Assign)

    def ToList(self):
        return [self[i] for i in range(self.Size())]



    def __iter__(self):
        class iter_array:
            def __init__(self, obj):
                self.obj = obj
                self.idx = 0
                self.size = obj.Size()
            def __iter__(self):
                self.idx = 0
            def __next__(self):
                if self.idx < self.size:
                    res = self.obj[self.idx]
                    self.idx += 1
                    return res
                else:
                    raise StopIteration
        return iter_array(self)



    def __getitem__(self, param):
        r"""__getitem__(IntegrationPointArray self, PyObject * param) -> PyObject *"""
        return _intrules.IntegrationPointArray___getitem__(self, param)
    __getitem__ = _swig_new_instance_method(_intrules.IntegrationPointArray___getitem__)

# Register IntegrationPointArray in _intrules:
_intrules.IntegrationPointArray_swigregister(IntegrationPointArray)

class IntegrationRulePtrArray(object):
    r"""Proxy of C++ mfem::Array< mfem::IntegrationRule * > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _intrules.delete_IntegrationRulePtrArray

    def GetData(self, *args):
        r"""
        GetData(IntegrationRulePtrArray self) -> IntegrationRule
        GetData(IntegrationRulePtrArray self) -> mfem::IntegrationRule *const *
        """
        return _intrules.IntegrationRulePtrArray_GetData(self, *args)
    GetData = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_GetData)

    def GetMemory(self, *args):
        r"""
        GetMemory(IntegrationRulePtrArray self) -> mfem::Memory< mfem::IntegrationRule * >
        GetMemory(IntegrationRulePtrArray self) -> mfem::Memory< mfem::IntegrationRule * > const &
        """
        return _intrules.IntegrationRulePtrArray_GetMemory(self, *args)
    GetMemory = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_GetMemory)

    def UseDevice(self):
        r"""UseDevice(IntegrationRulePtrArray self) -> bool"""
        return _intrules.IntegrationRulePtrArray_UseDevice(self)
    UseDevice = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_UseDevice)

    def OwnsData(self):
        r"""OwnsData(IntegrationRulePtrArray self) -> bool"""
        return _intrules.IntegrationRulePtrArray_OwnsData(self)
    OwnsData = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_OwnsData)

    def StealData(self, p):
        r"""StealData(IntegrationRulePtrArray self, mfem::IntegrationRule *** p)"""
        return _intrules.IntegrationRulePtrArray_StealData(self, p)
    StealData = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_StealData)

    def LoseData(self):
        r"""LoseData(IntegrationRulePtrArray self)"""
        return _intrules.IntegrationRulePtrArray_LoseData(self)
    LoseData = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_LoseData)

    def MakeDataOwner(self):
        r"""MakeDataOwner(IntegrationRulePtrArray self)"""
        return _intrules.IntegrationRulePtrArray_MakeDataOwner(self)
    MakeDataOwner = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_MakeDataOwner)

    def Size(self):
        r"""Size(IntegrationRulePtrArray self) -> int"""
        return _intrules.IntegrationRulePtrArray_Size(self)
    Size = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Size)

    def SetSize(self, *args):
        r"""
        SetSize(IntegrationRulePtrArray self, int nsize)
        SetSize(IntegrationRulePtrArray self, int nsize, IntegrationRule initval)
        SetSize(IntegrationRulePtrArray self, int nsize, mfem::MemoryType mt)
        """
        return _intrules.IntegrationRulePtrArray_SetSize(self, *args)
    SetSize = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_SetSize)

    def Capacity(self):
        r"""Capacity(IntegrationRulePtrArray self) -> int"""
        return _intrules.IntegrationRulePtrArray_Capacity(self)
    Capacity = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Capacity)

    def Reserve(self, capacity):
        r"""Reserve(IntegrationRulePtrArray self, int capacity)"""
        return _intrules.IntegrationRulePtrArray_Reserve(self, capacity)
    Reserve = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Reserve)

    def Append(self, *args):
        r"""
        Append(IntegrationRulePtrArray self, IntegrationRule el) -> int
        Append(IntegrationRulePtrArray self, mfem::IntegrationRule *const * els, int nels) -> int
        Append(IntegrationRulePtrArray self, IntegrationRulePtrArray els) -> int
        """
        return _intrules.IntegrationRulePtrArray_Append(self, *args)
    Append = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Append)

    def Prepend(self, el):
        r"""Prepend(IntegrationRulePtrArray self, IntegrationRule el) -> int"""
        return _intrules.IntegrationRulePtrArray_Prepend(self, el)
    Prepend = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Prepend)

    def Last(self, *args):
        r"""
        Last(IntegrationRulePtrArray self) -> IntegrationRule
        Last(IntegrationRulePtrArray self) -> IntegrationRule
        """
        return _intrules.IntegrationRulePtrArray_Last(self, *args)
    Last = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Last)

    def DeleteLast(self):
        r"""DeleteLast(IntegrationRulePtrArray self)"""
        return _intrules.IntegrationRulePtrArray_DeleteLast(self)
    DeleteLast = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_DeleteLast)

    def DeleteAll(self):
        r"""DeleteAll(IntegrationRulePtrArray self)"""
        return _intrules.IntegrationRulePtrArray_DeleteAll(self)
    DeleteAll = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_DeleteAll)

    def Copy(self, copy):
        r"""Copy(IntegrationRulePtrArray self, IntegrationRulePtrArray copy)"""
        return _intrules.IntegrationRulePtrArray_Copy(self, copy)
    Copy = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Copy)

    def MakeRef(self, *args):
        r"""
        MakeRef(IntegrationRulePtrArray self, mfem::IntegrationRule ** arg2, int arg3)
        MakeRef(IntegrationRulePtrArray self, IntegrationRulePtrArray master)
        """
        return _intrules.IntegrationRulePtrArray_MakeRef(self, *args)
    MakeRef = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_MakeRef)

    def GetSubArray(self, offset, sa_size, sa):
        r"""GetSubArray(IntegrationRulePtrArray self, int offset, int sa_size, IntegrationRulePtrArray sa)"""
        return _intrules.IntegrationRulePtrArray_GetSubArray(self, offset, sa_size, sa)
    GetSubArray = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_GetSubArray)

    def begin(self, *args):
        r"""
        begin(IntegrationRulePtrArray self) -> IntegrationRule
        begin(IntegrationRulePtrArray self) -> mfem::IntegrationRule *const *
        """
        return _intrules.IntegrationRulePtrArray_begin(self, *args)
    begin = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_begin)

    def end(self, *args):
        r"""
        end(IntegrationRulePtrArray self) -> IntegrationRule
        end(IntegrationRulePtrArray self) -> mfem::IntegrationRule *const *
        """
        return _intrules.IntegrationRulePtrArray_end(self, *args)
    end = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_end)

    def MemoryUsage(self):
        r"""MemoryUsage(IntegrationRulePtrArray self) -> std::size_t"""
        return _intrules.IntegrationRulePtrArray_MemoryUsage(self)
    MemoryUsage = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_MemoryUsage)

    def Read(self, on_dev=True):
        r"""Read(IntegrationRulePtrArray self, bool on_dev=True) -> mfem::IntegrationRule *const *"""
        return _intrules.IntegrationRulePtrArray_Read(self, on_dev)
    Read = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Read)

    def HostRead(self):
        r"""HostRead(IntegrationRulePtrArray self) -> mfem::IntegrationRule *const *"""
        return _intrules.IntegrationRulePtrArray_HostRead(self)
    HostRead = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_HostRead)

    def Write(self, on_dev=True):
        r"""Write(IntegrationRulePtrArray self, bool on_dev=True) -> mfem::IntegrationRule **"""
        return _intrules.IntegrationRulePtrArray_Write(self, on_dev)
    Write = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Write)

    def HostWrite(self):
        r"""HostWrite(IntegrationRulePtrArray self) -> mfem::IntegrationRule **"""
        return _intrules.IntegrationRulePtrArray_HostWrite(self)
    HostWrite = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_HostWrite)

    def ReadWrite(self, on_dev=True):
        r"""ReadWrite(IntegrationRulePtrArray self, bool on_dev=True) -> mfem::IntegrationRule **"""
        return _intrules.IntegrationRulePtrArray_ReadWrite(self, on_dev)
    ReadWrite = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_ReadWrite)

    def HostReadWrite(self):
        r"""HostReadWrite(IntegrationRulePtrArray self) -> mfem::IntegrationRule **"""
        return _intrules.IntegrationRulePtrArray_HostReadWrite(self)
    HostReadWrite = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_HostReadWrite)

    def __init__(self, *args):
        r"""
        __init__(IntegrationRulePtrArray self) -> IntegrationRulePtrArray
        __init__(IntegrationRulePtrArray self, mfem::MemoryType mt) -> IntegrationRulePtrArray
        __init__(IntegrationRulePtrArray self, int asize) -> IntegrationRulePtrArray
        __init__(IntegrationRulePtrArray self, int asize, mfem::MemoryType mt) -> IntegrationRulePtrArray
        __init__(IntegrationRulePtrArray self, mfem::IntegrationRule ** data_) -> IntegrationRulePtrArray
        __init__(IntegrationRulePtrArray self, IntegrationRulePtrArray src) -> IntegrationRulePtrArray
        __init__(IntegrationRulePtrArray self, void * List_or_Tuple) -> IntegrationRulePtrArray
        """
        _intrules.IntegrationRulePtrArray_swiginit(self, _intrules.new_IntegrationRulePtrArray(*args))

    def __setitem__(self, i, v):
        r"""__setitem__(IntegrationRulePtrArray self, int i, IntegrationRule v)"""

        i = int(i)


        return _intrules.IntegrationRulePtrArray___setitem__(self, i, v)


    def Assign(self, *args):
        r"""
        Assign(IntegrationRulePtrArray self, mfem::IntegrationRule *const * arg2)
        Assign(IntegrationRulePtrArray self, IntegrationRule a)
        """
        return _intrules.IntegrationRulePtrArray_Assign(self, *args)
    Assign = _swig_new_instance_method(_intrules.IntegrationRulePtrArray_Assign)

    def ToList(self):
        return [self[i] for i in range(self.Size())]



    def __iter__(self):
        class iter_array:
            def __init__(self, obj):
                self.obj = obj
                self.idx = 0
                self.size = obj.Size()
            def __iter__(self):
                self.idx = 0
            def __next__(self):
                if self.idx < self.size:
                    res = self.obj[self.idx]
                    self.idx += 1
                    return res
                else:
                    raise StopIteration
        return iter_array(self)



    def __getitem__(self, param):
        r"""__getitem__(IntegrationRulePtrArray self, PyObject * param) -> PyObject *"""
        return _intrules.IntegrationRulePtrArray___getitem__(self, param)
    __getitem__ = _swig_new_instance_method(_intrules.IntegrationRulePtrArray___getitem__)

# Register IntegrationRulePtrArray in _intrules:
_intrules.IntegrationRulePtrArray_swigregister(IntegrationRulePtrArray)

class IntegrationPoint(object):
    r"""Proxy of C++ mfem::IntegrationPoint class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_intrules.IntegrationPoint_x_get, _intrules.IntegrationPoint_x_set, doc=r"""x : double""")
    y = property(_intrules.IntegrationPoint_y_get, _intrules.IntegrationPoint_y_set, doc=r"""y : double""")
    z = property(_intrules.IntegrationPoint_z_get, _intrules.IntegrationPoint_z_set, doc=r"""z : double""")
    weight = property(_intrules.IntegrationPoint_weight_get, _intrules.IntegrationPoint_weight_set, doc=r"""weight : double""")
    index = property(_intrules.IntegrationPoint_index_get, _intrules.IntegrationPoint_index_set, doc=r"""index : int""")

    def Init(self, i):
        r"""Init(IntegrationPoint self, int const i)"""
        return _intrules.IntegrationPoint_Init(self, i)
    Init = _swig_new_instance_method(_intrules.IntegrationPoint_Init)

    def Get(self, p, dim):
        r"""Get(IntegrationPoint self, double * p, int const dim)"""
        return _intrules.IntegrationPoint_Get(self, p, dim)
    Get = _swig_new_instance_method(_intrules.IntegrationPoint_Get)

    def Set(self, *args):
        r"""
        Set(IntegrationPoint self, double const * p, int const dim)
        Set(IntegrationPoint self, double const x1, double const x2, double const x3, double const w)
        """
        return _intrules.IntegrationPoint_Set(self, *args)
    Set = _swig_new_instance_method(_intrules.IntegrationPoint_Set)

    def Set3w(self, p):
        r"""Set3w(IntegrationPoint self, double const * p)"""
        return _intrules.IntegrationPoint_Set3w(self, p)
    Set3w = _swig_new_instance_method(_intrules.IntegrationPoint_Set3w)

    def Set3(self, *args):
        r"""
        Set3(IntegrationPoint self, double const x1, double const x2, double const x3)
        Set3(IntegrationPoint self, double const * p)
        """
        return _intrules.IntegrationPoint_Set3(self, *args)
    Set3 = _swig_new_instance_method(_intrules.IntegrationPoint_Set3)

    def Set2w(self, *args):
        r"""
        Set2w(IntegrationPoint self, double const x1, double const x2, double const w)
        Set2w(IntegrationPoint self, double const * p)
        """
        return _intrules.IntegrationPoint_Set2w(self, *args)
    Set2w = _swig_new_instance_method(_intrules.IntegrationPoint_Set2w)

    def Set2(self, *args):
        r"""
        Set2(IntegrationPoint self, double const x1, double const x2)
        Set2(IntegrationPoint self, double const * p)
        """
        return _intrules.IntegrationPoint_Set2(self, *args)
    Set2 = _swig_new_instance_method(_intrules.IntegrationPoint_Set2)

    def Set1w(self, *args):
        r"""
        Set1w(IntegrationPoint self, double const x1, double const w)
        Set1w(IntegrationPoint self, double const * p)
        """
        return _intrules.IntegrationPoint_Set1w(self, *args)
    Set1w = _swig_new_instance_method(_intrules.IntegrationPoint_Set1w)

    def __init__(self):
        r"""__init__(IntegrationPoint self) -> IntegrationPoint"""
        _intrules.IntegrationPoint_swiginit(self, _intrules.new_IntegrationPoint())
    __swig_destroy__ = _intrules.delete_IntegrationPoint

# Register IntegrationPoint in _intrules:
_intrules.IntegrationPoint_swigregister(IntegrationPoint)

class IntegrationRule(IntegrationPointArray):
    r"""Proxy of C++ mfem::IntegrationRule class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def SetPointIndices(self):
        r"""SetPointIndices(IntegrationRule self)"""
        return _intrules.IntegrationRule_SetPointIndices(self)
    SetPointIndices = _swig_new_instance_method(_intrules.IntegrationRule_SetPointIndices)

    def __init__(self, *args):
        r"""
        __init__(IntegrationRule self) -> IntegrationRule
        __init__(IntegrationRule self, int NP) -> IntegrationRule
        __init__(IntegrationRule self, IntegrationRule irx, IntegrationRule iry) -> IntegrationRule
        __init__(IntegrationRule self, IntegrationRule irx, IntegrationRule iry, IntegrationRule irz) -> IntegrationRule
        """
        _intrules.IntegrationRule_swiginit(self, _intrules.new_IntegrationRule(*args))

    def GetOrder(self):
        r"""GetOrder(IntegrationRule self) -> int"""
        return _intrules.IntegrationRule_GetOrder(self)
    GetOrder = _swig_new_instance_method(_intrules.IntegrationRule_GetOrder)

    def SetOrder(self, order):
        r"""SetOrder(IntegrationRule self, int const order)"""
        return _intrules.IntegrationRule_SetOrder(self, order)
    SetOrder = _swig_new_instance_method(_intrules.IntegrationRule_SetOrder)

    def GetNPoints(self):
        r"""GetNPoints(IntegrationRule self) -> int"""
        return _intrules.IntegrationRule_GetNPoints(self)
    GetNPoints = _swig_new_instance_method(_intrules.IntegrationRule_GetNPoints)

    def IntPoint(self, *args):
        r"""
        IntPoint(IntegrationRule self, int i) -> IntegrationPoint
        IntPoint(IntegrationRule self, int i) -> IntegrationPoint
        """
        return _intrules.IntegrationRule_IntPoint(self, *args)
    IntPoint = _swig_new_instance_method(_intrules.IntegrationRule_IntPoint)

    def GetWeights(self):
        r"""GetWeights(IntegrationRule self) -> doubleArray"""
        return _intrules.IntegrationRule_GetWeights(self)
    GetWeights = _swig_new_instance_method(_intrules.IntegrationRule_GetWeights)
    __swig_destroy__ = _intrules.delete_IntegrationRule

# Register IntegrationRule in _intrules:
_intrules.IntegrationRule_swigregister(IntegrationRule)

class QuadratureFunctions1D(object):
    r"""Proxy of C++ mfem::QuadratureFunctions1D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def GaussLegendre(np, ir):
        r"""GaussLegendre(int const np, IntegrationRule ir)"""
        return _intrules.QuadratureFunctions1D_GaussLegendre(np, ir)
    GaussLegendre = _swig_new_static_method(_intrules.QuadratureFunctions1D_GaussLegendre)

    @staticmethod
    def GaussLobatto(np, ir):
        r"""GaussLobatto(int const np, IntegrationRule ir)"""
        return _intrules.QuadratureFunctions1D_GaussLobatto(np, ir)
    GaussLobatto = _swig_new_static_method(_intrules.QuadratureFunctions1D_GaussLobatto)

    @staticmethod
    def OpenUniform(np, ir):
        r"""OpenUniform(int const np, IntegrationRule ir)"""
        return _intrules.QuadratureFunctions1D_OpenUniform(np, ir)
    OpenUniform = _swig_new_static_method(_intrules.QuadratureFunctions1D_OpenUniform)

    @staticmethod
    def ClosedUniform(np, ir):
        r"""ClosedUniform(int const np, IntegrationRule ir)"""
        return _intrules.QuadratureFunctions1D_ClosedUniform(np, ir)
    ClosedUniform = _swig_new_static_method(_intrules.QuadratureFunctions1D_ClosedUniform)

    @staticmethod
    def OpenHalfUniform(np, ir):
        r"""OpenHalfUniform(int const np, IntegrationRule ir)"""
        return _intrules.QuadratureFunctions1D_OpenHalfUniform(np, ir)
    OpenHalfUniform = _swig_new_static_method(_intrules.QuadratureFunctions1D_OpenHalfUniform)

    @staticmethod
    def ClosedGL(np, ir):
        r"""ClosedGL(int const np, IntegrationRule ir)"""
        return _intrules.QuadratureFunctions1D_ClosedGL(np, ir)
    ClosedGL = _swig_new_static_method(_intrules.QuadratureFunctions1D_ClosedGL)

    @staticmethod
    def GivePolyPoints(np, pts, type):
        r"""GivePolyPoints(int const np, double * pts, int const type)"""
        return _intrules.QuadratureFunctions1D_GivePolyPoints(np, pts, type)
    GivePolyPoints = _swig_new_static_method(_intrules.QuadratureFunctions1D_GivePolyPoints)

    def __init__(self):
        r"""__init__(QuadratureFunctions1D self) -> QuadratureFunctions1D"""
        _intrules.QuadratureFunctions1D_swiginit(self, _intrules.new_QuadratureFunctions1D())
    __swig_destroy__ = _intrules.delete_QuadratureFunctions1D

# Register QuadratureFunctions1D in _intrules:
_intrules.QuadratureFunctions1D_swigregister(QuadratureFunctions1D)

def QuadratureFunctions1D_GaussLegendre(np, ir):
    r"""QuadratureFunctions1D_GaussLegendre(int const np, IntegrationRule ir)"""
    return _intrules.QuadratureFunctions1D_GaussLegendre(np, ir)
QuadratureFunctions1D_GaussLegendre = _intrules.QuadratureFunctions1D_GaussLegendre

def QuadratureFunctions1D_GaussLobatto(np, ir):
    r"""QuadratureFunctions1D_GaussLobatto(int const np, IntegrationRule ir)"""
    return _intrules.QuadratureFunctions1D_GaussLobatto(np, ir)
QuadratureFunctions1D_GaussLobatto = _intrules.QuadratureFunctions1D_GaussLobatto

def QuadratureFunctions1D_OpenUniform(np, ir):
    r"""QuadratureFunctions1D_OpenUniform(int const np, IntegrationRule ir)"""
    return _intrules.QuadratureFunctions1D_OpenUniform(np, ir)
QuadratureFunctions1D_OpenUniform = _intrules.QuadratureFunctions1D_OpenUniform

def QuadratureFunctions1D_ClosedUniform(np, ir):
    r"""QuadratureFunctions1D_ClosedUniform(int const np, IntegrationRule ir)"""
    return _intrules.QuadratureFunctions1D_ClosedUniform(np, ir)
QuadratureFunctions1D_ClosedUniform = _intrules.QuadratureFunctions1D_ClosedUniform

def QuadratureFunctions1D_OpenHalfUniform(np, ir):
    r"""QuadratureFunctions1D_OpenHalfUniform(int const np, IntegrationRule ir)"""
    return _intrules.QuadratureFunctions1D_OpenHalfUniform(np, ir)
QuadratureFunctions1D_OpenHalfUniform = _intrules.QuadratureFunctions1D_OpenHalfUniform

def QuadratureFunctions1D_ClosedGL(np, ir):
    r"""QuadratureFunctions1D_ClosedGL(int const np, IntegrationRule ir)"""
    return _intrules.QuadratureFunctions1D_ClosedGL(np, ir)
QuadratureFunctions1D_ClosedGL = _intrules.QuadratureFunctions1D_ClosedGL

def QuadratureFunctions1D_GivePolyPoints(np, pts, type):
    r"""QuadratureFunctions1D_GivePolyPoints(int const np, double * pts, int const type)"""
    return _intrules.QuadratureFunctions1D_GivePolyPoints(np, pts, type)
QuadratureFunctions1D_GivePolyPoints = _intrules.QuadratureFunctions1D_GivePolyPoints

class Quadrature1D(object):
    r"""Proxy of C++ mfem::Quadrature1D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Invalid = _intrules.Quadrature1D_Invalid
    
    GaussLegendre = _intrules.Quadrature1D_GaussLegendre
    
    GaussLobatto = _intrules.Quadrature1D_GaussLobatto
    
    OpenUniform = _intrules.Quadrature1D_OpenUniform
    
    ClosedUniform = _intrules.Quadrature1D_ClosedUniform
    
    OpenHalfUniform = _intrules.Quadrature1D_OpenHalfUniform
    
    ClosedGL = _intrules.Quadrature1D_ClosedGL
    

    @staticmethod
    def CheckClosed(type):
        r"""CheckClosed(int type) -> int"""
        return _intrules.Quadrature1D_CheckClosed(type)
    CheckClosed = _swig_new_static_method(_intrules.Quadrature1D_CheckClosed)

    @staticmethod
    def CheckOpen(type):
        r"""CheckOpen(int type) -> int"""
        return _intrules.Quadrature1D_CheckOpen(type)
    CheckOpen = _swig_new_static_method(_intrules.Quadrature1D_CheckOpen)

    def __init__(self):
        r"""__init__(Quadrature1D self) -> Quadrature1D"""
        _intrules.Quadrature1D_swiginit(self, _intrules.new_Quadrature1D())
    __swig_destroy__ = _intrules.delete_Quadrature1D

# Register Quadrature1D in _intrules:
_intrules.Quadrature1D_swigregister(Quadrature1D)

def Quadrature1D_CheckClosed(type):
    r"""Quadrature1D_CheckClosed(int type) -> int"""
    return _intrules.Quadrature1D_CheckClosed(type)
Quadrature1D_CheckClosed = _intrules.Quadrature1D_CheckClosed

def Quadrature1D_CheckOpen(type):
    r"""Quadrature1D_CheckOpen(int type) -> int"""
    return _intrules.Quadrature1D_CheckOpen(type)
Quadrature1D_CheckOpen = _intrules.Quadrature1D_CheckOpen

class IntegrationRules(object):
    r"""Proxy of C++ mfem::IntegrationRules class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(IntegrationRules self, int Ref=0, int type=GaussLegendre) -> IntegrationRules"""
        _intrules.IntegrationRules_swiginit(self, _intrules.new_IntegrationRules(*args, **kwargs))

    def Get(self, GeomType, Order):
        r"""Get(IntegrationRules self, int GeomType, int Order) -> IntegrationRule"""
        return _intrules.IntegrationRules_Get(self, GeomType, Order)
    Get = _swig_new_instance_method(_intrules.IntegrationRules_Get)

    def Set(self, GeomType, Order, IntRule):
        r"""Set(IntegrationRules self, int GeomType, int Order, IntegrationRule IntRule)"""
        return _intrules.IntegrationRules_Set(self, GeomType, Order, IntRule)
    Set = _swig_new_instance_method(_intrules.IntegrationRules_Set)

    def SetOwnRules(self, o):
        r"""SetOwnRules(IntegrationRules self, int o)"""
        return _intrules.IntegrationRules_SetOwnRules(self, o)
    SetOwnRules = _swig_new_instance_method(_intrules.IntegrationRules_SetOwnRules)
    __swig_destroy__ = _intrules.delete_IntegrationRules

# Register IntegrationRules in _intrules:
_intrules.IntegrationRules_swigregister(IntegrationRules)


cvar = _intrules.cvar
IntRules = cvar.IntRules
RefinedIntRules = cvar.RefinedIntRules

