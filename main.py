import PySimpleGUI as sg

from static.layout import *
from static.functions import *
from static.languages import *

sg.theme("Reddit")

##### ##### Layout  #####  #####

#must resize
image_formula_latex_column = sg.Image(filename="result.png", key="image_formula_latex", right_click_menu=click_menu[lang])

#####   Tab Group #####
main_column_left_tabs = sg.TabGroup([[
    sg.Tab(normal[lang], normal_layout, key="normal"),
    sg.Tab(function[lang], function_layout, key="function"),
    sg.Tab(alphabet[lang], alphabet_layout, key="alphabet")
    ]], font=FONT, expand_x=True)

main_column_right_tabs = sg.TabGroup([[
    sg.Tab(limit[lang], limit_layout, key="limit", font=FONT),
    sg.Tab(sigma[lang], sigma_layout, key="sigma", font=FONT),
    sg.Tab(diff[lang], differential_layout, key="diff", font=FONT),
    sg.Tab(integral[lang], integral_layout, key="integral", font=FONT),
    #No There # sg.Tab(matrix[lang], matrix_layout, key="matrix", font=FONT)
    ]], font=FONT, expand_x=True)

#####   Output  #####
multiline_formula_tex = sg.Output(key='output_tex', font=FONT_output, pad=((0, 0), (0, 0)), size=(100, 5), expand_x=True, expand_y=True)
output_frame = sg.Frame(output_frame_title[lang], [[multiline_formula_tex]], font=FONT_output, expand_x=True)

#レイアウト
layout = [ [output_frame], 
            [main_column_left_tabs, main_column_right_tabs],
            [sg.Column([[image_formula_latex_column]],  justification='center', scrollable=True)]
            ]

window = sg.Window(title[lang], layout, icon="", use_default_focus=False, resizable=True, finalize=True)

set_bind(window)

# -------------------------------------
#           イベント毎の処理
# -------------------------------------
focus = ""
space = ""
while True:

    event, values = window.read() #type:ignore

    if event == sg.WIN_CLOSED:
        break
    #Diff / Change Image
    elif event == "diff_select":
        selected = values["diff_select"]
        window["diff_img"].update(filename="images/diff/diff_{i}.png".format(i=selected))

    #get Focus
    elif event in binds:
        focus = str(event).replace("+Input", "")
        print(focus)

    #All Clear
    elif event == "allclear":
        if focus in limit_tab:
            for box in limit_tab:
                window["{i}".format(i=box)].update(space) #type:ignore
        elif focus in sum_tab:
            for box in sum_tab:
                window["{i}".format(i=box)].update(space) #type:ignore
        elif focus in diff_tab:
            for box in diff_tab:
                window["{i}".format(i=box)].update(space) #type:ignore
        elif focus in integral_tab:
            for box in integral_tab:
                window["{i}".format(i=box)].update(space) #type:ignore
    
    #括弧含む
    elif event in brackets:
        if focus != "":
            text = values["{i}".format(i=focus)]
            text = text + window[event].get_text() + "(" #type:ignore
            window["{i}".format(i=focus)].update(text)
    
    #2乗
    elif event in "power_twice":
        if focus != "":
            text = values["{i}".format(i=focus)]
            if text != "":
                text = text + "²"
                window["{i}".format(i=focus)].update(text)

    #Other Bottons
    elif event in all_btns_keys:
        if focus != "":
            text = values["{i}".format(i=focus)]
            #values[event] occur error
            text = text + window[event].get_text() #type:ignore
            window["{i}".format(i=focus)].update(text)
    
    #Add
    elif event in "add_limit":
        if values["limit_formula"] != "":
            if values["limit_start"] != "" and values["limit_end"] != "":
                print(f'G')

    elif event in "add_sum":
        if values["sum_formula"] != "":
            print(f'G')

    elif event in "add_diff":
        if values["diff_formula"] != "":
            formula = r"""$${i}$$""".format(i=values["diff_formula"])
            print(formula)
            
    elif event in "add_integral":
        if values["integral_formula"] != "":
            if values["integral_start"] != "" and values["integral_end"] != "":
                #定積分
                formula = values["integral_formula"]
            
            elif values["integral_start"] == "" and values["integral_end"] == "":
                #不定積分
                formula = values["integral_formula"]

    #Clear
    elif event in clear_btn:
        if focus != "":
            window["{i}".format(i=focus)].update(space) #type:ignore

    #Waste
    elif event == "integral_btn":
        y= sympy.E ** (-2 * x) * sympy.sin(3 * x) #type:ignore
        result_tex = sympy.latex((sympy.integrate(y, x)).doit())

        F2 = x ** 5 + x + 1
        tex_result = sympy.latex((sympy.solve(F2, x)))

        #tex
        if multiline_formula_tex.do_not_clear == None:
            print(f" + ", tex_result) 
        else: print(tex_result)

        ##積分定数は加えずに表示
        latex_result = r"""$${tex}$$""".format(tex=tex_result)
        image_result = sympy.preview(latex_result, viewer="file", filename="result.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])
        print(f're'.format(result_tex))

        window["output_tex"].print(tex_result) #type:ignore
        print(f"途中式は、 ", values["output_tex"], " です。")

    elif event == 'limit_btn':
        print(f"pressed it")
        y = sympy.sin(x ** 2) / (E ** (-x) + 1)
        tex_result = sympy.latex(sympy.integrate(y, (x, -(Pi / 2), Pi / 2)).doit())
        latex_result = r"""$${tex}$$""".format(tex=tex_result)
        image_result = sympy.preview(latex_result, viewer="file", filename="result.png", euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600"])
        print(latex_result)
        #tex
        window["output_tex"].print(tex_result) #type:ignore

window.close()