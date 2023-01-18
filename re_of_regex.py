import re
from static.functions import *

#分数有式
string = r"\sin{\pi^{2}} － 1 / {x} = 25 ＋ e / {\pi ＋ {25 / {\cos{\theta}}}}"
#string = r"1 / {x ＋ \pi} = 25 ＋ e / {\pi ＋ {25 / 2021}}"
#string = r"100/{\pi ＋ e}"

print("[ Formula : ] ", string)

#分子中に於ける演算記号の有無
pattern = r"/\s*?{[^}]+[＋－]"
plus_in_frac = re.findall(pattern, string)
for i in plus_in_frac:
    plus = str(i).replace("＋", "+")
    string = string.replace(i, plus)
    print("Match: ", i, " || Pattern: ", pattern, " || 結果: ", string)

regex = r"[＋－=]"
split_formula = re.split(regex, string)
print("Split : ", split_formula)
#Split : Split :  ['1 / {x +(Edited) \\pi} ', ' 25 ', ' e / {\\pi +(Edited) {25 / 2021}}']

#項で分割
for i in split_formula:
    try:
        pattern = "[^/]+[^}]+"
        res = re.search(pattern, i).group() #type:ignore
        #分数がある場合
        if res.__contains__("/"):
            print("\n 分数: ", res)
            res = res.replace("\\\\", "")
            print("Before add \" \\ \" : ", res)
            res = res.replace("\\", "\\\\")
            bunshi_pattern = "[^{]+"
            frac = re.search(bunshi_pattern, res).group() #type:ignore
            bunshi = frac.replace("/", "")
            bunbo = res.replace(frac, "")
            bunbo = bunbo.lstrip("{").replace("+", "＋") + "}"
            print("\n分子 : ", bunshi, "\n分母 : ", bunbo)
            print("\n[ Result Match: ] \\frac{{{0}}}{{{1}".format(bunshi, bunbo))

            #\\pi + {25 / {\\cos{\\theta
            if bunbo.__contains__("/"):
                bunbo = bunbo.replace("\\\\", "\\")
                print("[Not edit yet]", bunbo)

                #分子中に於ける演算記号の有無
                pattern = r"/\s*?{[^}]+[＋－]"
                plus_in_frac = re.findall(pattern, bunbo)
                for i in plus_in_frac:
                    plus = str(i).replace("＋", "+")
                    bunbo = bunbo.replace(i, plus)
                    print("Match: ", i, " || Pattern: ", pattern, " || 結果: ", bunbo)

                regex = r"[＋－=]"
                split_formula = re.split(regex, bunbo)
                print("Split : ", split_formula)

    except:
        break

string = r"1 / {x ＋ \pi} = 25 ＋ e / {\pi ＋ {25 / 2021}}"
#print("関数: \n", transfer_frac(string))

##### Regex #####
# . : 任意の1文字
# * : 0回以上
# ? : なるべく少ない文字数でマッチ
# + : 文字列
# [^] : 特定の文字以外(1文字)
res = re.search("y[^def]+", "xyabcdefg")
#print("\n",res)