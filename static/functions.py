import json
import re
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

#LiteralString ->return: r"""$${tex}$$"""
tex = ""
def transfer_latex(text):
    tex = text
    tex = tex.replace("√", "\\sqrt ").replace("∞", "\\infty ").replace("π", "\\pi ").replace("θ", "\\theta ").replace("²", "^{2}").replace("log", "\\log")
    #逆三角関数
    tex = tex.replace("asin", "\\arcsin").replace("acos", "\\arccos").replace("atan", "\\arctan")
    #三角関数
    tex = tex.replace("sin", "\\sin").replace("cos", "\\cos").replace("tan", "\\tan")

    #分数

    return tex

print("Latex表記 : ", transfer_latex(r"e / {\pi ＋ {25 / {\cos{\theta}}}}"))
print("Latex表記 : ", transfer_latex(r"\pi +(Edited) {25 / {\cos{\theta"))

#Frac
def transfer_frac(string):
    formula = string
    #分子中に於ける演算記号の有無
    pattern_plus = r"/\s*?{[^}]+[＋－]"
    plus_in_frac = re.findall(pattern_plus, formula)
    for i in plus_in_frac:
        plus = str(i).replace("＋", "+")
        formula = formula.replace(i, plus)
    
    regex = r"[＋－=]"
    split_formula = re.split(regex, formula)
    print("Split : ", split_formula)
    for i in split_formula:
        try:
            pattern = "[^/]+[^}]+"
            res = re.search(pattern, i).group() #type:ignore

            #are there any Denominators
            if res.__contains__("/"):
                print(f"\n[Frac : ]", res)
                numerator_pattern = "[^{]+"
                frac = re.search(numerator_pattern, res).group() #type:ignore
                numerator = frac.replace("/", "")
                denominator = res.replace(frac, "")
                denominator = denominator.lstrip("{").__add__("}").replace("+", "＋")
                print("\n分子 : ", numerator, "\n分母 : ", denominator)
                print("\n \\frac{{{0}}}{{{1}".format(numerator, denominator))

                if denominator.__contains__("/"):
                    transfer_frac(denominator)
        except:
            break
    return formula
    
string = r"\sin{\pi^{2}} － 1 / {x} = 25 ＋ e / {\pi ＋ {25 / {\cos{\theta}}}}"
print(transfer_frac(string))

#def autosize_latex(LiteralString):
    #定積分
    #不定積分
    #数列
    #極限
    #方程式