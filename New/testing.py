import polynomial as ply

a = ply.Polynomial([[-1, {'x':3}], [-8, {}]])
# -x^3 - 8
print(ply.definite_integral(a, 10, 20))
# this result is accurate


