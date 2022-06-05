import matplotlib.pyplot as plt
import polynomial as p

def plot_polynomial(poly, x_range):
    x = [i for i in range(x_range[0], x_range[1])]
    y = [poly.plugin({'x': i}) for i in x]
    plt.plot(x, y)
    plt.show()

plot_polynomial(p.Polynomial([[-1, {'x': 3}], [-5, {'x': 2}], [-3, {'x': 1}]]), (-10000, 10000))