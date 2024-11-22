## pyGKLS

pyGKLS is a Python wrapper for the GKLS generator of global optimization test functions ([Giavano et al., 2003](https://dl.acm.org/doi/10.1145/962437.962444)). It uses the original C implementation of the generator and provides a Python interface using Cython to generate the test functions. pyGKLS encompass a C++ class that wraps the original C implementation to provide a more user-friendly interface that can be used in C++ projects (see `src/example.cc`) or Python projects (see `test.py`).

### Random number generator
The original GKLS generator uses a random number generator based introduced by Knuth in his book "The Art of Computer Programming". pyGKLS uses the Mersenne Twister random number generator from the C++ standard library to generate random numbers.

### Installation
To install pyGKLS, one need `Python 3.10` or later, `CMake 3.30` or later, and a C++ compiler that supports C++23. Then clone the repository and run the following commands:
```bash
pip install .
```
This will build the C++ dynamic library and the Cython package.

### Usage
The Python interface is simple and easy to use. Here is an example of how to generate a GKLS function:
```python
from gkls import GKLS

# Create an instance of the GKLS class
gkls = GKLS(2, 2, [-1, 1], -1, deterministic=True)

x = [0.5, 0.5]

print(f"D_f = {gkls.get_d_f(x)}")
print(f"D2_f = {gkls.get_d2_f(x)}")
print(f"ND_f = {gkls.get_nd_f(x)}")

print(f"D_grad = {gkls.get_d_grad(x)}")
print(f"D2_grad = {gkls.get_d2_grad(x)}")

print(f"D2_hessian = {gkls.get_d2_hess(x)}")
```
The output of the above code is:
```
D_f = 1.5100378326790798
D2_f = 1.5100378326790798
ND_f = 1.5100378326790798
D_grad = [2.3881468199540072, -0.5804361265978222]
D2_grad = [2.3881468199540072, -0.5804361265978222]
D2_hessian = [[2.0, 0.0], [0.0, 2.0]]
```

Arguments can be passed to the `GKLS` constructor function to control the properties of the generated function. The constructor has the following signature:
```python
GKLS(
  dim : int, # dimension of the function
  num_minima : int, # number of local minima
  domain : List[float], # domain of the function (i.e. [domain_low, domain_high])
  global_value : float # global minimum value
  global_dist=None : float, # distance from the paraboloid minimizer to the global minimizer
  global_radius=None : float, # radius of the global minimizer attraction region
  deterministic=False : bool, # if True, the generation of the function is deterministic
)
```