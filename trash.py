import sympy
from static.layout import *

sympy.init_printing()

#微分
y = sympy.E ** x
Dy = sympy.Derivative(y, x).doit()
print(sympy.latex(Dy))
#e^{x}

#微分係数
y = x**2-2*x+2
Dfy = sympy.diff(y, x).subs(x,2)
print(Dfy)
#2

#不定積分
y = 1 / (sympy.sin(x) + sympy.cos(x) + 1)  # type: ignore
Iy = sympy.integrate(y, x)
print(sympy.latex(Iy))
#\log{\left(\tan{\left(\frac{x}{2} \right)} + 1 \right)}

#定積分
y = x**2
DIy = sympy.integrate(y, (x, 0, 1))
print(DIy)
#1/3

F10 = 2*x + 2*y + 6*z + 3
F11 =   x +   y - 2*z - 7
F12 = 5*x - 9*y + 2*z - 15
print(sympy.solve([F10, F11, F12], [x, y, z]), "\n")

F1 = x * x + 2 * x + 1 # 普通にシンボルを演算するだけ
F2 = x ** 5 + x + 1 # 高次式
F3 = (x + 2) * (x - 1) / ((x - 2) * (x - 2)) # 有理関数
F4 = sympy.cos(Pi * x) # 三角関数
F5 = sympy.exp(x) / sympy.Pow(x, 10) # 指数関数とべき乗
F6 = sympy.log(x * x + 1) # 対数関数
F7 = (x + y) ** 3 # 2変数関数
F8 = (x + y + z / 2) ** 4 # 多変数関数

print(sympy.latex((F1*F2*F3+F4)/(F5*F6/F7+F8)))

F10 = 2*x + 2*y + 6*z + 3
F11 =   x +   y - 2*z - 7
F12 = 5*x - 9*y + 2*z - 15
print(sympy.solve([F10, F11, F12], [x, y, z]))

X = x * x + y * y - 1
Y = x - y + sympy.Rational(1, 2)
print(sympy.latex(sympy.solve([X, Y], [x, y])))

y= sympy.E ** (-2 * x) * sympy.sin(3 * x)
print("\n", sympy.latex(sympy.integrate(y, x)), "+C", "\n")

# ('- \\frac{2 e^{- 2 x} \\sin{\\left(3 x \\right)}}{13} - \\frac{3 e^{- 2 x} \\cos{\\left(3 x \\right)}}{13}', '+C')

result = r"""$$
- \frac{2 e^{- 2 x} \sin{\left(3 x \right)}}{13} - \frac{3 e^{- 2 x} \cos{\left(3 x \right)}}{13} +C
$$"""
wave = r"""$$\frac{\partial^2 u}{\partial t^2}=c^2\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)$$"""
sympy.preview(result, viewer="file", filename="result.png", euler=False,
                dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])