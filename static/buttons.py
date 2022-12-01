import PySimpleGUI as sg
import sympy
from sympy import Sum, oo, N

##定数
Pi = sympy.S.Pi # 円周率
E = sympy.S.Exp1 # 自然対数の底
I = sympy.S.ImaginaryUnit # 虚数単位
oo = sympy.oo #無限大

# 使用する変数の定義(小文字1文字は全てシンボルとする)
(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sympy.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

#Font of Button
FONT = ('HGS明朝B', 15)
FONT_tex = ('HGS明朝B', 12)

# 数学記号など
symbol_commands = [
    "\\frac{}{}", "\\frac{d }{d }", "\\int_{}^{}", "\\sum\\limits_{}^{}", 
    """\\begin{aligned}
    \\left[
        \\begin{array}{}

        \\end{array}
        \\right]
    \\end{aligned}""",
    """\\begin{aligned}
    \\left\\{
    \\begin{array}{l}

    \\end{array}
    \\right.
    \\end{aligned}""",
]
symbols = [
    "分数", "微分", "積分", "総和", "行列", "方程式"
]
symbol_buttons = [
    sg.Button(
        symbol,
        key=symbol_commands[i],
        pad=(0, 0),
        font=FONT
    ) for i, symbol in enumerate(symbols)
]

# ギリシャ文字（小文字）
low_greek_letter_commands = [
    "\\alpha", "\\beta", "\\gamma", "\\delta", "\\epsilon", "\\zeta",
    "\\theta", "\\lambda", "\\mu","\\pi", "\\rho", "\\phi","\\omega"
]
low_greek_letters = [
    "α", "β", "γ", "δ", "ε", "ζ",
    "θ","λ", "μ","π", "ρ", "φ","ω"
]
low_greek_buttons = [
    sg.Button(
        low_greek_letter,
        key=low_greek_letter_commands[i],
        pad=(0, 0),
        font=FONT
    ) for i, low_greek_letter in enumerate(low_greek_letters)
]

# 装飾
decoration_commands = [
    "\\dot{}", "\\sqrt[]{}"
]
decorations = [
    "ドット", "ルート"
]
decoration_buttons = [
    sg.Button(
        decoration,
        key=decoration_commands[i],
        pad=(0, 0),
        font=FONT
    ) for i, decoration in enumerate(decorations)
]