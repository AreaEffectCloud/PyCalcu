from .functions import get_json
#En and Jp
## load a config.json file | Get setting of language
config = get_json("config.json")
lang = config['user']['language']

#Window title
title = { 'en':str('Function Application'), 'ja':str('関数アプリ') }

#Tex Multiline
output_frame_title = { 'en':str('Output'), 'ja':str('出力') }

#Tab title
normal = { 'en':str('Normal'), 'ja':str('一般')}
function = { 'en':str('Function'), 'ja':str('関数')}
alphabet = { 'en':str('Alphabet'), 'ja':str('アルファベット')}
limit = { 'en':str('Limit'), 'ja':str('極限')}
sigma = { 'en':str('Sum'), 'ja':str('数列')}
diff = { 'en':str('Differential'), 'ja':str('微分')}
integral = { 'en':str('Integral'), 'ja':str('積分')}
top = { 'en':str('Top'), 'ja':str('上端')}
bottom = { 'en':str('Bottom'), 'ja':str('下端')}

add = { 'en':str('Export'), 'ja':str('生成')}
clear = { 'en':str('Clear'), 'ja':str('クリア')}