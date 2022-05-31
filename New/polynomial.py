'''
Harrison, Abraham, Imran

Polynomial with Python

This package attempts to provide polynomial handling and functions. Functions are as follows:

Current Capabilities:
    Creating polynomial object
    Creating term object (polynomial object is multiple terms)
    Simplifying a polynomial
        Adding polynomials
        Subtracting polynomials
    Multiplying polynomials
    Dividing Polynomials

The polynomial data structure is comprised of a list of lists and dictionaries, as follows:
    [ [8, {'x': 2}], [4, {'x': 1}], [-5, {}] ]
    And equates to: 8x^2 + 4x - 5

The dictionary contains the variable(s) as the key, and the power to which the variable is raised 
as the value. Note that fractinal and negative exponents retain functionality. Note that one sublist is a term. 
Also note that many variables can be represented. For example:
    the term: 27x^3y
    can be represented by the term: [27, {'x':3, 'y': 1}]

Issues:
    * When the vars of a term are changed it's degree is not updated
    Need to add:
    Handling mult with one term

'''

from copy import deepcopy 
from term import term

class Polynomial: # the poynomial class

    '''
    a polynomial in math is comprised of multiple zero or nonzero terms. 
    in this case, our polynomial class will be a list of multiple term objects
    that it, it will read as follows:

    []
    '''


    def __init__(self, terms_input):
        # term object is composed of operator, coef, vars, degree
        if terms_input:
            self.terms = [term(t) for t in terms_input] if type(terms_input[0]) == list else terms_input
            self.sort()
            self.degree = self.terms[0].degree
        else:
            self.terms = []
            self.degree = 0
        

    def simplify(self):

        self.terms = simplify(self.terms)

    def print(self, return_=False):
        self.sort()
        outpolys = []
        for t in self.terms: # prettifying terms
            if t.degree:
                polystr = f'{t.operator} {abs(t.coef) if abs(t.coef) != 1 and len(t.vars) else ""}'
            else:
                polystr = f'{t.operator} {abs(t.coef)}'
            for k, v in t.vars.items():
                if v not in [1, 0]: 
                    polystr += f"{k}^{v}"
                elif v == 0:
                    polystr += "" 
                else:
                    polystr += f"{k}"
            outpolys.append(polystr)
        
        if '+' in outpolys[0]: # delete leading '+'
            outpolys[0] = outpolys[0].replace('+ ', '') 
        
        if return_:
            return ' '.join(outpolys) # if return_ arg is true, returned instead of printed

        print(' '.join(outpolys)) 
    
    def plugin(self, vars):
        return sum([t.coef*sum([vars[a]**t.vars[a] for a in t.vars.keys()]) for t in self.terms])
    
    def sort(self): # might want to tweak this/degree of terms
        self.terms = sorted(self.terms, key=lambda self: self.degree, reverse=True)

def simplify(terms):
    simpler = {} # {vars as derived from t (term): [sum of coefs, [term objects]]}
    for t in terms:
        # keys of dictionaries must be hashable so a dictionary can not be a key for a dictionary
        # this turns the vars for a term into a string so that they can be used as keys
        vars_items = list(dict(sorted(t.vars.items(), key=lambda item: item[0])).items()) 
        vars_key = ''
        for item in vars_items:
            vars_key += item[0] + str(item[1])

        if vars_key in simpler.keys(): # tally coefs in dictionary simpler
            simpler[vars_key][0] += t.coef
            simpler[vars_key][1].append(t)
        else:
            simpler[vars_key] = [t.coef, [t]] # create dictionary entry of vars if vars is not in dicitonary

    for simple_term in simpler.values(): # reasign the compounded term values and delete excess terms
        if len(simple_term[1]) != 1:
            simple_term[1][0].coef = simple_term[0]
            for t in simple_term[1][1:]:
                terms.remove(t)
            
    return terms

def add(p1, p2):
    return Polynomial(simplify(p1.terms + p2.terms))

def sub(p1, p2):
    negative = mult(p2, -1)
    equation = p1.terms + negative.terms
    return Polynomial(simplify(equation))

def mult(p1, p2):
    terms = []
    if not isinstance(p2, Polynomial):
        p2 = Polynomial([[p2,{}]])
    if not isinstance(p1, Polynomial):
        p1 = Polynomial([[p1,{}]])
    for n in p1.terms:
        for m in p2.terms:
            coef = n.coef * m.coef
            # merging vars dictionaries => a^(b+c) = a^b * a^c
            v = dict(n.vars) # reclassed because otherwise refrence is changed
            for key, value in m.vars.items():
                if key in v.keys():
                    v[key] += value
                else:
                    v[key] = value
            terms.append(term([coef, v])) 
    
    return Polynomial(simplify(terms))

def single_div(dividend1, divisor): #This is their leading terms
    dividend = deepcopy(dividend1)
    # Divide coefs 
    coef = dividend.coef/divisor.coef
    # subtract exponents
    for variable, value in divisor.vars.items():
        if variable in dividend.vars.keys():
            dividend.vars[variable] -= value
        else:
            dividend.vars[variable] = -1 * value
    
    return term([coef, dividend.vars])

def div(dividend1, divisor1, printed=False):
    dividend = dividend1.terms
    divisor = divisor1.terms
    answer = []
    break_ = False      
    while 1:
        dividend = [term for term in dividend if term.coef != 0]
        if dividend == []: # If the dividend is emptied the division is completed
            break
        # divide the leading term of the active dividend by the leading term of the divisor
        leading_div = single_div(dividend[0], divisor[0])
        # if we divide the leading term of the coefficient and the leading term of the divisor, if there is a negetive exponenet then the dividend is the remainder
        for power in list(leading_div.vars.values()):
            if not power + 1: # Handle zeros
                break_ = True
        if break_:
            break
        # recording that result to the answer
        answer.append(leading_div)
        # Multiply -1th term in the answer by the divisor
        result = mult(Polynomial([answer[-1]]), divisor1)
        # subtract the dividend by the result
        dividend = sub(Polynomial(dividend), result).terms
    
    if dividend:
        answer = [Polynomial(answer), [Polynomial(dividend), divisor1]]
        if printed: # If print argument is specified to be true than a formated answer is returned
            answer = f"{answer[0].print(True)} + ({answer[1][0].print(True)})/({answer[1][1].print(True)})"

    else:
        answer = [Polynomial(answer), []]
        if printed:
            answer = answer[0].print(True)
    
    return answer

def expo(poly, power):
    
    for i in range(power-1):
        poly = mult(poly, poly)
    
    return poly

def compose(*polyss): # args will be of Polynomial class
    polys = [t.terms for t in list(reversed(polyss))] + [[]]
    
    for index, poly1 in enumerate(polys[:-1]):
        Polynomial(simplify(polys[-1])).print()
        poly = Polynomial(poly1)
        for iterm, term in enumerate(polys[index]):

            # raise poly to the power of term
            try:
                powered = expo(poly, term.vars[list(term.vars.keys())[0]])
            except IndexError:
                powered = expo(poly, 0)
            # mult result by coef of term
            product = mult(powered, term.coef)
            # add term active polynomial
            try:
                del polys[index + 1][iterm] 
            except:
                pass
            polys[index + 1] += product.terms
        
    return Polynomial(simplify(polys[-1]))

a = Polynomial([[5, {'x':2}], [1,{}]])

b = Polynomial([[1, {'x': 2}], [1, {'x':1}], [-1, {'x':0}]])

composed = compose(a, b)
composed.print()