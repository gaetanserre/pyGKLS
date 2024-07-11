## pyGKLS

pyGKLS is a Python wrapper for the GKLS generator of global optimization test functions ([Giavano et al., 2003](https://dl.acm.org/doi/10.1145/962437.962444)). It uses the original C implementation of the generator and provides a Python interface using Cython to generate the test functions. pyGKLS also encompass a C++ wrapper around the original C implementation to provide a more user-friendly interface that can be used in C++ projects (see `pygkls/src/example.cc`).

### Random number generator
The original GKLS generator uses a random number generator based introduced by Knuth in his book "The Art of Computer Programming". pyGKLS uses the Mersenne Twister random number generator from the C++ standard library to generate random numbers.

### Installation
To install pyGKLS, one need `Python 3.12` or later, `CMake 3.28` or later, and a C++ compiler that supports C++20. One also need to have `python3-dev` installed. Then clone the repository and run the following commands:
```bash
./build_and_install.sh
```
This will build the C++ dynamic library and the Cython package. Then, it will copy the Cython package to the Python site-packages directory and the shared library to `$HOME/.local/lib`. Make sure that `LD_LIBRARY_PATH` (or `DYLD_LIBRARY_PATH` for macOS) includes `$HOME/.local/lib`.

### Usage
The Python interface is simple and easy to use. Here is an example of how to generate a GKLS function:
```python
import pygkls

pygkls.init()

x = [0.5, 0.5]

print(f"D_f = {pygkls.get_d_f(x)}")
print(f"D2_f = {pygkls.get_d2_f(x)}")
print(f"ND_f = {pygkls.get_nd_f(x)}")

print(f"D_grad = {pygkls.get_d_grad(x)}")
print(f"D2_grad = {pygkls.get_d2_grad(x)}")

print(f"D2_hessian = {pygkls.get_d2_hess(x)}")
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