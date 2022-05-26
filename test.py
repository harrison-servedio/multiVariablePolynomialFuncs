import numpy as np
x = np.array([2.0, 4.0, 5.0,-1])
y = np.array([1.0, -3.0])
a, b = np.polydiv(x, y)
print(np.polydiv(a, b))

# (array([0.01923077, 0.09615385, 0.33653846]), array([0.]))
