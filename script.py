from janome.tokenizer import Tokenizer #日本語形態素解析
import re #正規表現

gokugo = '([アカサタナハマラガザダバダ])[イエ]' #悟空語

#悟空辞書
keys = "ア,カ,サ,タ,ナ,ハ,マ,ラ,ガ,ザ,バ,ダ".split(",")
values = "え,け,せ,て,ね,へ,め,れ,げ,ぜ,べ,で".split(",")
dic = dict(zip(keys, values))

with open('wagahaiwa_nekodearu.txt', encoding="cp932") as f:
    data = f.read()

t = Tokenizer()

tokens = t.tokenize(data)
sentence = ""
cnt = 0

for token in tokens:
    text = token.reading #ヨミガナ代入
    if (re.search(gokugo, text)):
        for s in re.findall(gokugo, text):
            text = text.replace(s, dic[s] + "ぇ", 1)
        text = text.replace("ぇイ", "ぇ")
        text = text.replace("ぇエ", "ぇ")
        sentence += text.strip()
    else:
        sentence += token.surface.strip()
    cnt += 1
    if cnt == 1000:
        break

print(sentence)
