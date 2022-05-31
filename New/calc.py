class term:
    def __init__(self, term): # Terms is [coef, {variable1: degree, variable2: degree}
        self.operator = '-' if term[0] < 0 else '+'
        self.coef = term[0]
        self.vars = term[-1]
        self.degree = sum(self.vars.values())

class Polynomial:
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
    
    def unique_vars(self):
        h = []
        for t in self.terms:
            for var in list(t.vars.keys()):
                if var not in h:
                    h.append(var)
        return h

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

def riemann(poly, lbound, ubound, steps = 10):
    
    '''
    this function will attempt to obtain a riemann sum to approximate the are under a curve
    the curve will be the polynomial passed as an argument. the left bound of the riemann sum will be passed via lbound
    and the upper bound of the riemann sum will be passed via the ubound argument
    the number of steps that the riemann sum will undergo will be given in the 'steps' argument, which defaults to 1 billion steps

    this riemann sum function will use trapezoidal approximation, and not right or left rectangles because i dont want to  
    also this is only for single variable, 2d functions because i said so  
    '''

    if len(poly.unique_vars()) == 1: # ONLY SINGLE VARIABLE REIMANN SUM

        sum = 0 # cumulative sum of trapezoids set at 0

        var = list(poly.terms[0].vars.keys())[0]
        increment = (ubound-lbound)/steps

        current_step = lbound
        while current_step < ubound: # originally i made a for loop as follows: for lb
            l_sln = poly.plugin({var: current_step})
            u_sln = poly.plugin({var: current_step+increment})

            a = increment * (l_sln + u_sln)/2
            print(f"{l_sln}, {u_sln}, {a}")
            sum += a
            current_step += increment
        
        return sum

a = Polynomial([[1, {'x':3}], [-8, {}]])
print(a.plugin({"x":1.5}))
a.print()
print(riemann(a, 0, 2))