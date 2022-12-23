""" disabled=True でボタン自体の操作を無効化する"""
import PySimpleGUI as sg

sg.theme("Default1")
font = ('HGS明朝B', 24)
layout = [
    [sg.Button("press it first", key="first", font=font)],
    #初期設定は必須
    [sg.Button("PRESS IT SECOND", key="second", disabled=True, font=font)],
    [sg.Button("Press It Third", key="third", disabled=True, font=font)]]

window = sg.Window(title="Sample", layout=layout)

while True:
    event, values = window.read()#type:ignore
    if event is None:
        break
    elif event == "first":
        #updateで変更可
        window["second"].update(disabled=False)
    elif event == "second":
        window["third"].update(disabled=False)
    elif event == "third":
        window["first"].update(disabled=True)
        sg.PopupError("Successfully!!!", auto_close=True, auto_close_duration=3.141592653515, font=font)

window.close()