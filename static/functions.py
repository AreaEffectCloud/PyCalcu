import json
import sympy
from PIL import Image

##### config.json から設定の読み込み
#####
def get_json(path):
    with open(path, encoding="utf-8_sig") as json_file:
       f = json.load(json_file)
    return f

#どの Input / Multiline boxにFocusされているかを設定するEventをbind
def set_bind(window):
    #Limit
    window['limit_start'].bind('<FocusIn>', '+Input')
    window['limit_end'].bind('<FocusIn>', '+Input')
    window['limit_formula'].bind('<FocusIn>', '+Input')

    #Sum
    window['sum_end'].bind('<FocusIn>', '+Input')
    window['sum_func'].bind('<FocusIn>', '+Input')
    window['sum_start'].bind('<FocusIn>', '+Input')
    window['sum_formula'].bind('<FocusIn>', '+Input')

    #Diff
    window['diff_formula'].bind('<FocusIn>', '+Input')

    #Integral
    window['integral_end'].bind('<FocusIn>', '+Input')
    window['integral_start'].bind('<FocusIn>', '+Input')
    window['integral_formula'].bind('<FocusIn>', '+Input')

    return None

binds = ["limit_start+Input", "limit_end+Input", "limit_formula+Input",
         "sum_end+Input", "sum_func+Input", "sum_start+Input", "sum_formula+Input",
         "diff_formula+Input",
         "integral_end+Input", "integral_start+Input", "integral_formula+Input"]

def new_horizon_layout(i):
    #matchで縦(横)の数ごとに増やす
    return [[]]

def new_vertical_layout(i):
    return [[]]

#LiteralString -> r"""$${result_tex}$$"""
#def autosize_latex(LiteralString):
    #行列
    #定積分
    #不定積分
    #数列
    #極限
    #数字