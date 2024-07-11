import pygkls

pygkls.init()

x = [0.5, 0.5]

print(f"D_f = {pygkls.get_d_f(x)}")
print(f"D2_f = {pygkls.get_d2_f(x)}")
print(f"ND_f = {pygkls.get_nd_f(x)}")

print(f"D_grad = {pygkls.get_d_grad(x)}")
print(f"D2_grad = {pygkls.get_d2_grad(x)}")

print(f"D2_hessian = {pygkls.get_d2_hess(x)}")

pygkls.free()
