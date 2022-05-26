class term:
    def __init__(self, term): # Terms is [coef, {variable1: degree, variable2: degree}
        self.operator = '-' if term[0] < 0 else '+'
        self.coef = term[0]
        self.vars = term[-1]
        self.degree = sum(term[-1].values())
        pass
