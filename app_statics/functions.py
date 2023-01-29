import json
import sympy
from sympy import sympify
from PIL import Image

##### config.json から設定の読み込み
with open("config.json", encoding="utf-8_sig") as f:
    config = json.load(f)
## load a config.json file | Get setting of language
lang = config['user']['language']

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

all_alpha = {"alpha":"α", "beta":"β", "gamma":"γ", "delta":"δ", "epsilon":"ε", "zeta":"ζ", "eta":"η", "theta":"θ", "iota":"ι", "kappa":"κ", "lambda":"λ", 
             "mu":"μ", "nu":"ν", "xi":"ξ", "omicron":"ο", "pi":"π", "rho":"ρ", "sigma":"σ", "tau":"τ", "upsilon":"υ", "phi":"φ", "chi":"χ", "psi":"ψ", "omega":"ω"}

#α to \\alpha
def symbol_latex(text):
    for key, value in all_alpha.items():
        text = str(text)
        if text.__contains__(value):              
            text = text.replace(value, "\\" + key)
    return text

def transform_latex(text):
    text= str(text).replace("√", "sqrt").replace("∞", "oo").replace("＋", "+").replace("－", "-")
    try:
        formula = sympify(text, convert_xor=True, evaluate=True)
        text = sympy.latex(formula)
    except:
        if lang == "en":
            print("========================================\n[Format Error]\n---> \"{0}\"\n========================================".format(text))
        elif lang == "ja":
            print("========================================\n[Format Error]\n---> {0}\n========================================".format(text))
    return text

def autosize_latex(formula):
    formula = symbol_latex(formula)
    try:
        sympy.preview(formula, viewer="file", filename="output_images/formula.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])

        im = Image.open("output_images/formula.png")
        width, height = im.size
    
        #拡大は不可
        size = (0, 0)
        if height >= 260 and width >= 984:
            size = (984, height)
        elif height >= 260:
            size = (width, 260)
        elif width >= 984:
            size = (984, height)
        else: size = (width, height)

        im.thumbnail(size)
        out_dim = im.size
        if out_dim[1] >= 260:
            size = (out_dim[0], 260)
            im.thumbnail(size)
            out_twice_dim = im.size
            out_twice_name = "formula_resized-" + str(out_twice_dim[0]) + "-" + str(out_twice_dim[1]) + ".png"
            im.save("output_images/" + out_twice_name, "PNG")
            im.close()
            return "output_images/" + out_twice_name
        else:
            out_name = "formula_resized-" + str(out_dim[0]) + "-" + str(out_dim[1]) + ".png"
            im.save("output_images/" + out_name, "PNG")
            im.close()
            return "output_images/" + out_name

    except:
        if lang == "en":
            print("========================================Couldn't generate a image of result========================================")
        elif lang == "ja":
            print("========================================画像を生成することが出来ませんでした========================================")
