"""
Remainder division test case:   
a = Polynomial([[2, {'x':3}], [4, {'x': 2}], [5, {'x': 1}], [-1, {}]])

b = Polynomial([[1, {'x': 2}], [-3, {'x': 1}]])

print(div(a, b, True))"""

"""
No remainder division test case:   
a = Polynomial([[1, {'x':4}], [-1, {'x': 3}], [-5, {'x': 2}], [-3, {'x': 1}]])

b = Polynomial([[1, {'x': 2}], [-3, {'x': 1}]])

print(div(a, b, True))"""

"""b = Polynomial([[1, {'x': 2}], [-3, {'x': 1}]])
print(b.plugin({'x': 3}))"""

# a = term([10, {'x': }])
# b = term([1, {'x': 2}])
# Polynomial([single_div(a,b)]).print()


import polynomial as p
a = p.Polynomial([[1, {'x':4}], [-1, {'x': 3}], [-5, {'x': 2}], [-3, {'x': 1}]])
print(a.terms)

b = p.Polynomial([[1, {'x': 2}], [-3, {'x': 1}]])

