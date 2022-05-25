from term import term


class Polynomial:
    def __init__(self, terms): # Terms is [coef, {variable1: degree, variable2: degree}
        self.terms = [term(t) for t in terms]
        self.degree = sum([t.degree for t in self.terms])

poly = Polynomial([[3, {'x': 2}], [4, {'x': 1}], [-5, {}]])
print(poly.degree)