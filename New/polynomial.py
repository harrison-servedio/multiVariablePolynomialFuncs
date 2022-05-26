from term import term

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
    return Polynomial(simplify(p1.terms + mult(p2, -1).terms))

def mult(p1, p2):
    terms = []
    if not isinstance(p2, Polynomial):
        p2 = Polynomial([[p2,{}]])
    if not isinstance(p1, Polynomial):
        p2 = Polynomial([[p1,{}]])
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


class Polynomial:
    def __init__(self, terms_input):
        # term object is composed of operator, coef, vars, degree
        self.terms = [term(t) for t in terms_input] if type(terms_input[0]) == list else terms_input
        self.simplify()
        self.sort()
        
        self.degree = self.terms[0].degree

    def simplify(self):
        self.terms = simplify(self.terms)
    def print(self):
        self.sort()
        outpolys = []
        for t in self.terms: # prettifying terms
            polystr = f'{t.operator} {abs(t.coef)}'
            for k, v in t.vars.items():
                polystr += f"{k}^{v}" if v != 1 else f"{k}"
            outpolys.append(polystr)
        
        if '+' in outpolys[0]: # delete leading '+'
            outpolys[0] = outpolys[0].replace('+ ', '') 
        
        print(' '.join(outpolys))

    def sort(self): # might want to tweak this/degree of terms
        self.terms = sorted(self.terms, key=lambda self: self.degree, reverse=True)

"""poly = Polynomial([[8, {'x': 2}], [4, {'x': 1}], [-5, {}]])
poly2 = Polynomial([[3, {'x': 2, 'y': 3}], [4, {'x': 1}], [-5, {}]])
multip = mult(poly2, poly)
multip.print()
#divid/divis"""

def single_div(dividend, divisor): #This is their leading terms
    # Divide coefs 
    coef = dividend.coef/divisor.coef
    # subtract exponents
    for variable, value in divisor.vars.items():
        if variable in dividend.vars.keys():
            dividend.vars[variable] -= value
        else:
            dividend.vars[variable] = -1 * value
    
    return term([coef, dividend.vars])

# a = term([10, {'x': }])
# b = term([1, {'x': 2}])
# Polynomial([single_div(a,b)]).print()
def div(dividend1, divisor1):
    dividend = dividend1.terms
    divisor = divisor1.terms
    answer = []

    while 1:
        # divide the leading term of the active dividend by the leading term of the divisor
        # recording that result to the answer
        answer.append(single_div(dividend[0], divisor[0]))
        # Multiply -1th term in the answer by the divisor
        result = mult(Polynomial([answer[-1]]), divisor1)
        # subtract the dividend by the result
        dividend = sub(Polynomial(dividend), result).terms
        # if we divide the leading term of the coefficient and the leading term of the divisor, if there is a negetive exponenet then the dividend is the remainder
        #3x^4y^5/x^5

        
a = Polynomial([[2, {'x':3}], [4, {'x': 2}], [5, {'x': 1}], [-1, {''}]])

b = Polynomial([[[1, {'x': 2}], [3, {'x': 1}]]])

div(a, b)