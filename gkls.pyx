# FFI for the GKLS library

from libcpp.vector cimport vector
from libcpp cimport bool
from libcpp.string cimport string

cdef extern from "include/gkls.hh":
  cdef cppclass CGKLS "GKLS":
    CGKLS(int dim, int num_minima, double domain_lo, double domain_hi, double global_dist, double global_radius, double global_min, string gen_str)

    CGKLS(int dim, int num_minima, double domain_lo, double domain_hi, double global_min, string gen_str)

    double get_d_func(vector[double] x);
    double get_d2_func(vector[double] x);
    double get_nd_func(vector[double] x);
    vector[double] get_d_gradient(vector[double] x);
    vector[double] get_d2_gradient(vector[double] x);
    vector[vector[double]] get_d2_hessian(vector[double] x);

cdef class GKLS:
  cdef CGKLS *thisptr
  def __cinit__(self, dim, num_minima, domain, global_min, global_dist=None, global_radius=None, gen=None):

    if gen is None:
      gen = "none"
    elif gen == "geometry":
      gen = "g"
    elif type(gen) is int:
      gen = "s" + str(gen % 1073741821)
    else:
      raise ValueError("gen must be one of None, 'geometry' or an integer.")

    gen_bytes = gen.encode("utf-8")
    if global_dist is None or global_radius is None:
      self.thisptr = new CGKLS(dim, num_minima, domain[0], domain[1], global_min, gen_bytes)
    else:
      self.thisptr = new CGKLS(dim, num_minima, domain[0], domain[1], global_dist, global_radius, global_min, gen_bytes)

  def get_d_f(self, x):
    return self.thisptr.get_d_func(x)
  
  def get_d2_f(self, x):
    return self.thisptr.get_d2_func(x)

  def get_nd_f(self, x):
    return self.thisptr.get_nd_func(x)

  def get_d_grad(self, x):
    return self.thisptr.get_d_gradient(x)

  def get_d2_grad(self, x):
    return self.thisptr.get_d2_gradient(x)

  def get_d2_hess(self, x):
    return self.thisptr.get_d2_hessian(x)
