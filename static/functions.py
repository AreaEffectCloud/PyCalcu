import json
import sympy
from sympy import sympify
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
def transform_latex(text):
    text= str(text).replace("√", "sqrt ").replace("∞", "oo").replace("＋", "+").replace("－", "-")
    try:
        formula = sympify(text, convert_xor=True, evaluate=True)
        text = sympy.latex(formula)
    except:
        #How to show the error that is format error
        print(f"Fromat error")
    return text

# formula : r"{\frac{}{}}"
def autosize_latex(formula):
    sympy.preview(formula, viewer="file", filename="formula.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])

    #画像の大きさに応じて、縦を調整
    im = Image.open("formula.png")
    width, height = im.size
    print("Width : ", width, "Height : ", height)
    size = (650, width)
    im.thumbnail(size)
    out_dim = im.size
    out_name = "resized-" + str(out_dim[0]) + "-" + str(out_dim[1]) + ".png"
    im.save(out_name, "PNG")
    im.close()
    
    #極限
    #数列
    #定積分
    #不定積分
    #方程式

wave = r"""$$\frac{\partial^2 u}{\partial t^2}=c^2\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)$$"""
int = r"""$$\int\limits_{}^{}{y^{64} - \frac{y^{π}}{\log{\left(y + y² \right)}}}dx$$"""
frac = r"""$$\int\limits_{0}^{1}{- \frac{π}{2}}dx\\$$"""
autosize_latex(frac)