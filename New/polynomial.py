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
    Polynomial expected in the form: [[term], [term]] where term is [coef, {var:exponent}]
    '''

    '''
    a polynomial in math is comprised of multiple zero or nonzero terms. 
    in this case, our polynomial class will be a list of multiple term objects
    that it, it will be as follows:
        [<term.term object at 0x0000013551D8E100>, <term.term object at 0x0000013551D8EB50>]
    where each of these term objects is: [coef, {var:exponent}]
    So, we can represent, for example 5x^3 + 3x^2 - 4x + 12 as:
        [[5, {'x':3}], [3 {'x':2}], [-4 {'x':1}], [12, {}]]    
    '''


    def __init__(self, terms_input=False): 
        # the input will be a list of term objects composed of operator, coef, vars, degree
        if terms_input: # if there is an input
            self.terms = [term(t) for t in terms_input] if type(terms_input[0]) == list else terms_input
            self.sort()
            self.elim_empty_vars()
            self.degree = self.terms[0].degree
        else: # if false
            self.terms = [term([0,{}])] # value of the polynomial is set to 0
            self.degree = 0 # the degree is set to 0  as well
    
    # Prints the polynomial when the class is requested as a string
    def __str__(self) -> str:
        return self.print(return_=True)

    def simplify(self): # we can simplify the terms using the simplify function that is defined later

        self.terms = simplify(self.terms) # once, again, defined later. 

    # Function to add term to self.terms
    def add_term(self, term):
        self.terms.append(term)
    def print(self, return_=False): 
        '''
        printing the polynomial nicely. for example, will display:
            [[5, {'x':3}], [3 {'x':2}], [-4 {'x':1}], [12, {'x':0}]]
        in a more readable fashion as:
            5x^3 + 3x^2 - 4x + 12
        '''

        self.sort() # we will sort the polynomial. this method is defined later in the class
        outpolys = [] # a blank list for our inevitable output
        for t in self.terms: # we will now go through and make each term into a readble string
            if t.degree: 
                polystr = f'{t.operator} {abs(t.coef) if abs(t.coef) != 1 and len(t.vars) else ""}' # displauuing the coefficient
            else:
                polystr = f'{t.operator} {abs(t.coef)}' # displaying coefficient
            for k, v in t.vars.items(): # displauing variables
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

        print(' '.join(outpolys)) # otherwise, print the string representation of the polynomial
    
    def list_vars(self):
        '''
        lists all unique vairbales present in Polynomial Object
        '''        
        
        # we will attempt to list out all unique variables used in the polynomial
        unique_variables = [] # a list of all unique variables in the polynomial object
        for term in self.terms: # we shal look through all of the terms in the polynomial
            for variable in list(term.vars.keys()): # we look through potentially multiple variables
                if variable not in unique_variables: # if the variable has not been seen before
                    unique_variables.append(variable) # we add it to a list of all of unique variables
        
        return unique_variables # w return the list of all unique variables

    def elim_empty_vars(self):
        '''
        TAKES: nothing
        RETURNS: Nothing, modifies polynomial object

        take the following polynomial:
            [[5, {'x':3}], [3 {'x':2}], [-4 {'x':1}], [12, {}]]
        Specifically, notice how the final term, [12, {}] has an empty variable dictionary
        this causes issues when solving because it is evaluated to 0 and therefore, a potentially important constant is evaluated as 0
        We shall fix this by replacing the empty dictionary with a filled dictionary of degree 0
        '''
        for term in self.terms: # we parse through each term of the polynomial
            if len(term.vars) == 0: # if the variable dictionary is empty
                for variable in self.list_vars(): # then well go through all possible variables
                    term.vars[variable] = 0 # and set the power to 0

    def plugin(self, vars): 
        '''
        TAKES: VARIABLE OF FORM {'x':value} 
        RETURNS: Integer

        it is important to plug in values into a polynomial
        expected input is a dict containing variable(s) and the value we want to be inputed
        for example, input for f(x) would be {'x':value} and input for f(x,y) woudl be {'x':value, 'y':value}
        '''
        self.elim_empty_vars() # we first make sure that there are no empty variables. see documentation for this specific funciton to udnerstadn why this step is important
        return sum([t.coef*sum([vars[a]**t.vars[a] for a in t.vars.keys()]) for t in self.terms]) # then we go through each term and each variable in the term, and simply perform arithmetic with the desired value
  
    def sort(self): 
        # NOTE : might want to tweak this/degree of terms
        # otherwise, this simply sorts all of the terms by highest degree to lowest degree
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
    '''
    TAKES: Two Polynomial objects
    RETURNS: One Polynomial object 
    We will add two polynomials together
    '''
    if not isinstance(p2, Polynomial): # just in case p2 is integer, make it Polynomial Object
        p2 = Polynomial([[p2,{}]])
    if not isinstance(p1, Polynomial): # likewise, in case p1 is inteher
        p1 = Polynomial([[p1,{}]])
    return Polynomial(simplify(p1.terms + p2.terms)) 

def sub(p1, p2):
    '''
    TAKES: Two Polynomial objects
    RETURNS: One Polynomial object 
    We will subtract two polynomials. P2 is subtracted from P1
    '''
    if not isinstance(p2, Polynomial): # just in case p2 is integer, make it Polynomial Object
        p2 = Polynomial([[p2,{}]])
    if not isinstance(p1, Polynomial): # likewise, in case p1 is inteher
        p1 = Polynomial([[p1,{}]])
    negative = mult(p2, -1) 
    equation = p1.terms + negative.terms
    return Polynomial(simplify(equation))

def mult(p1, p2):
    '''
    TAKES: Two polynomial objects or integers
    RETURNS: One Polynomial Object
    we will multiply two polynomials
    '''
    terms = [] # a blank holder list 
    if not isinstance(p2, Polynomial): # just in case p2 is integer, make it Polynomial Object
        p2 = Polynomial([[p2,{}]])
    if not isinstance(p1, Polynomial): # likewise, in case p1 is inteher
        p1 = Polynomial([[p1,{}]])
    for n in p1.terms: # we iterate through each term
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
    '''
    TAKES: Two Polynomial objects, bool printed
    RETURNS: One Polynomial object 
    We will devide two polynomials if printed is false. dividend1 is devided by divisor1
    If printed is true it will return the polynomial as a string
    '''
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
    
    '''
    this function will raise a polynomial to a given power
    '''

    if power == 0: # we want to return 1
        # however, rather than just returning 1 with an empty var list, I will return it with the variables of the original polynomial
        uniques = poly.list_vars() # generate all of the vairables from arg poly
        p = Polynomial([[1, {}]]) # polynomial with 1 and empty vars
        for var in uniques: # going through
            p.terms[0].vars[var] = 0 # setting unique vars to power 0 
        return p # will end up returning something like [[1, {'x':0, 'y':0}]]

    for i in range(power-1): # we will exponent
        poly = mult(poly, poly) # we multipluy
    
    return poly # we rteeun raised polynomial

def compose(*polyss): # args will be of Polynomial class
    polys = [t.terms for t in list(reversed(polyss))] # ordering the list of polynomials that we will compose

    active = polys.pop(0) # Active is what will be plugged into the next term
    
    for func in polys: # we go through through each polynomial. func is a Polynomial object
        result = [] # an empty result list 
        for t in func: # for each term in the Polynomial Object
            if t.vars: # if there is a variable
                result += mult(t.coef, expo(Polynomial(active), list(t.vars.values())[0])).terms # we will add the correct polynomial
            else:
                result.append(t) # if no variable just append the term

        active = result # we keep going 

    return Polynomial(simplify(active)) # return
    
def riemann(poly, lbound, ubound, steps = 100000):
    
    '''
    this function will attempt to obtain a riemann sum to approximate the are under a curve
    the curve will be the polynomial passed as an argument. the left bound of the riemann sum will be passed via lbound
    and the upper bound of the riemann sum will be passed via the ubound argument
    the number of steps that the riemann sum will undergo will be given in the 'steps' argument, which defaults to 1 billion steps

    this riemann sum function will use trapezoidal approximation, and not right or left rectangles because i dont want to  
    also this is only for single variable, 2d functions because i said so  
    '''

    if len(poly.list_vars()) == 1: # ONLY SINGLE VARIABLE REIMANN SUM

        sum = 0 # cumulative sum of trapezoids set at 0

        var = list(poly.terms[0].vars.keys())[0] # we see the unique variable
        increment = (ubound-lbound)/steps # we set the incremement

        current_step = lbound # the starting step is the lower bound
        while current_step < ubound: # originally i made a for loop then changed to while bc increment cant be below 1
            l_sln = poly.plugin({var: current_step}) # the lower y value
            u_sln = poly.plugin({var: current_step+increment}) # the upper y value

            a = increment * (l_sln + u_sln)/2 # the area of the trapezoid
            sum += a # add the area to the sum
            current_step += increment # we increment more
        
        return sum # return the sum

def derive(polynomial):
    '''
    we will take the derivate of the polynomial.
    because this is for polynomials, the algorithm is actually rather simple. 
    the constraint here is that it will only work for single variabled functions
    expected input is a Polynomial `
    '''

    tpoly = polynomial # we dont want to modfy the original polynomial argument, so we'll use a temporary and return it

    if len(tpoly.list_vars()) == 1: # only single variable functions
    
        for term in tpoly.terms: # for each term in the polynomial
            if term.degree != 0: # if the degree is a nonzero numnber
                term.coef = term.coef * term.degree # we multiply the coef by the degree
                (term.vars)[tpoly.list_vars()[0]] -= 1  # and we decrease the degree by 1
            elif term.degree == 0: # if the degree is 0
                term.coef = 0 # the coefficient becomes 0
                term.vars = {tpoly.list_vars()[0]: 0} # rather than subtracting 1, we keep it at 0

        tpoly.simplify() # we simplify the polynomial
        return tpoly

    else: # otherwise, if the polynomial has more than one variable
        raise ValueError('Expected polynomial with one variable')

def aderive(polynomial, new=True):
    '''
    here we will take the antiderivate of the input polynomial
    As with the derive function, this is also pretty simple, becaue it is just a polynomial
    HOWEVER HOWEVER, THERE ARE STILL REALLY IMPORTANT CONSTRAINTS:
        antiderivate of x^-1 is ln(x) but thats beyond the scope of this
        only single variable functions
    Expected input is a polynomial object
    '''
    tpoly = polynomial # we dont want to modfy the original polynomial argument, so we'll use a temporary and return it

    if len(tpoly.list_vars()) == 1: # only works with a single variable polynomial

        var = tpoly.list_vars()[0] # the specific variable. we can do this because we know for a fact there is only one variable present

        for term in tpoly.terms: # we iterate through each term
            if term.degree == -1: # no ln(x)
                raise ValueError("Contains term with degree -1, expected polynomial with no degrees of -1") # ln(X) is supported. 
            else: # otherwise, if the term is valid
                (term.vars)[var] += 1 # we increase the power by one
                term.coef = term.coef / term.degree # we also fix the coefficient

        tpoly.simplify() # simplify the polynomial
        return tpoly

    else: # if the variable has more than one variable
        raise ValueError("Expected single variable polynomial")

def slope_at_point(polynomial, point):
    '''
    TAKES: a polynomial object and a integer value as point
    RETURN: a numberical sloe
    
    we will simply use the derive function to find the slope at a point
    '''
    
    if len(polynomial.list_vars()) == 1: # only single variable functions

        var = polynomial.list_vars()[0] # the specific variable. we can do this because we know for a fact there is only one variable present
        derivative = derive(polynomial) # derivate of the polynomial argument
        return derivative.plugin({var: point}) # we return the numeric value of the derivate at the point

    else:
        raise ValueError("Expected polynomial with one unique variable")

def tangent_line_equation(polynomial, point):
    '''
    TAKES: a SINGLE VARIABLE polynomial object and an integer
    RETURNS: a polynomial object of degree 1 that represents the polynomial 
    
    
    '''
    if len(polynomial.list_vars()) == 1:
        var = polynomial.list_vars()[0] # the specific variable. we can do this because we know for a fact there is only one variable present
        yval = polynomial.plugin({var:point}) # the y value of the function
        slope = slope_at_point()


    else:
        raise ValueError("Expected polynomial with one variable")




# Function to multiply two polynomials
def mult(poly1, poly2):
    '''
    TAKES: two polynomial objects
    RETURNS: a polynomial object that is the product of the two input polynomials
    '''
    if len(poly1.list_vars()) == 1 and len(poly2.list_vars()) == 1: # only single variable functions
        result = Polynomial([]) # initialize the result
        for term1 in poly1.terms: # for each term in the first polynomial
            for term2 in poly2.terms: # for each term in the second polynomial
                result.terms.append(term1 * term2) # we add the product of the two terms to the result
        result.simplify() # simplify the result
        return result # return the result
    else:
        raise ValueError("Expected polynomial with one unique variable")
