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
func_1 = {"sin":"sin", "cos":"cos", "tan":"tan", "asin":"asin", "acos":"acos"}
func_2 = {"atan":"atan", "alpha":" α ", "beta":" β ", "gamma":" γ ", "delta":" δ "}
func_3 = {"epsilon":" ε ", "zeta":" ζ ", "eta":" η ", "iota":" ι ", "kappa":" κ "}
func_4 = {"lambda":" λ ", "mu":" μ ", "xi":" ξ ", "rho":" ρ ", "sigma":" σ "}
func_5 = {"tau":" τ ", "upsilon":" υ ", "phi":" φ ", "chi":" χ ", "psi":" ψ "}

btns = [func_1, func_2, func_3, func_4, func_5]
function_layout = [
    [sg.Column([[sg.Button(f'{value}', font=BTNS_FONT, key=f'{key}', size=SIZE, disabled=False, expand_x=True) 
    for key, value in btns_horizon.items()] for btns_horizon in btns], expand_x=True)]
]

#Alphabet
alpha_1 = {" a ", " b ", " c ", " d ", " f "}
alpha_2 = [" g ", " h ", " i ", " j ", " k "]
alpha_3 = [" l ", " m ", " n ", " o ", " p "]
alpha_4 = [" q ", " r ", " s ", " t ", " u "]
alpha_5 = [" v ", " w ", " x ", " y ", " z "]

btns_al = [alpha_1, alpha_2, alpha_3, alpha_4, alpha_5]
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
    [sg.Button("Add", font=BTNS_FONT, size=SIZE, key="add_limit"), 
     sg.Button("Clear", font=BTNS_FONT, key="delete_limit")]
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
    [sg.Button("Add", font=BTNS_FONT, size=SIZE, key="add_sum"), 
     sg.Button("Clear", font=BTNS_FONT, key="delete_sum")]
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
        font=('HGS明朝B', 40), background_color=COLOR, key="diff_select", enable_events=True)],
        ], background_color=COLOR, vertical_alignment='c'),
     sg.Column([
        [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
        [sg.Text("  ", background_color=COLOR, font=BTNS_FONT)],
        [sg.Multiline("", font=INPUT_FONT, size=(20, 2))],
        [sg.Text("  ", background_color=COLOR, font=FONT)],
        [sg.Button("Add", font=BTNS_FONT, size=SIZE, key="add_diff"), 
         sg.Button("Clear", font=BTNS_FONT, key="delete_diff")],
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
        [sg.Text(top[lang], background_color=('Gray'), font=FONT)],
        [sg.Input("", font=INPUT_FONT, size=SIZE, key="integral_end")],
        [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
        [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
        [sg.Input("", font=INPUT_FONT, size=SIZE, key="integral_start")],
        [sg.Text(bottom[lang], background_color=('Gray'), font=FONT)],
        ], background_color=COLOR, vertical_alignment='c', element_justification='c')
    ]
]
right = [
    [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
    [sg.Text("  ", background_color=COLOR, font=BTNS_FONT)],
    [sg.Multiline("", font=INPUT_FONT, size=(20, 2))],
    [sg.Text("  ", background_color=COLOR, font=FONT)],
    [sg.Button("Add", font=BTNS_FONT, size=SIZE, key="add_integral"), 
     sg.Button("Clear", font=BTNS_FONT, key="delete_integral")],
    [sg.Text("  ", background_color=COLOR, font=('HGS明朝B', 5))]
]
integral_layout = [
    [sg.Column(left, element_justification='c', vertical_alignment='center', background_color=COLOR),
     sg.Column(right, background_color=COLOR)]
]

#Matrix
input_boxes = [
    [sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), 
     sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE)],
    [sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), 
     sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE)],
    [sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), 
     sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE),],
    [sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), 
     sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE),],
    [sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), 
     sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE), sg.Input(font=BTNS_FONT, size=SIZE),]
]
matrix_layout = [
    [sg.Text("  ", background_color=COLOR, font=FONT, size=(8, 1)), 
     sg.Button("＋", font=FONT, size=SIZE, key="plus_vertical"),
     sg.Text(rows[lang], background_color=('Gray'), font=FONT)],
    [sg.Column([[sg.Button("＋", font=FONT, size=SIZE, key="plus_horizon")],
    [sg.Text(columns[lang], background_color=('Gray'), font=FONT)],
    ], background_color=COLOR, element_justification='c', vertical_alignment='top'), 
     sg.Column(input_boxes, background_color=COLOR, element_justification='l', scrollable=False),
     sg.Column([
        [sg.Button("Add", font=BTNS_FONT, size=SIZE, key="add_matrix")],
        [sg.Button("Clear", font=BTNS_FONT, key="delete_matrix")]
     ], background_color=COLOR, element_justification='l', vertical_alignment='center')]
]
