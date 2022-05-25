import parser
from math import sin

formula = "sin(x)*x**2"
code = parser.expr(formula).compile()
print([i for i in code])