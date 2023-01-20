import sympy
from sympy import sympify
sympy.init_printing()
#All alphabets
(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sympy.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
Pi = sympy.S.Pi # 円周率
E = sympy.S.Exp1 # 自然対数の底
I = sympy.S.ImaginaryUnit # 虚数単位
eq = sympy.solve(((x + 2) * (x - 1) / ((x - 2) * (x - 2))), x)

print("\n[Integrate]", sympy.latex(eq), "\n")

string = "sympy.sin(x ** 5) / (E ** Pi)"
formula = sympify("x ** 6 + 2 * x ** 4 - 3 * x ** 2")
formula = sympify("1 / (x^(456))", convert_xor=True, evaluate=True)
#formula = sympify("((x-1) * (x ** 5 + x + 1)) / ((x - 2) ** 2)", convert_xor=True, evaluate=True)
print("[ String : ] ", string, "    |||   [ Latex : ]", sympy.latex(string))
print("[ Sympify : ] ", formula, "    |||   [ Latex : ]", sympy.latex(formula))

#  \lim_{start \to end}{formula}
start = "c"
end = r"\infty"
formula = r"\frac{1}{c}"
limit_tex = r"\lim_{{{0} \to {1}}}{{{2}}}".format(start, end, formula)
print(limit_tex)

F1 = x * x + 2 * x + 1 # 普通にシンボルを演算するだけ
F2 = x ** 5 + x + 1 # 高次式
F3 = (x + 2) * (x - 1) / ((x - 2) * (x - 2)) # 有理関数
F4 = sympy.cos(Pi * x) # 三角関数
F5 = E ** x / sympy.Pow(x, 10) # 指数関数とべき乗
F6 = sympy.log(x * x + 1) # 自然対数
F7 = (x + y) ** 3 # 2変数関数
F8 = (x + y + z / 2) ** 4 # 多変数関数

#pprint(sympy.latex((F1*F2*F3+F4)/(F5*F6/F7+F8)))