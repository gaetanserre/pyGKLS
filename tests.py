import gkls

gkls.init()

x = [0.5, 0.5]

print(f"D_f = {gkls.get_d_f(x)}")
print(f"D2_f = {gkls.get_d2_f(x)}")
print(f"ND_f = {gkls.get_nd_f(x)}")

print(f"D_grad = {gkls.get_d_grad(x)}")
print(f"D2_grad = {gkls.get_d2_grad(x)}")

print(f"D2_hessian = {gkls.get_d2_hess(x)}")

gkls.free()
