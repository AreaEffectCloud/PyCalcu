import PySimpleGUI as sg

from app_statics.gui_layout import *
from app_statics.functions import *

sg.theme("Reddit")

##### ##### Layout  #####  #####

#must resize
image_formula_latex_column = sg.Column([
    [sg.Image(filename="output_images/formula.png", key="image_formula_latex", expand_y=True)]
    ], element_justification='c', vertical_alignment='center', expand_x=True, expand_y=True, visible=False)

#####   Tab Group #####
main_column_left_tabs = sg.TabGroup([[
    sg.Tab(normal[lang], normal_layout, key="normal"),
    sg.Tab(function[lang], function_layout, key="function"),
    sg.Tab(alphabet[lang], alphabet_layout, key="alphabet"),
    ]], font=FONT, expand_x=True)

main_column_right_tabs = sg.TabGroup([[
    sg.Tab(limit[lang], limit_layout, key="limit", font=FONT),
    sg.Tab(sigma[lang], sigma_layout, key="sigma", font=FONT),
    sg.Tab(diff[lang], differential_layout, key="diff", font=FONT),
    sg.Tab(integral[lang], integral_layout, key="integral", font=FONT),
    ]], font=FONT, expand_x=True)

#####   Output  #####
multiline_formula_tex = sg.Output(key='output_tex', font=FONT_output, pad=((0, 0), (0, 0)), size=(100, 5), expand_x=True)
output_frame = sg.Frame(output_frame_title[lang], [[multiline_formula_tex]], font=FONT_output, expand_x=True)

#レイアウト
gui_layout = [[output_frame], 
          [main_column_left_tabs, main_column_right_tabs],
          [image_formula_latex_column]
         ]

window = sg.Window(title[lang], gui_layout, icon="", use_default_focus=False, resizable=True, finalize=True)

