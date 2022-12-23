import sympy as sym
sym.init_printing()
(x, y, z) = sym.symbols('x y z')
Pi = sym.S.Pi # 円周率
E = sym.S.Exp1 # 自然対数の底
I = sym.S.ImaginaryUnit # 虚数単位
expr = sym.sin(x ** 5)/E ** Pi
eq = sym.Eq(sym.Integral(expr, x), sym.integrate(expr, x))

print("\n", sym.latex(eq), "\n")

F1 = x * x + 2 * x + 1 # 普通にシンボルを演算するだけ
F2 = x ** 5 + x + 1 # 高次式
F3 = (x + 2) * (x - 1) / ((x - 2) * (x - 2)) # 有理関数
F4 = sym.cos(Pi * x) # 三角関数
F5 = sym.exp(x) / sym.Pow(x, 10) # 指数関数とべき乗
F6 = sym.log(x * x + 1) # 対数関数
F7 = (x + y) ** 3 # 2変数関数
F8 = (x + y + z / 2) ** 4 # 多変数関数

print(sym.latex((F1*F2*F3+F4)/(F5*F6/F7+F8)))