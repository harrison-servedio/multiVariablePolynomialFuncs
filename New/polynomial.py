from operator import itemgetter
from term import term


class Polynomial:
    def __init__(self, terms_input):
        self.terms = [term(t) for t in terms_input] # term object is composed of operator, coefficient, vars, degree
        self.simplify()
        self.sort()
        
        self.degree = self.terms[0].degree

    def sort(self):
        self.terms = sorted(self.terms, key=lambda self: self.degree, reverse=True)

    def simplify(self):
        simpler = {} # {vars as derived from t (term): [sum of coefficients, [term objects]]}
        for t in self.terms:

            vars_items = list(dict(sorted(t.vars.items(), key=lambda item: item[0])).items())
            vars_key = ''
            for item in vars_items:
                vars_key += item[0] + str(item[1])
            
            
            if vars_key in simpler.keys():
                simpler[vars_key][0] += t.coefficient
                simpler[vars_key][1].append(t)
            else:
                simpler[vars_key] = [t.coefficient, [t]]

        for simple_term in simpler.values():
            if len(simple_term[1]) == 1:
                pass
            else:
                simple_term[1][0].coefficient = simple_term[0]
                for t in simple_term[1][1:]:
                    self.terms.remove(t)

    def mul(p1, p2):
        # multiply two polynomials
        pass

poly = Polynomial([[3, {'x': 2}], [5, {'x': 2}], [4, {'x': 1}], [-5, {}]])
print(poly.terms)