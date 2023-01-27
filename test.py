import sympy
from sympy import sympify
sympy.init_printing()

string = sympify("arctan(x**β) / (e / (tan(x)))", convert_xor=True, evaluate=True)
formula = sympify("x ** 456 + 2 * x ** 4 - 3 * x ** 2")
#formula = sympify("j^{2} + 45*k^{12} - l", convert_xor=True, evaluate=True)
#formula = sympify("((x-1) * (x ** 5 + x + 1)) / ((x - 2) ** 2)", convert_xor=True, evaluate=True)
print("[ String : ] ", string, "    |||   [ Latex : ]", sympy.latex(string))
print("[ Sympify : ] ", formula, "    |||   [ Latex : ]", sympy.latex(formula))
