import PySimpleGUI as sg

from static.tabs import *
from static.functions import *
from languages import *

sg.theme("Reddit")

## load a config.json file
config = get_json("static/config.json")
#Get setting of language
lang = config['user']['language']

#####   #####   GUI Layout  #####  #####
#Latex表記 -> .png形式で表示
#Image Column で様々な場合における結果を中央に配置できない:  , pad=((0, 0), (158, 0))
image_formula_latex_column = sg.Image(filename="result.png", key="image_formula_latex", right_click_menu=click_menu[lang])

#####   Tab Group #####

main_column_Tabs = sg.TabGroup([[
    sg.Tab(normal[lang], normal_layout, font=FONT, key="normal"),
    sg.Tab(limit[lang], limit_layout, font=FONT, key="limit"),
    sg.Tab(sigma[lang], sigma_layout, key="sigma", font=FONT),
    sg.Tab(diff[lang], differential_layout, key="diff", font=FONT),
    sg.Tab(integral[lang], integral_layout, key="integral", font=FONT)
    ]], font=FONT, expand_x=True, expand_y=True)

#####   Output  #####
multiline_formula_tex = sg.Output(key='multiline_formula_tex', font=FONT_tex, pad=((0, 0), (0, 0)), size=(100, 5), expand_x=True, expand_y=True)
output_frame = sg.Frame(output_frame_title[lang], [[multiline_formula_tex]], expand_x=True, expand_y=True)

#レイアウト
layout = [ [output_frame], 
            [main_column_Tabs],
            [sg.Column([[image_formula_latex_column]], size=(800, 426), justification='center', scrollable=True)]]

window = sg.Window(title[lang], layout, icon="", resizable=True, finalize=True)

# -------------------------------------
#           イベント毎の処理
# -------------------------------------
while True:

    event, values = window.read()#type:ignore

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'integrate':
        #式
        y= sympy.E ** (-2 * x) * sympy.sin(3 * x) #type:ignore
        result_tex = sympy.latex((sympy.integrate(y, x)).doit())

        F2 = x ** 5 + x + 1 # 高次式
        result_tex = sympy.latex((sympy.solve(F2, x)))

        #tex
        if multiline_formula_tex.do_not_clear == None:
            window["multiline_formula_tex"].print(" + ", result_tex) #type:ignore
        else: window["multiline_formula_tex"].print(result_tex) #type:ignore
        #Latex
        #-1個しか表示されない
        print("途中式は、 ", values["multiline_formula_tex"], " です。")

        ##積分定数は加えずに表示
        latex_result = r"""$${result_tex}$$""".format(result_tex=result_tex)
        image_result = sympy.preview(latex_result, viewer="file", filename="result.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])
        print(latex_result)

        #How to update the image at the sg.Image
        #window["image_formula_latex"].bind(image_result)  # type: ignore

    #
    #        DANGEROUS CODE HERE !!!!!!!!!!!!!!!
    #    
    elif event == 'sigma':
        r = 0
        for K in range(10000):
            r += (sympy.N(sympy.sin(sympy.Rational(K, 10000).doit()), 50))

        image_result = sympy.preview(r, viewer="file", filename="result.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])
        print(r)
        #tex
        window["multiline_formula_tex"].print(r)  # type: ignore

    elif event == 'limit':
        y = sympy.sin(x ** 2) / (E ** (-x) + 1)
        result_tex = sympy.latex(sympy.integrate(y, (x, -(Pi / 2), Pi / 2)).doit())
        latex_result = r"""$${result_tex}$$""".format(result_tex=result_tex)
        image_result = sympy.preview(latex_result, viewer="file", filename="result.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])
        print(latex_result)
        #tex
        window["multiline_formula_tex"].print(result_tex) #type:ignore

window.close()