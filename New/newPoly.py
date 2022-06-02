class polynomial:
    def __init__(self, coefs):
        '''
        coefs is a list of coeficients where the list position equals 
        '''
        
        self.coefs = coefs
        self.delete_zeros()
        self.degree = len(coefs) - 1
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
        # add leading zeros to other to make it the same length as self
        if len(self.coefs) > len(other.coefs):
            for i in range(len(self.coefs) - len(other.coefs)):
                other.coefs.insert(0, 0)
        elif len(self.coefs) < len(other.coefs):
            for i in range(len(other.coefs) - len(self.coefs)):
                self.coefs.insert(0, 0)
        return polynomial([self.coefs[i] - other.coefs[i] for i in range(len(self.coefs))])
    def __mul__(self, other):
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
    def __ne__(self, other):
        return not self == other
    # function to divide a polynomial by a constant
    def __truediv__(self, remainder):
        result = []
        while remainder.degree < self.degree:
            result.append(self.coefs[0] / remainder.coefs[0])
            remainder = remainder - self * polynomial([result[-1]])

        return polynomial(result), remainder, self

    # function to find the remainder of two polynomials with polynomial long division algorithm
    def __mod__(self, other):
        if self.degree < other.degree:
            return self
        else:
            remainder = self
            while remainder.degree >= other.degree:
                remainder = remainder - other * (remainder / other)
            return remainder
    
    def plugin(self, x):
        return sum([self.coefs[i] * x**i for i in range(len(self.coefs))])
    
    # function to delete the leading zeros in the polynomial
    def delete_zeros(self):
        if self.coefs != []:
            while self.coefs[0] == 0:
                self.coefs.pop(0)
                self.degree -= 1
    

# test cases for poly class
p1 = polynomial([3, 2, 0])
p2 = polynomial([1, 1, 2, 0])
p3 = polynomial([1, 2, 3, 4])
p4 = polynomial([1, 2, 3, 4])

print(p2/p1)
