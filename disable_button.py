import re
#分数有式
string = r"\sin{x^{2}} / {e^{\pi}}"
string = r"\sin{\pi^{2}} － 1 / {x} = 25 ＋ e / {\pi ＋ {25 / {\cos{\theta}}}}"

pattern = r"[＋－][^/]+[^}]+"
#演算記号で分割 -> 分数の抽出
split_formula = re.split(r"[＋－=]", string)
print("Split : ", split_formula)
#Split :  ['\\sin{\\pi^{2}} ', ' 1 / {x} ', ' 25 ', ' e / {\\pi / {25 / {\\cos{\\theta}}}}']

#項で分割
for i in split_formula:
    try:
        pattern = "[^/]+[^}]+"
        res = re.search(pattern, i).group() #type:ignore
        
        #更に分数がある場合
        if res.__contains__("/"):
            print("\n", res)
            res = res.replace("\\", "\\\\")
            bunshi_pattern = "[^{]+"
            frac = re.search(bunshi_pattern, res).group() #type:ignore
            bunshi = frac.replace("/", "")
            bunbo = res.replace(frac, "")
            bunbo = bunbo.lstrip("{")
            print("\n分子 : ", bunshi, "\n分母 : ", bunbo)
            print("\n \\frac{{{0}}}{{{1}".format(bunshi, bunbo))

            #if bunbo.__contains__("/"):
    except:
        break

# \frac{e  }{{\pi / {25 / {\cos{\theta

""" disabled=True でボタン自体の操作を無効化する"""
import PySimpleGUI as sg

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