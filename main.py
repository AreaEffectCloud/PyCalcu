import PySimpleGUI as sg

from static.buttons import *
from static.functions import *

sg.theme("Reddit")

## config.json の読み込み
print("Loading... : ", load_file("static/config.json"))

menu_def_jp = [
    ["&ファイル", ["新規",
                    "開く",
                    "&上書き保存             Ctrl+S",
                    "名前を付けて保存",
                    "&終了"]],
    ["&編集", ["元に戻す        Ctrl+Z",
               "再実行           Ctrl+Y"]],
    ["&書式", ["Font"]],
    ["&ヘルプ", ["Info of version"]]
]

#MenuBarは一旦なしで作る [menu],
#menu = sg.MenuBar(menu_def_jp, key="menubar", font=("メイリオ", 10), size=(15, 3))

#Latex表記 -> .png形式で表示
###             need resize the image
image_formula_latex = sg.Image(filename="result.png", key="image_formula_latex", pad=((0, 0), (0, 0)), right_click_menu=None)

##              <       Preview     >           ##
#Tex表記 => Latexに変換する前の段階 + 任意の文字に変更可
multiline_formula_tex = sg.Multiline(key='multiline_formula_tex', font=FONT_tex, pad=((0, 0), (0, 0)), size=(100, 4), enter_submits=True),

#Edit
right_click_menu_jp = ['&Right', ["Copy", "Paste"]]

#レイアウト
layout = [[image_formula_latex],
          [sg.Button('Integrate', key="integrate", font=FONT, size=(15, 1)), 
            sg.Button('Sigma', key="sigma", font=FONT, size=(15, 1)), 
            sg.Button('limit', key="limit", font=FONT, size=(15, 1))],
          [sg.Button('Cancel', key="Cancel", font=FONT, size=(15, 1))],
          [multiline_formula_tex]
         ]

title = { 'en':str('Calculator'), 'ja':str('関数電卓') }
window = sg.Window(title['en'], layout, margins=(0,0), size=(750, 500), icon="", resizable=True, finalize=True)

window['multiline_formula_tex'].expand(expand_x=True, expand_y=True)

# -------------------------------------
#           イベント毎の処理
# -------------------------------------
while True:

    event, values = window.read() # type: ignore

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'integrate':
        #式
        y= sympy.E ** (-2 * x) * sympy.sin(3 * x)
        result_tex = sympy.latex((sympy.integrate(y, x)).doit())

        #F2 = x ** 5 + x + 1 # 高次式
        #result_tex = sympy.latex((sympy.solve(F2, x)))

        #tex
        if multiline_formula_tex.index == None:
            window["multiline_formula_tex"].print(" + ", result_tex) #type:ignore
        else: window["multiline_formula_tex"].print(result_tex) #type:ignore
        #Latex
        #-1個しか表示されない
        print("途中式は、 ", values["multiline_formula_tex"], " です。")

        ##
        ##          Tex表記に何とかして変換したい
        ##                                   --->  積分定数は加えずに表示
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