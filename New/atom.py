
from re import sub


class atom:
    
    def __init__(self, letter, subscript=-1, power=1):                                              # Initializes atom class with require variables and defaults
        self.letter = letter                                                                        # Letter should be a single character
        self.subscript = subscript                                                                  # subscript should be an int
        self.power = power                                                                          # Power should be an int
    

    # These are pretty self explanitory - I'm also pretty sure these are not needed because you can do class.variable to get the variable and class.variable = x to set the class variables
    # def getLetter(self):
    #     return self.letter

    # def getSubscript(self):
    #     return self.subscript

    # def getPower(self):
    #     return self.power
    
    # def setLetter(self, letter):
    #     self.letter = letter
    
    # def setSubscript(self, subscript):
    #     self.subscript = subscript

    # def setPower(self, power):
    #     self.power = power

    # def setAtom(self, letter, subscript, power):
    #     self.letter = letter
    #     self.subscript = subscript
    #     self.power = power
    
    # This function presumably mutiplies two atoms by adding the exponent. It assumes that the subscripts and letters are the same as it is called time "like" atom
    def timesLikeAtom(self, atom):
        # For some reason doing "return atom(args)" did not work. There are better solutions but this one worked for some reason
        temp = atom
        temp.__init__(self.letter, self.subscript, self.power + atom.power)
        return temp

    # Returns true if the atoms are "like"
    def like(self, atom):   
        return self.letter == atom.letter and self.subscript == atom.subscript

    # Compares if two atoms are equal
    def equals(self, atom):
        return self.letter == atom.letter and self.subscript == atom.subscript and self.power == atom.power

    # Compares two atoms too see if the atoms is less or equal to the inputed atom
    def lessThanOrEqual(self, atom):
        if self.letter < atom.letter:                                                               # First checks if the letter itself is bigger
            return True
        elif self.letter == atom.letter:                                                            # If the leters are equal it first checks the subscripts to see if one is less
            if self.subscript < atom.subscript:
                return True
            elif self.subscript == atom.subscript and self.power < atom.power:                      # After checking the subscipts, if they are equal then it checks the powers
                return True
        return self.equals(atom)                                                                    # Kinda like a catch all - the previous code checks for less than and this just confirms if they are equal or not
        # It would have made more sense to use less than or equal too "<=" or ">=" instead of using the semi catch all at the lend

x = atom("a", power=0)
y = atom("a")

print(x.lessThanOrEqual(y))
