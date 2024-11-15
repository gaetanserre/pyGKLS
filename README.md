## pyGKLS

pyGKLS is a Python wrapper for the GKLS generator of global optimization test functions ([Giavano et al., 2003](https://dl.acm.org/doi/10.1145/962437.962444)). It uses the original C implementation of the generator and provides a Python interface using Cython to generate the test functions. pyGKLS also encompass a C++ wrapper around the original C implementation to provide a more user-friendly interface that can be used in C++ projects (see `src/example.cc`).

### Random number generator
The original GKLS generator uses a random number generator based introduced by Knuth in his book "The Art of Computer Programming". pyGKLS uses the Mersenne Twister random number generator from the C++ standard library to generate random numbers.

### Installation
To install pyGKLS, one need `Python 3.10` or later, `CMake 3.30` or later, and a C++ compiler that supports C++23. Then clone the repository and run the following commands:
```bash
pip install .
```
This will build the C++ dynamic library and the Cython package.


> [!WARNING]  
> To use pyGKLS in Jupyter notebooks, it seems that one needs to put the shared library (`libpygkls.{so|dylib}`) in the global library path (e.g. `/usr/lib`), or to create a symbolic link. One can also put the shared library in the same directory as the notebook.

### Usage
The Python interface is simple and easy to use. Here is an example of how to generate a GKLS function:
```python
import gkls

gkls.init()

x = [0.5, 0.5]

print(f"D_f = {gkls.get_d_f(x)}")
print(f"D2_f = {gkls.get_d2_f(x)}")
print(f"ND_f = {gkls.get_nd_f(x)}")

print(f"D_grad = {gkls.get_d_grad(x)}")
print(f"D2_grad = {gkls.get_d2_grad(x)}")

print(f"D2_hessian = {gkls.get_d2_hess(x)}")
```
Arguments can be passed to the `init` function to control the properties of the generated function. The `init` function has the following signature:
```python
def init(
  nf=1, # number of the function in the function class (1 <= nf <= 100)
  dim=None, # dimension of the function
  num_minima=None, # number of local minima
  domain_lo=None, # lower bound of the domain
  domain_hi=None, # upper bound of the domain
  global_dist=None, # distance from the paraboloid minimizer to the global minimizer
  global_radius=None, # radius of the global minimizer attraction region
  global_value=None # global minimum value
  )
```