# FFI for the GKLS library

from libcpp.vector cimport vector

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void set_default()

cdef extern from "include/wrapper.hh" namespace "GKLS":
  int generate(unsigned int nf)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void set_dim(unsigned int dim)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void set_num_minima(unsigned int num_minima)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void set_domain(double domain_lo, double domain_hi)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void set_global_dist(double global_dist)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void set_global_radius(double global_radius)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void set_global_value(double global_value)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  double get_d_func(vector[double] &x)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  double get_d2_func(vector[double] &x)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  double get_nd_func(vector[double] &x)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  vector[double] get_d_gradient(vector[double] &x)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  vector[double] get_d2_gradient(vector[double] &x)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  vector[vector[double]] get_d2_hessian(vector[double] &x)

cdef extern from "include/wrapper.hh" namespace "GKLS":
  double get_global_minimum()

cdef extern from "include/wrapper.hh" namespace "GKLS":
  void free_gkls()

# Python interface

def init(
  nf=1,
  dim=None,
  num_minima=None,
  domain_lo=None,
  domain_hi=None,
  global_dist=None,
  global_radius=None,
  global_value=None
  ):
    set_default()
    if dim is not None:
        set_dim(dim)
    if num_minima is not None:
        set_num_minima(num_minima)
    if domain_lo is not None and domain_hi is not None:
        set_domain(domain_lo, domain_hi)
    if global_dist is not None:
        set_global_dist(global_dist)
    if global_radius is not None:
        set_global_radius(global_radius)
    if global_value is not None:
        set_global_value(global_value)
    return generate(nf)

def get_d_f(x):
    return get_d_func(x)

def get_d2_f(x):
    return get_d2_func(x)

def get_nd_f(x):
    return get_nd_func(x)

def get_d_grad(x):
    return get_d_gradient(x)

def get_d2_grad(x):
    return get_d2_gradient(x)

def get_d2_hess(x):
    return get_d2_hessian(x)

def get_global_min():
    return get_global_minimum()

def free():
    free_gkls()