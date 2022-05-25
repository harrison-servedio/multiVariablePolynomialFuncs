from operator import itemgetter
from term import term

def simplify(terms):
    simpler = {} # {vars as derived from t (term): [sum of coefficients, [term objects]]}
    for t in terms:

        # keys of dictionaries must be hashable so a dictionary can not be a key for a dictionary
        # this turns the vars for a term into a string so that they can be used as keys
        vars_items = list(dict(sorted(t.vars.items(), key=lambda item: item[0])).items()) 
        vars_key = ''
        for item in vars_items:
            vars_key += item[0] + str(item[1])
        
        
        if vars_key in simpler.keys(): # tally coefficients in dictionary simpler
            simpler[vars_key][0] += t.coefficient
            simpler[vars_key][1].append(t)
        else:
            simpler[vars_key] = [t.coefficient, [t]] # create dictionary entry of vars if vars is not in dicitonary

    for simple_term in simpler.values(): # reasign the compounded term values and delete excess terms
        if len(simple_term[1]) == 1:
            pass
        else:
            simple_term[1][0].coefficient = simple_term[0]
            for t in simple_term[1][1:]:
                terms.remove(t)
    return terms

def add(p1, p2):
    return Polynomial(simplify(p1.terms + p2.terms))

class Polynomial:
    def __init__(self, terms_input):
        # term object is composed of operator, coefficient, vars, degree
        self.terms = [term(t) for t in terms_input] if type(terms_input[0]) == list else terms_input
        self.simplify()
        self.sort()
        
        self.degree = self.terms[0].degree

    def simplify(self):
        simplify(self.terms)

    def print(self):
        self.sort()
        outpolys = []
        for t in self.terms: # prettifying terms
            polystr = f'{t.operator} {abs(t.coefficient)}'
            for k, v in t.vars.items():
                polystr += f"{k}^{v}"
            outpolys.append(polystr)
        
        if '+' in outpolys[0]: # delete leading '+'
            outpolys[0] = outpolys[0].replace('+ ', '') 
        
        print(' '.join(outpolys))

    def sort(self):
        self.terms = sorted(self.terms, key=lambda self: self.degree, reverse=True)

    def mul(self, p1, p2):
        # multiply two polynomials
        pass

    

poly = Polynomial([[3, {'x': 2}], [5, {'x': 2}], [4, {'x': 1}], [-5, {}]])
poly2 = Polynomial([[3, {'x': 2}], [5, {'x': 2}], [4, {'x': 1}], [-5, {}]])
added = add(poly2, poly)
added.print()