import re

#分数有式
string = r"\sin{\pi^{2}} － 1 / {x} = 25 ＋ e / {\pi ＋ {25 / {\cos{\theta}}}}"
string = r"1 / {x ＋ \pi} = 25 ＋ e / {\pi ＋ {25 / 2021}}"

#分子の中に演算記号があるかどうか
pattern = r"/ {.*?[^}][＋－]" # / {.*? ＋－ .*?}

plus_in_frac = re.search(pattern, string).group() #type:ignore
plus = plus_in_frac.replace("＋", "+(Edited)")
print("分数中の演算: ", plus_in_frac)

string = string.replace(plus_in_frac, plus)
print(string)

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