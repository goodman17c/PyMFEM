# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _device
else:
    import _device

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _device.SWIG_PyInstanceMethod_New
_swig_new_static_method = _device.SWIG_PyStaticMethod_New

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


import mfem._par.mem_manager
class Backend(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CPU = _device.Backend_CPU
    OMP = _device.Backend_OMP
    CUDA = _device.Backend_CUDA
    HIP = _device.Backend_HIP
    RAJA_CPU = _device.Backend_RAJA_CPU
    RAJA_OMP = _device.Backend_RAJA_OMP
    RAJA_CUDA = _device.Backend_RAJA_CUDA
    OCCA_CPU = _device.Backend_OCCA_CPU
    OCCA_OMP = _device.Backend_OCCA_OMP
    OCCA_CUDA = _device.Backend_OCCA_CUDA
    CEED_CPU = _device.Backend_CEED_CPU
    CEED_CUDA = _device.Backend_CEED_CUDA
    DEBUG = _device.Backend_DEBUG
    NUM_BACKENDS = _device.Backend_NUM_BACKENDS
    CPU_MASK = _device.Backend_CPU_MASK
    CUDA_MASK = _device.Backend_CUDA_MASK
    HIP_MASK = _device.Backend_HIP_MASK
    OMP_MASK = _device.Backend_OMP_MASK
    CEED_MASK = _device.Backend_CEED_MASK
    DEVICE_MASK = _device.Backend_DEVICE_MASK
    RAJA_MASK = _device.Backend_RAJA_MASK
    OCCA_MASK = _device.Backend_OCCA_MASK

    def __init__(self):
        _device.Backend_swiginit(self, _device.new_Backend())
    __swig_destroy__ = _device.delete_Backend

# Register Backend in _device:
_device.Backend_swigregister(Backend)

class Device(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _device.Device_swiginit(self, _device.new_Device(*args))
    __swig_destroy__ = _device.delete_Device

    def Configure(self, device, dev=0):
        return _device.Device_Configure(self, device, dev)
    Configure = _swig_new_instance_method(_device.Device_Configure)

    def Print(self, *args):
        return _device.Device_Print(self, *args)
    Print = _swig_new_instance_method(_device.Device_Print)

    @staticmethod
    def IsConfigured():
        return _device.Device_IsConfigured()
    IsConfigured = _swig_new_static_method(_device.Device_IsConfigured)

    @staticmethod
    def IsAvailable():
        return _device.Device_IsAvailable()
    IsAvailable = _swig_new_static_method(_device.Device_IsAvailable)

    @staticmethod
    def IsEnabled():
        return _device.Device_IsEnabled()
    IsEnabled = _swig_new_static_method(_device.Device_IsEnabled)

    @staticmethod
    def IsDisabled():
        return _device.Device_IsDisabled()
    IsDisabled = _swig_new_static_method(_device.Device_IsDisabled)

    @staticmethod
    def Allows(b_mask):
        return _device.Device_Allows(b_mask)
    Allows = _swig_new_static_method(_device.Device_Allows)

    @staticmethod
    def GetHostMemoryType():
        return _device.Device_GetHostMemoryType()
    GetHostMemoryType = _swig_new_static_method(_device.Device_GetHostMemoryType)

    @staticmethod
    def GetHostMemoryClass():
        return _device.Device_GetHostMemoryClass()
    GetHostMemoryClass = _swig_new_static_method(_device.Device_GetHostMemoryClass)

    @staticmethod
    def GetDeviceMemoryType():
        return _device.Device_GetDeviceMemoryType()
    GetDeviceMemoryType = _swig_new_static_method(_device.Device_GetDeviceMemoryType)

    @staticmethod
    def GetMemoryType():
        return _device.Device_GetMemoryType()
    GetMemoryType = _swig_new_static_method(_device.Device_GetMemoryType)

    @staticmethod
    def GetDeviceMemoryClass():
        return _device.Device_GetDeviceMemoryClass()
    GetDeviceMemoryClass = _swig_new_static_method(_device.Device_GetDeviceMemoryClass)

    @staticmethod
    def GetMemoryClass():
        return _device.Device_GetMemoryClass()
    GetMemoryClass = _swig_new_static_method(_device.Device_GetMemoryClass)

    @staticmethod
    def SetGPUAwareMPI(force=True):
        return _device.Device_SetGPUAwareMPI(force)
    SetGPUAwareMPI = _swig_new_static_method(_device.Device_SetGPUAwareMPI)

    @staticmethod
    def GetGPUAwareMPI():
        return _device.Device_GetGPUAwareMPI()
    GetGPUAwareMPI = _swig_new_static_method(_device.Device_GetGPUAwareMPI)

# Register Device in _device:
_device.Device_swigregister(Device)

def Device_IsConfigured():
    return _device.Device_IsConfigured()
Device_IsConfigured = _device.Device_IsConfigured

def Device_IsAvailable():
    return _device.Device_IsAvailable()
Device_IsAvailable = _device.Device_IsAvailable

def Device_IsEnabled():
    return _device.Device_IsEnabled()
Device_IsEnabled = _device.Device_IsEnabled

def Device_IsDisabled():
    return _device.Device_IsDisabled()
Device_IsDisabled = _device.Device_IsDisabled

def Device_Allows(b_mask):
    return _device.Device_Allows(b_mask)
Device_Allows = _device.Device_Allows

def Device_GetHostMemoryType():
    return _device.Device_GetHostMemoryType()
Device_GetHostMemoryType = _device.Device_GetHostMemoryType

def Device_GetHostMemoryClass():
    return _device.Device_GetHostMemoryClass()
Device_GetHostMemoryClass = _device.Device_GetHostMemoryClass

def Device_GetDeviceMemoryType():
    return _device.Device_GetDeviceMemoryType()
Device_GetDeviceMemoryType = _device.Device_GetDeviceMemoryType

def Device_GetMemoryType():
    return _device.Device_GetMemoryType()
Device_GetMemoryType = _device.Device_GetMemoryType

def Device_GetDeviceMemoryClass():
    return _device.Device_GetDeviceMemoryClass()
Device_GetDeviceMemoryClass = _device.Device_GetDeviceMemoryClass

def Device_GetMemoryClass():
    return _device.Device_GetMemoryClass()
Device_GetMemoryClass = _device.Device_GetMemoryClass

def Device_SetGPUAwareMPI(force=True):
    return _device.Device_SetGPUAwareMPI(force)
Device_SetGPUAwareMPI = _device.Device_SetGPUAwareMPI

def Device_GetGPUAwareMPI():
    return _device.Device_GetGPUAwareMPI()
Device_GetGPUAwareMPI = _device.Device_GetGPUAwareMPI



