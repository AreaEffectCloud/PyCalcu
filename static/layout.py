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

##### Main Left Layout #####

#btns_1 = ["sin", "x", "log", "ln"]
#btns_2 = ["cos", "y", "7", "4", "1", "+/-"]
#btns_3 = ["tan", "z", "8", "5", "2", "0"]
#btns_4 = ["π", "ω", "9", "6", "3", "e"]

btns_1 = ["sin", "cos", "tan", " π "]
btns_2 = [" x ", " y ", " z ", " ω "]
btns_3 = ["^", "7", "8", "9"]
btns_4 = ["∞", "4", "5", "6"]
btns_5 = ["log", "1", "2", "3"]
btns_6 = ["ln", "0", "( )", "AC"]

one_layout = [
    [sg.Button(f'{i}', font=FONT) for i in btns_1]
]
two_layout = [
    [sg.Button(f'{i}', font=FONT) for i in btns_2]
]
three_layout = [
    [sg.Button(f'{i}', font=FONT) for i in btns_3]
]
four_layout = [
    [sg.Button(f'{i}', font=FONT) for i in btns_4]
]
five_layout = [
    [sg.Button(f'{i}', font=FONT) for i in btns_5]
]
six_layout = [
    [sg.Button(f'{i}', font=FONT) for i in btns_6]
]

normal_layout = [
    #列ごとに設定する
    [sg.Column(one_layout, background_color=COLOR)],
    [sg.Column(two_layout, background_color=COLOR)],
    [sg.Column(three_layout, background_color=COLOR)],
    [sg.Column(four_layout, background_color=COLOR)],
    [sg.Column(five_layout, background_color=COLOR)],
    [sg.Column(six_layout, background_color=COLOR)], 
]

##### Tab Layout #####
limit_layout = [[]]
sigma_layout = [[]]
differential_layout = [[]]
integral_layout = [[]]
matrix_layout = [[]]