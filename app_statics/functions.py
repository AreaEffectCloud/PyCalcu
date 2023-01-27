import sympy
from sympy import sympify
from PIL import Image

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

all_alpha = {"alpha":"α", "beta":"β", "gamma":"γ", "delta":"δ",
             "epsilon":"ε", "zeta":"ζ", "eta":"η", "iota":"ι", "kappa":"κ",
             "lambda":"λ", "mu":"μ", "xi":"ξ", "rho":"ρ", "sigma":"σ",
             "tau":"τ", "upsilon":"υ", "phi":"φ", "chi":"Χ", "psi":"Ψ"}

#α -> alpha
def symbol_latex(text):
    for key, value in all_alpha.items():
        text = str(text)
        if text.__contains__(value):
            #Debug
            print("\n[Before]", text, "\n[Key]", key, " [Value]", value)                
            text = text.replace(value, "\\" + key)
            #Debug
            print("[Result]", text)
    return text

#LiteralString ->return: r"""$${tex}$$"""
def transform_latex(text):
    #How to replace π to \pi
    text= str(text).replace("√", "sqrt").replace("∞", "oo").replace("＋", "+").replace("－", "-")
    try:
        #Debug
        print(text)
        formula = sympify(text, convert_xor=True, evaluate=True)
        #Debug
        print("[After Sympify : ]", formula)
        text = sympy.latex(formula)
        #Debug
        print("[After Latex : ]", text)
    except:
        #How to show the error that is format error
        #Debug
        print(f"[ Format error ] Sympify Error")
        print(f"[Error Text : ]", text)
    return text

# formula : r"{\frac{}{}}"
def autosize_latex(formula):
    formula = symbol_latex(formula)
    print("\n", formula)
    formula = formula.replace("π", "\\pi")
    sympy.preview(formula, viewer="file", filename="output_images/formula.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])

    #画像の大きさに応じて、縦を調整
    im = Image.open("output_images/formula.png")
    width, height = im.size
    print("Width : ", width, "Height : ", height)
    size = (650, width)
    im.thumbnail(size)
    out_dim = im.size
    out_name = "resized-" + str(out_dim[0]) + "-" + str(out_dim[1]) + ".png"
    im.save("output_images/" + out_name, "PNG")
    im.close()
    
    #極限
    #数列
    #定積分
    #不定積分
    #方程式