set_bind(window)
# -------------------------------------
#           イベント毎の処理
# -------------------------------------
focus = ""
space = ""
index = 0
diff_selected = "x"
integral_selected = "dx"
while True:

    event, values = window.read() #type:ignore

    if event == sg.WIN_CLOSED:
        break
    #Diff / Change Image
    elif event in "diff_select":
        diff_selected = values["diff_select"]
        window["diff_img"].update(filename="images/diff/diff_{0}.png".format(diff_selected))

    #Integral /
    elif event in "integral_select":
        integral_selected = values["integral_select"]
        integral_selected = str(integral_selected).strip()

    #get Focus
    elif event in binds:
        focus = str(event).replace("+Input", "")
        print(focus)
        print(values["integral_select"])

    #All Clear
    elif event == "allclear":
        if focus in limit_tab:
            for box in limit_tab:
                window["{0}".format(box)].update(space) #type:ignore
        elif focus in sum_tab:
            for box in sum_tab:
                window["{0}".format(box)].update(space) #type:ignore
        elif focus in diff_tab:
            for box in diff_tab:
                window["{0}".format(box)].update(space) #type:ignore
        elif focus in integral_tab:
            for box in integral_tab:
                window["{0}".format(box)].update(space) #type:ignore
    
    #括弧含む
    elif event in brackets:
        if focus != "":
            text = values["{0}".format(focus)]
            text = text + window[event].get_text() + "(" #type:ignore
            window["{0}".format(focus)].update(text) # type: ignore
    #逆三角関数
    elif event in triangle_brackets:
        if focus != "":
            value = window[event].get_text().lstrip("a") #type:ignore
            text = values["{0}".format(focus)] + "arc" + value + "("
            window["{0}".format(focus)].update(text) # type: ignore

    #Other Bottons
    elif event in all_btns_keys:
        if focus != "":
            text = values["{0}".format(focus)]
            #values[event] occur error
            text = text + window[event].get_text() #type:ignore
            window["{0}".format(focus)].update(text) # type: ignore
    
    #2乗
    elif event in "power_twice":
        if focus != "":
            text = values["{0}".format(focus)]
            if text != "":
                text = text + "**(2)"
                window["{0}".format(focus)].update(text) # type: ignore
    
    #Add
    #極限
    elif event in "add_limit":
        if values["limit_formula"] != "":
            #All
            if values["limit_start"] != "" and values["limit_end"] != "":
                window["output_tex"].update(space) #type:ignore
                tex_start = transform_latex(values["limit_start"])
                tex_end = transform_latex(values["limit_end"])
                tex_formula = transform_latex(values["limit_formula"])

                limit_tex = r"""$$\lim_{{{0}\to{1}}}{{{2}}}$$""".format(tex_start, tex_end, tex_formula)
                print(limit_tex)
                autosize_latex(limit_tex)

            elif values["limit_start"] == "" and values["limit_end"] == "":
                window["output_tex"].update(space) #type:ignore
                #一般方程式
                tex = r"""$${0}$$""".format(transform_latex(values["limit_formula"]))
                print(tex)
                autosize_latex(tex)

    #数列
    elif event in "add_sum":
        if values["sum_formula"] != "":
            if values["sum_func"] != "":
                #関数のみの数列
                if values["sum_end"] == "" and values["sum_start"] == "":
                    window["output_tex"].update(space) #type:ignore
                    tex_func = values["sum_func"]
                    tex_formula = transform_latex(values["sum_formula"])

                    sum_func_tex = r"""$$\sum_{{{0}}}^{{}}{{{1}}}$$""".format(tex_func, tex_formula)
                    autosize_latex(sum_func_tex)

                #全て入力された状態
                elif values["sum_end"] != "" and values["sum_start"] != "":
                    window["output_tex"].update(space) #type:ignore
                    tex_func = transform_latex(values["sum_func"])
                    tex_start = transform_latex(values["sum_start"])
                    tex_end = transform_latex(values["sum_end"])
                    tex_formula = transform_latex(values["sum_formula"])

                    sum_tex = r"""$$\sum_{{{0}={1}}}^{{{2}}}{{{3}}}$$""".format(tex_func, tex_start, tex_end, tex_formula)
                    autosize_latex(sum_tex)

            elif values["sum_func"] == "" and values["sum_end"] == "" and values["sum_start"] == "":
                window["output_tex"].update(space) #type:ignore
                #一般方程式
                tex = r"""$${0}$$""".format(transform_latex(values["sum_formula"]))
                autosize_latex(tex)

    #微分
    elif event in "add_diff":
        if values["diff_formula"] != "":
            window["output_tex"].update(space) #type:ignore
            diff = transform_latex(values["diff_formula"])
            diff_tex = r"""$$\frac{{d}}{{d{0}}}{{{1}}}$$""".format(diff_selected, diff)
            autosize_latex(diff_tex)
            print(diff_tex)

    #積分   
    elif event in "add_integral":
        if values["integral_formula"] != "":
            if values["integral_start"] != "" and values["integral_end"] != "":
                window["output_tex"].update(space) #type:ignore
                #定積分
                tex_start = transform_latex(values["integral_start"])
                tex_end = transform_latex(values["integral_end"])
                tex_formula = transform_latex(values["integral_formula"])
                integral_int_tex = r"""$$\int\limits_{{{0}}}^{{{1}}}{{{2}}}{3}$$""".format(tex_start, tex_end, tex_formula, integral_selected)
                autosize_latex(integral_int_tex)
                print(integral_int_tex)

            
            elif values["integral_start"] == "" and values["integral_end"] == "":
                window["output_tex"].update(space) #type:ignore
                #不定積分
                tex_formula = transform_latex(values["integral_formula"])
                integral_tex = r"""$$\int{{{0}}}{1}$$""".format(tex_formula, integral_selected)
                autosize_latex(integral_tex)
                print(integral_tex)
                print(tex_formula)
                print(integral_selected)
                
    #Clear
    elif event in clear_btn:
        if focus != "":
            window["{i}".format(i=focus)].update(space) #type:ignore

window.close()