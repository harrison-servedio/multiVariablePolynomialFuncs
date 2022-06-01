
# term class

class term:

    # each term is of the following form:
    # t = [coefficient, {variable: exponent, variable, exponent}]
    # the term, [5, {x:5, y:4}] would be 5x^5y^4

    def __init__(self, term): 
        self.operator = '-' if term[0] < 0 else '+' # the operator determined by sign of term. only really used for displaying
        self.coef = term[0] # the coefficient is the first element of the term list
        self.vars = term[-1] # the dictionary of vars is term.vars, therefore we can access specific vars or exponents by using term.vars.keys()[] or term.vars.values()[]
        self.degree = sum(self.vars.values()) # the degree of on term is the sum of all exponents in a dictionary
    

