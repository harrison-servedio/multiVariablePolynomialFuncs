class polynomial:
    def __init__(self, coefs):
        '''
        coefs is a list of coeficients where the list position equals 
        '''
        self.degree = len(coefs) - 1
        self.coefs = [int(i) for i in ' '.join([str(i) for i in coefs]).lstrip('0 ').split(' ')]
    # arithmetic operators for polynomials
    
    def __add__(self, other):
        if not isinstance(other, polynomial):# Converts the other term to a polynomial if not already
            other = polynomial([other])
        biggerPoly = self.coefs if self.degree > other.degree else other.coefs
        smallerPoly = other.coefs if self.degree >= other.degree else self.coefs
        for i in range(len(biggerPoly) - len(smallerPoly)):
            smallerPoly.insert(0, 0)
        return polynomial([biggerPoly[i]+smallerPoly[i] for i in range(len(biggerPoly))])
            
            
    def __sub__(self, other):
        if self.degree == other.degree:
            return polynomial([self.coefs[i] - other.coefs[i] for i in range(self.degree + 1)])
        else:
            raise ValueError("Polynomials must have the same degree")
    def __mul__(self, other):
        print(self)
        print(other)
        """if self.degree != other.degree:
            if self.degree < other.degree:
                self.coefs = [0 for i in range(other.degree - other.degree)] + self.coefs
            else:
                other.coefs = [0 for i in range(self.degree - other.degree)] + other.coefs"""
        print(self)
        print(other)

        result = [0 for i in range(len(self.coefs) + len(other.coefs) - 1)]
        print(result)
        for i in range(len(self.coefs)):
            for j in range(len(other.coefs)):
                result[i+j] += self.coefs[i] * other.coefs[j]
        return polynomial(result)
    def __pow__(self, power):
        if power == 0:
            return polynomial([1])
        else:
            return self * (self ** (power - 1))
    def __str__(self):
        return str(self.coefs)
    def __repr__(self):
        return str(self.coefs)
    def __eq__(self, other):
        return self.coefs == other.coefs
    # function to divide two polynomials with polynomial long division algorithm
    def __truediv__(self, other):
        if self.degree < other.degree:
            return polynomial([0])
        else:
            quotient = polynomial([0])
            remainder = self
            while remainder.degree >= other.degree:
                quotient.coefs.insert(0, remainder.coefs[0]/other.coefs[0])
                remainder = remainder - other * quotient
            return quotient
    

# test cases for poly class
p1 = polynomial([3, 2, 0])
p2 = polynomial([1, 1, 2, 0])
p3 = polynomial([1, 2, 3, 4])
p4 = polynomial([1, 2, 3, 4])

print(p1 ** 3)
