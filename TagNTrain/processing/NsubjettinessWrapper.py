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
    from . import _NsubjettinessWrapper
else:
    import _NsubjettinessWrapper

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

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


import collections.abc
class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _NsubjettinessWrapper.delete_SwigPyIterator

    def value(self):
        return _NsubjettinessWrapper.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _NsubjettinessWrapper.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _NsubjettinessWrapper.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _NsubjettinessWrapper.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _NsubjettinessWrapper.SwigPyIterator_equal(self, x)

    def copy(self):
        return _NsubjettinessWrapper.SwigPyIterator_copy(self)

    def next(self):
        return _NsubjettinessWrapper.SwigPyIterator_next(self)

    def __next__(self):
        return _NsubjettinessWrapper.SwigPyIterator___next__(self)

    def previous(self):
        return _NsubjettinessWrapper.SwigPyIterator_previous(self)

    def advance(self, n):
        return _NsubjettinessWrapper.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _NsubjettinessWrapper.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _NsubjettinessWrapper.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _NsubjettinessWrapper.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _NsubjettinessWrapper.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _NsubjettinessWrapper.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _NsubjettinessWrapper.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _NsubjettinessWrapper:
_NsubjettinessWrapper.SwigPyIterator_swigregister(SwigPyIterator)

class vectord(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _NsubjettinessWrapper.vectord_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _NsubjettinessWrapper.vectord___nonzero__(self)

    def __bool__(self):
        return _NsubjettinessWrapper.vectord___bool__(self)

    def __len__(self):
        return _NsubjettinessWrapper.vectord___len__(self)

    def __getslice__(self, i, j):
        return _NsubjettinessWrapper.vectord___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _NsubjettinessWrapper.vectord___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _NsubjettinessWrapper.vectord___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _NsubjettinessWrapper.vectord___delitem__(self, *args)

    def __getitem__(self, *args):
        return _NsubjettinessWrapper.vectord___getitem__(self, *args)

    def __setitem__(self, *args):
        return _NsubjettinessWrapper.vectord___setitem__(self, *args)

    def pop(self):
        return _NsubjettinessWrapper.vectord_pop(self)

    def append(self, x):
        return _NsubjettinessWrapper.vectord_append(self, x)

    def empty(self):
        return _NsubjettinessWrapper.vectord_empty(self)

    def size(self):
        return _NsubjettinessWrapper.vectord_size(self)

    def swap(self, v):
        return _NsubjettinessWrapper.vectord_swap(self, v)

    def begin(self):
        return _NsubjettinessWrapper.vectord_begin(self)

    def end(self):
        return _NsubjettinessWrapper.vectord_end(self)

    def rbegin(self):
        return _NsubjettinessWrapper.vectord_rbegin(self)

    def rend(self):
        return _NsubjettinessWrapper.vectord_rend(self)

    def clear(self):
        return _NsubjettinessWrapper.vectord_clear(self)

    def get_allocator(self):
        return _NsubjettinessWrapper.vectord_get_allocator(self)

    def pop_back(self):
        return _NsubjettinessWrapper.vectord_pop_back(self)

    def erase(self, *args):
        return _NsubjettinessWrapper.vectord_erase(self, *args)

    def __init__(self, *args):
        _NsubjettinessWrapper.vectord_swiginit(self, _NsubjettinessWrapper.new_vectord(*args))

    def push_back(self, x):
        return _NsubjettinessWrapper.vectord_push_back(self, x)

    def front(self):
        return _NsubjettinessWrapper.vectord_front(self)

    def back(self):
        return _NsubjettinessWrapper.vectord_back(self)

    def assign(self, n, x):
        return _NsubjettinessWrapper.vectord_assign(self, n, x)

    def resize(self, *args):
        return _NsubjettinessWrapper.vectord_resize(self, *args)

    def insert(self, *args):
        return _NsubjettinessWrapper.vectord_insert(self, *args)

    def reserve(self, n):
        return _NsubjettinessWrapper.vectord_reserve(self, n)

    def capacity(self):
        return _NsubjettinessWrapper.vectord_capacity(self)
    __swig_destroy__ = _NsubjettinessWrapper.delete_vectord

# Register vectord in _NsubjettinessWrapper:
_NsubjettinessWrapper.vectord_swigregister(vectord)

class Nsubjettiness(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _NsubjettinessWrapper.Nsubjettiness_swiginit(self, _NsubjettinessWrapper.new_Nsubjettiness(*args))

    def getTau(self, maxTau, particles):
        return _NsubjettinessWrapper.Nsubjettiness_getTau(self, maxTau, particles)
    NormalizedMeasure = _NsubjettinessWrapper.Nsubjettiness_NormalizedMeasure
    UnnormalizedMeasure = _NsubjettinessWrapper.Nsubjettiness_UnnormalizedMeasure
    OriginalGeometricMeasure = _NsubjettinessWrapper.Nsubjettiness_OriginalGeometricMeasure
    NormalizedCutoffMeasure = _NsubjettinessWrapper.Nsubjettiness_NormalizedCutoffMeasure
    UnnormalizedCutoffMeasure = _NsubjettinessWrapper.Nsubjettiness_UnnormalizedCutoffMeasure
    GeometricCutoffMeasure = _NsubjettinessWrapper.Nsubjettiness_GeometricCutoffMeasure
    N_MEASURE_DEFINITIONS = _NsubjettinessWrapper.Nsubjettiness_N_MEASURE_DEFINITIONS
    KT_Axes = _NsubjettinessWrapper.Nsubjettiness_KT_Axes
    CA_Axes = _NsubjettinessWrapper.Nsubjettiness_CA_Axes
    AntiKT_Axes = _NsubjettinessWrapper.Nsubjettiness_AntiKT_Axes
    WTA_KT_Axes = _NsubjettinessWrapper.Nsubjettiness_WTA_KT_Axes
    WTA_CA_Axes = _NsubjettinessWrapper.Nsubjettiness_WTA_CA_Axes
    Manual_Axes = _NsubjettinessWrapper.Nsubjettiness_Manual_Axes
    OnePass_KT_Axes = _NsubjettinessWrapper.Nsubjettiness_OnePass_KT_Axes
    OnePass_CA_Axes = _NsubjettinessWrapper.Nsubjettiness_OnePass_CA_Axes
    OnePass_AntiKT_Axes = _NsubjettinessWrapper.Nsubjettiness_OnePass_AntiKT_Axes
    OnePass_WTA_KT_Axes = _NsubjettinessWrapper.Nsubjettiness_OnePass_WTA_KT_Axes
    OnePass_WTA_CA_Axes = _NsubjettinessWrapper.Nsubjettiness_OnePass_WTA_CA_Axes
    OnePass_Manual_Axes = _NsubjettinessWrapper.Nsubjettiness_OnePass_Manual_Axes
    MultiPass_Axes = _NsubjettinessWrapper.Nsubjettiness_MultiPass_Axes
    N_AXES_DEFINITIONS = _NsubjettinessWrapper.Nsubjettiness_N_AXES_DEFINITIONS
    __swig_destroy__ = _NsubjettinessWrapper.delete_Nsubjettiness

# Register Nsubjettiness in _NsubjettinessWrapper:
_NsubjettinessWrapper.Nsubjettiness_swigregister(Nsubjettiness)



