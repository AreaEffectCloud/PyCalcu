import json

##### config.json から設定の読み込み
#####
def get_json(path):
    with open(path, encoding="utf-8_sig") as json_file:
        f = json.load(json_file)
    return f

# Ex. {'user': [{'language': 'en', 'tex_multiline': 'True'}]