
class term:
    def __init__(self, term): # Terms is [coef, [[variable1, degree], [variable2, degree]]]
        self.operator = -1 if term[0] < 0 else 1
        self.coefficient = term[0]
        self.vars = term[-1]
        pass

