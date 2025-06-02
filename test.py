from gkls import GKLS

# Create an instance of the GKLS class with random generation (default)
print("Testing GKLS class with random generation:")

gkls = GKLS(2, 2, [-1, 1], -1)

x = [0.5, 0.5]

print(f"D_f = {gkls.get_d_f(x)}")
print(f"D2_f = {gkls.get_d2_f(x)}")
print(f"ND_f = {gkls.get_nd_f(x)}")

print(f"D_grad = {gkls.get_d_grad(x)}")
print(f"D2_grad = {gkls.get_d2_grad(x)}")

print(f"D2_hessian = {gkls.get_d2_hess(x)}")

# Create an instance of the GKLS class with generation from geometrical parameters
print("\nTesting GKLS class with geometrical parameters generation:")

gkls = GKLS(2, 2, [-1, 1], -1, gen="geometry")
x = [0.5, 0.5]

print(f"D_f = {gkls.get_d_f(x)}")
print(f"D2_f = {gkls.get_d2_f(x)}")
print(f"ND_f = {gkls.get_nd_f(x)}")

print(f"D_grad = {gkls.get_d_grad(x)}")
print(f"D2_grad = {gkls.get_d2_grad(x)}")

print(f"D2_hessian = {gkls.get_d2_hess(x)}")

# Create an instance of the GKLS class with deterministic generation
print("\nTesting GKLS class with deterministic generation:")

gkls = GKLS(2, 2, [-1, 1], -1, gen=42)
x = [0.5, 0.5]

print(f"D_f = {gkls.get_d_f(x)}")
print(f"D2_f = {gkls.get_d2_f(x)}")
print(f"ND_f = {gkls.get_nd_f(x)}")

print(f"D_grad = {gkls.get_d_grad(x)}")
print(f"D2_grad = {gkls.get_d2_grad(x)}")

print(f"D2_hessian = {gkls.get_d2_hess(x)}")
