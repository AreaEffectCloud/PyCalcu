import sympy
from sympy import sympify

sympy.init_printing()
# 使用する変数の定義(小文字1文字は全てシンボルとする)
(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sympy.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

# ('- \\frac{2 e^{- 2 x} \\sin{\\left(3 x \\right)}}{13} - \\frac{3 e^{- 2 x} \\cos{\\left(3 x \\right)}}{13}', '+C')

result = r"""$$
- \frac{2 e^{- 2 x} \sin{\left(3 x \right)}}{13} - \frac{3 e^{- 2 x} \cos{\left(3 x \right)}}{13} +C
$$"""
wave = r"""$$\frac{\partial^2 u}{\partial t^2}=c^2\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)$$"""
sympy.preview(wave, viewer="file", filename="result.png", euler=False,
                dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])

expr = r"""$$\sqrt{mgh-2gr}$$"""
expr = sympy.sin(sympy.pi ** 2) + b * x ** 2 + a* x ** 89
print("\n", sympify(expr, convert_xor=True, evaluate=True))