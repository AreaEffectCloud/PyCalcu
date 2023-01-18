import re

#分数有式
string = r"\sin{\pi^{2}} － 1 / {x} = 25 ＋ e / {\pi ＋ {25 / {\cos{\theta}}}}"
string = r"1 / {x ＋ \pi} = 25 ＋ e / {\pi ＋ {25 / 2021}}"

#分子中に於ける演算記号の有無
pattern = r"/ {[^}]+[＋－]"
plus_in_frac = re.findall(pattern, string)
for i in plus_in_frac:
    plus = str(i).replace("＋", "+(Edited)")
    string = string.replace(i, plus)
    print("Match: ", i, " || Pattern: ", pattern, " || 結果: ", string)

regex = r"[＋－=]"
split_formula = re.split(regex, string)
print("Split : ", split_formula)
#Split :  

##### Regex #####
# . : 任意の1文字
# * : 0回以上
# ? : なるべく少ない文字数でマッチ
res = re.search("y[^def]+", "xyabcdefg")
print("\n",res)