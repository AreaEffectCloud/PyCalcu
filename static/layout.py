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

#Setting of Button
INPUT_FONT = ('HGS明朝B', 25)
BTNS_FONT = ('HGS明朝B', 20)
FONT = ('HGS明朝B', 15)
FONT_tex = ('HGS明朝B', 13)
FONT_output = ('HGS明朝B', 13)
COLOR = ('white')
SIZE = (4,1)
SPACE = (0, 1)

##### Main / Left Layout #####
#Normal
btns_2 = [" x² ", " e ", " π ", " θ ", " ∞ "]
btns_3 = [" √ ", " 7 ", " 8 ", " 9 ", " ÷ "]
btns_4 = [" ^ ", " 4 ", " 5 ", " 6 ", " × "]
btns_5 = ["log", " 1 ", " 2 ", " 3 ", " - "]
btns_6 = [" AC ", " 0 ", " ( ", " ) ", " + "]

btns = [btns_2, btns_3, btns_4, btns_5, btns_6]
normal_layout = [
    #列ごとに設定する
    [sg.Column([sg.Button(f'{i}', font=BTNS_FONT, size=SIZE, disabled=False) for i in btns_horizon] for btns_horizon in btns)]
]

#Functions
btns_1 = ["sin", "cos", "tan", "asin", "acos"]
btns_2 = ["atan", " α ", " β ", " γ ", "δ"]
btns_3 = [" ε ", " ζ ", " η ", " ι ", " κ "]
btns_4 = [" λ ", " μ ", " ξ ", " ρ ", " σ "]
btns_5 = [" τ ", " υ ", " φ ", " χ ", " ψ "]

btns = [btns_1, btns_2, btns_3, btns_4, btns_5]
function_layout = [
    [sg.Column([sg.Button(f'{i}', font=BTNS_FONT, size=SIZE, disabled=False) for i in btns_horizon] for btns_horizon in btns)]
]

#Alphabet
btns_1 = [" a ", " b ", " c ", " d ", " f "]
btns_2 = [" g ", " h ", " i ", " j ", " k "]
btns_3 = [" l ", " m ", " n ", " o ", " p "]
btns_4 = [" q ", " r ", " s ", " t ", " u "]
btns_5 = [" v ", " w ", " x ", " y ", " z "]

btns_al = [btns_1, btns_2, btns_3, btns_4, btns_5]
alphabet_layout = [
    [sg.Column([sg.Button(f'{i}', font=BTNS_FONT, size=SIZE) for i in btns_horizon] for btns_horizon in btns_al)]
]

##### Main / Right Layout #####
left = [
    [sg.Column([[sg.Image(filename="images/limit.png")]], background_color=COLOR, vertical_alignment='c')],
    [sg.Input("", font=INPUT_FONT, size=SIZE, key="lim_start"), 
     sg.Text("→", font=INPUT_FONT, text_color=('Black'), background_color=COLOR),
     sg.Input("", font=INPUT_FONT, size=SIZE, key="limit_end",)],
    [sg.Button("Add", font=FONT, size=SIZE, key="add_limit"), 
     sg.Button("Clear", font=FONT, key="delete_limit")]
]
right = [
    #上部分の調整
    [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
    [sg.Text("  ", background_color=COLOR, font=BTNS_FONT)],
    [sg.Multiline("", font=INPUT_FONT, size=(20, 2))],
    #Tab内のサイズを調整
    [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
    [sg.Text("  ", background_color=COLOR, font=INPUT_FONT)],
]
limit_layout = [
    [sg.Column(left, element_justification='c', vertical_alignment='center', background_color=COLOR),
     sg.Column(right, background_color=COLOR)]
]

sigma_layout = [[]]
differential_layout = [[]]
integral_layout = [[]]

#Matrix
matrix_layout = [
    [sg.Column([
    [sg.Button("＋", enable_events=True, pad=(65, 5), font=FONT, size=SIZE, key="plus_vertical")],
    [sg.Button("＋", enable_events=True, font=FONT, size=SIZE, key="plus_horizon"), sg.Input(font=FONT, size=SIZE)]])]
]