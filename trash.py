import sympy
from static.layout import *

sympy.init_printing()

# ('- \\frac{2 e^{- 2 x} \\sin{\\left(3 x \\right)}}{13} - \\frac{3 e^{- 2 x} \\cos{\\left(3 x \\right)}}{13}', '+C')

result = r"""$$
- \frac{2 e^{- 2 x} \sin{\left(3 x \right)}}{13} - \frac{3 e^{- 2 x} \cos{\left(3 x \right)}}{13} +C
$$"""
wave = r"""$$\frac{\partial^2 u}{\partial t^2}=c^2\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)$$"""
sympy.preview(wave, viewer="file", filename="result.png", euler=False,
                dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])

print("\n", sympify("\\sqrt{mgh-2gr}", convert_xor=True, evaluate=True))
