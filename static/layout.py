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
COLOR = ('white')
SIZE = (4,1)

##### Main / Left Layout #####
#Normal
btns_1 = ["sin", "cos", "tan", " π "]
btns_2 = [" x ", " y ", " z ", " θ "]
btns_3 = [" ^ ", " 7 ", " 8 ", " 9 "]
btns_4 = [" ∞ ", " 4 ", " 5 ", " 6 "]
btns_5 = ["log", " 1 ", " 2 ", " 3 "]
btns_6 = [" ln ", " 0 ", "( )", " AC "]

btns = [btns_1, btns_2, btns_3, btns_4, btns_5, btns_6]
normal_layout = [
    #列ごとに設定する
    [sg.Button(f'{i}', font=FONT, size=SIZE) for i in btns_horizon] for btns_horizon in btns
]

#Alphabet
btns_1 = [" a ", " b ", " c ", " d "]
btns_2 = [" e ", " f ", " g ", " h "]
btns_3 = [" i ", " j ", " k ", " l "]
btns_4 = [" m ", " n ", " o ", " p "]
btns_5 = [" q ", " r ", " s ", " t "]
btns_6 = [" u ", " v ", " w "]

btns_al = [btns_1, btns_2, btns_3, btns_4, btns_5, btns_6]
alphabet_layout = [
    [sg.Button(f'{i}', font=FONT, size=SIZE) for i in btns_horizon] for btns_horizon in btns_al
]

##### Main / Right Layout #####
limit_layout = [[]]
sigma_layout = [[]]
differential_layout = [[]]
integral_layout = [[]]

#Matrix
matrix_layout = [
    [sg.Button("＋", enable_events=True, pad=(65, 5), font=FONT, size=SIZE, key="plus_vertical")],
    [sg.Button("＋", enable_events=True, font=FONT, size=SIZE, key="plus_horizon"), sg.Input(font=FONT, size=SIZE)]]