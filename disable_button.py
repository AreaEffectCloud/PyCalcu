""" disabled=True でボタン自体の操作を無効化する"""
import PySimpleGUI as sg

import re
string = r"\sin{x^{2}} ＋ e / {\pi / {25 / {\cos{\theta}}}}"
#pattern = "[＋－×]{1} [^/]+ [/] [{] [^/]+ [}]"
pattern = "[＋－][^/]+[^}]+"

res = re.search(pattern, string)
print(res, " || ", pattern)
#match='＋ e / {\\pi / {25 / {\\cos{\\theta'

#分子
numerator = ""
#分母
denominator = ""
frac = res.group().replace("", "") #type:ignore

#\frac{分子}{分母}

sg.theme("Default1")
font = ('HGS明朝B', 24)
layout = [
    [sg.Button("press it first", key="first", font=font)],
    [sg.Input("", key="IN")],
    [sg.In()],
    #初期設定は必須
    [sg.Button("PRESS IT SECOND", key="second", disabled=True, font=font)],
    [sg.Button("Press It Third", key="third", disabled=True, font=font)]]

window = sg.Window(title="Sample", layout=layout, finalize=True)
window["IN"].bind('<FocusIn>', '+FOCUS IN+')

while True:
    event, values = window.read()#type:ignore
    if event is None:
        break
    elif event == "first":
        #updateで変更可
        window["second"].update(disabled=False)

        text = "\\sin^{2}{\\left(x \\right)} - \\cos^{2}{\\left(x \\right)}"

        tex = text.replace("\\\\", "\\")
        #三角関数
        tex = tex.replace("sin", "\\sin").replace("cos", "\\cos").replace("tan", "\\tan")
        #逆三角関数
        tex = tex.replace("asin", "\\arcsin").replace("acos", "\\arccos").replace("atan", "\\arctan")
        print(tex)

    elif event in 'IN+FOCUS IN+':
        sg.popup_ok('フォーカスされました。')
        break
    elif event == "second":
        window["third"].update(disabled=False)
    elif event == "third":
        window["first"].update(disabled=True)
        sg.PopupError("Successfully!!!", auto_close=True, auto_close_duration=3.141592653515, font=font)

window.close()