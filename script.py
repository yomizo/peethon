from janome.tokenizer import Tokenizer

t = Tokenizer()

str = "えな可愛いねぇ"

tokens = t.tokenize(str)

for token in tokens:
    print(token)

