from static.functions import *

#En and Jp
## load a config.json file | Get setting of language
config = get_json("static/config.json")
lang = config['user']['language']

#Window title
title = { 'en':str('Calculator'), 'ja':str('関数電卓') }

#Edit image
right_click_menu_en = ['&Right', ["Copy", "Paste"]]
right_click_menu_ja = ['&Right', ["コピー", "貼り付け"]]
click_menu = { 'en':right_click_menu_en, 'ja':right_click_menu_ja}

#Tex Multiline
output_frame_title = { 'en':str('Output'), 'ja':str('出力') }

#Tab title
normal = { 'en':str('Normal'), 'ja':str('一般')}
function = { 'en':str('Functions'), 'ja':str('関数')}
alphabet = { 'en':str('Alphabet'), 'ja':str('アルファベット')}
limit = { 'en':str('Limit'), 'ja':str('極限')}
sigma = { 'en':str('Sigma'), 'ja':str('数列')}
diff = { 'en':str('Differential'), 'ja':str('微分')}
integral = { 'en':str('Integral'), 'ja':str('積分')}
top = { 'en':str('Top'), 'ja':str('上端')}
bottom = { 'en':str('Bottom'), 'ja':str('下端')}
matrix = { 'en':str('Matrix'), 'ja':str('行列')}
rows = { 'en':str('Rows'), 'ja':str('行')}
columns = { 'en':str('Columns'), 'ja':str('列')}