import json
import sympy
from PIL import Image

##### config.json から設定の読み込み
#####
def get_json(path):
    with open(path, encoding="utf-8_sig") as json_file:
       f = json.load(json_file)
    return f

# Ex. {'user': [{'language': 'en', 'tex_multiline': 'True'}]

#LiteralString -> r"""$${result_tex}$$"""
#def autosize_latex(LiteralString):
    #行列
    #定積分
    #不定積分
    #数列
    #極限
    #数字