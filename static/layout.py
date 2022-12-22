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
FONT = ('HGS明朝B', 15)
FONT_tex = ('HGS明朝B', 13)
FONT_output = ('HGS明朝B', 13)
COLOR = ('white')
SIZE = (4,1)

##### Main / Left Layout #####
#Normal
btns_1 = [" π ", "sin", "cos", "tan"]
btns_2 = [" θ "]
btns_3 = [" ^ ", " 7 ", " 8 ", " 9 ", " ÷ "]
btns_4 = ["log", " 4 ", " 5 ", " 6 ", " × "]
btns_5 = [" ln ", " 1 ", " 2 ", " 3 ", " - "]
btns_6 = [" ∞ ", " 0 ", "( )", " AC ", " + "]

btns = [btns_1, btns_2, btns_3, btns_4, btns_5, btns_6]
normal_layout = [
    #列ごとに設定する
    [sg.Column([sg.Button(f'{i}', font=FONT, size=SIZE) for i in btns_horizon] for btns_horizon in btns)]
]

#Alphabet
btns_1 = [" a ", " b ", " c ", " d ", " α "]
btns_2 = [" e ", " f ", " g ", " h ", " β "]
btns_3 = [" i ", " j ", " k ", " l ", " ζ "]
btns_4 = [" m ", " n ", " o ", " p ", " δ" ]
btns_5 = [" q ", " r ", " s ", " t ", " ω "]
btns_6 = [" u ", " v ", " w ", " x ", " y "]

btns_al = [btns_1, btns_2, btns_3, btns_4, btns_5, btns_6]
alphabet_layout = [
    [sg.Column([sg.Button(f'{i}', font=FONT, size=SIZE) for i in btns_horizon] for btns_horizon in btns_al)]
]

##### Main / Right Layout #####
limit_layout = [[sg.Text("Sorry, but it isn't work on.",visible=True)]]
sigma_layout = [[]]
differential_layout = [[]]
integral_layout = [[]]

#Matrix
matrix_layout = [
    [sg.Column([
    [sg.Button("＋", enable_events=True, pad=(65, 5), font=FONT, size=SIZE, key="plus_vertical")],
    [sg.Button("＋", enable_events=True, font=FONT, size=SIZE, key="plus_horizon"), sg.Input(font=FONT, size=SIZE)]])]
]