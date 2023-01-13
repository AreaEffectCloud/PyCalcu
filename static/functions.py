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

limit_tab = ["limit_start", "limit_end", "limit_formula"]
sum_tab = ["sum_end", "sum_func", "sum_start", "sum_formula"]
diff_tab = ["diff_formula"]
integral_tab = ["integral_end", "integral_start", "integral_formula"]

#LiteralString ->return: r"""$${latex}$$"""
tex = ""
def transfer_latex(text):
    tex = text.replcae("²", "^{2}")
    #tex = tex.replace("√", "\\sqrt").replace("∞", "\\infty").replace("π", "\\pi").replace("log", "\\log")
    #三角関数
    tex = tex.replace("sin", "\\sin").replace("cos", "\\cos").replace("tan", "\\tan")
    #逆三角関数
    tex = tex.replace("asin", "\\arcsin").replace("acos", "\\arccos").replace("atan", "\\arctan")
    return tex
    
#def autosize_latex(LiteralString):
    #行列
    #定積分
    #不定積分
    #数列
    #極限
    #数字