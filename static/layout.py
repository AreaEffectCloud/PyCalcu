import PySimpleGUI as sg
import sympy

from languages import *

##定数
Pi = sympy.S.Pi # 円周率
E = sympy.S.Exp1 # 自然対数の底
I = sympy.S.ImaginaryUnit # 虚数単位
oo = sympy.oo #無限大

# 使用する変数の定義(小文字1文字は全てシンボルとする)
(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sympy.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

#Setting of Button
INPUT_FONT = ('HGS明朝B', 25)
BTNS_FONT = ('HGS明朝B', 20)
FONT = ('HGS明朝B', 15)
FONT_output = ('HGS明朝B', 13)
COLOR = ('white')
SIZE = (4,1)
SPACE = (0, 1)

##### Main / Left Layout #####
#Normal
normal_2 = {"power_two":" x² ", "e":" e ", "pi":" π ", "theta":" θ ", "infty":" ∞ "}
normal_3 = {"root":" √ ", "seven":" 7 ", "eight":" 8 ", "nine":" 9 ", "devide":" ÷ "}
normal_4 = {"power":" ^ ", "four":" 4 ", "five":" 5 ", "six":" 6 ", "multi":" × "}
normal_5 = {"log":"log", "one":" 1 ", "two":" 2 ", "three":" 3 ", "minus":" - "}
normal_6 = {"allclear":" AC ", "zero":" 0 ", "left_brackets":" ( ", "right_brackets":" ) ", "plus":" + "}

btns = [normal_2, normal_3, normal_4, normal_5, normal_6]
normal_layout = [
    #列ごとに設定する
    [sg.Column([[sg.Button(f'{value}', font=BTNS_FONT, key=f'{key}', size=SIZE, disabled=False, expand_x=True) 
    for key, value in btns_horizon.items()] for btns_horizon in btns], expand_x=True)]
]

#Functions
btns_1 = {"sin":"sin", "cos":"cos", "tan":"tan", "asin":"asin", "acos":"acos"}
btns_2 = {"atan":"atan", "alpha":" α ", "beta":" β ", "gamma":" γ ", "delta":" δ "}
btns_3 = {"epsilon":" ε ", "zeta":" ζ ", "eta":" η ", "iota":" ι ", "kappa":" κ "}
btns_4 = {"lambda":" λ ", "mu":" μ ", "xi":" ξ ", "rho":" ρ ", "sigma":" σ "}
btns_5 = {"tau":" τ ", "upsilon":" υ ", "phi":" φ ", "chi":" χ ", "psi":" ψ "}

btns = [btns_1, btns_2, btns_3, btns_4, btns_5]
function_layout = [
    [sg.Column([[sg.Button(f'{value}', font=BTNS_FONT, key=f'{key}', size=SIZE, disabled=False, expand_x=True) 
    for key, value in btns_horizon.items()] for btns_horizon in btns], expand_x=True)]
]

#Alphabet
btns_1 = [" a ", " b ", " c ", " d ", " f "]
btns_2 = [" g ", " h ", " i ", " j ", " k "]
btns_3 = [" l ", " m ", " n ", " o ", " p "]
btns_4 = [" q ", " r ", " s ", " t ", " u "]
btns_5 = [" v ", " w ", " x ", " y ", " z "]

btns_al = [btns_1, btns_2, btns_3, btns_4, btns_5]
alphabet_layout = [
    [sg.Column([[sg.Button(f'{i}', font=BTNS_FONT, size=SIZE, key=i, expand_x=True) 
    for i in btns_horizon] for btns_horizon in btns_al], expand_x=True)]
]

##### Main / Right Layout #####
#Limit
left = [
    [sg.Column([[sg.Image(filename="images/limit.png")]], background_color=COLOR, vertical_alignment='c')],
    [sg.Input("", font=INPUT_FONT, size=SIZE, key="lim_start"), 
     sg.Text("→", font=INPUT_FONT, text_color=('Black'), background_color=COLOR),
     sg.Input("", font=INPUT_FONT, size=SIZE, key="limit_end",)]
]
right = [
    #上部分の調整
    [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
    [sg.Text("  ", background_color=COLOR, font=BTNS_FONT)],
    [sg.Multiline("", font=INPUT_FONT, size=(20, 2))],
    #Tab内のサイズを調整
    [sg.Text("  ", background_color=COLOR, font=FONT)],
    [sg.Button("Add", font=FONT, size=SIZE, key="add_limit"), 
     sg.Button("Clear", font=FONT, key="delete_limit")]
]
limit_layout = [
    [sg.Column(left, element_justification='c', vertical_alignment='center', background_color=COLOR),
     sg.Column(right, background_color=COLOR)]
]

#Sum
left = [
    [sg.Column([[sg.Input("", font=INPUT_FONT, size=SIZE, key="sum_end")], [sg.Image(filename="images/sum.png")]], background_color=COLOR, element_justification='c', vertical_alignment='c')],
    [sg.Input("", font=INPUT_FONT, size=SIZE, key="sum_func"), 
     sg.Text("=", font=INPUT_FONT, text_color=('Black'), background_color=COLOR),
     sg.Input("", font=INPUT_FONT, size=SIZE, key="sum_start_value",)],
]
right = [
    [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
    [sg.Text("  ", background_color=COLOR, font=BTNS_FONT)],
    [sg.Multiline("", font=INPUT_FONT, size=(20, 2))],
    [sg.Text("  ", background_color=COLOR, font=FONT)],
    [sg.Button("Add", font=FONT, size=SIZE, key="add_sum"), 
     sg.Button("Clear", font=FONT, key="delete_sum")]
]
sigma_layout = [
    [sg.Column(left, element_justification='c', vertical_alignment='center', background_color=COLOR),
     sg.Column(right, background_color=COLOR)]
]

#Differential
#Default -> d/dx
left = [
    [sg.Column([
        [sg.Image(filename="images/diff/diff_x.png", key="diff_img")],
        ], background_color=COLOR, vertical_alignment='c')]
]
right = [
    [sg.Column([
        [sg.Combo(values=['x', 'y', 't', 'v'], default_value='x', size=(1, 1), readonly=True, 
        font=INPUT_FONT, background_color=COLOR, key="diff_select", enable_events=True)],
        ], background_color=COLOR, vertical_alignment='c'),
     sg.Column([
        [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
        [sg.Text("  ", background_color=COLOR, font=BTNS_FONT)],
        [sg.Multiline("", font=INPUT_FONT, size=(20, 2))],
        [sg.Text("  ", background_color=COLOR, font=FONT)],
        [sg.Button("Add", font=FONT, size=SIZE, key="add_diff"), 
         sg.Button("Clear", font=FONT, key="delete_diff")],
        [sg.Text("  ", background_color=COLOR, font=FONT)],
        ], background_color=COLOR, element_justification='l', vertical_alignment='c')
    ]
]
differential_layout = [
    [sg.Column(left, element_justification='c', vertical_alignment='center', background_color=COLOR),
     sg.Column(right, background_color=COLOR)]
]

#Integral
left = [
    [sg.Column([
        [sg.Image(filename="images/integral.png")],
        ], background_color=COLOR, vertical_alignment='c'),
    sg.Column([
        [sg.Text(top[lang], background_color=('Gray'), font=FONT_output)],
        [sg.Input("", font=INPUT_FONT, size=SIZE, key="integral_end")],
        [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
        [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
        [sg.Input("", font=INPUT_FONT, size=SIZE, key="integral_start")],
        [sg.Text(bottom[lang], background_color=('Gray'), font=FONT_output)],
        ], background_color=COLOR, vertical_alignment='c', element_justification='c')
    ]
]
right = [
    [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
    [sg.Text("  ", background_color=COLOR, font=BTNS_FONT)],
    [sg.Multiline("", font=INPUT_FONT, size=(20, 2))],
    [sg.Text("  ", background_color=COLOR, font=FONT)],
    [sg.Button("Add", font=FONT, size=SIZE, key="add_integral"), 
     sg.Button("Clear", font=FONT, key="delete_integral")],
    [sg.Text("  ", background_color=COLOR, font=FONT)]
]
integral_layout = [
    [sg.Column(left, element_justification='c', vertical_alignment='center', background_color=COLOR),
     sg.Column(right, background_color=COLOR)]
]

#Matrix
matrix_layout = [
    [sg.Column([
    [sg.Button("＋", enable_events=True, pad=(65, 5), font=FONT, size=SIZE, key="plus_vertical")],
    [sg.Button("＋", enable_events=True, font=FONT, size=SIZE, key="plus_horizon"), 
     sg.Column([[sg.Input(font=FONT, size=SIZE), sg.Input(font=FONT, size=SIZE)]], element_justification='l')],
    [sg.Column([[sg.Input(font=FONT, size=SIZE), sg.Input(font=FONT, size=SIZE)]], vertical_alignment='c')]
    ])]
]