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
FONT_tex = ('HGS明朝B', 13)

##### Tab Layout #####
normal_layout = [[]]
limit_layout = [[]]
sigma_layout = [[]]
differential_layout = [[]]
integral_layout = [[]]
