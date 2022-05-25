from operator import itemgetter
from term import term


class Polynomial:
    def __init__(self, terms_input): # Terms is [coef, {variable1: degree, variable2: degree}
        self.terms = [term(t) for t in terms_input]
        self.degree = max([t.degree for t in self.terms])

    def sort(self):
        self.terms = sorted(self.terms, key=lambda self: self.terms.degree)
poly = Polynomial([[3, {'x': 2}], [4, {'x': 1}], [-5, {}]])

print(poly.degree)