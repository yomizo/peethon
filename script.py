from janome.tokenizer import Tokenizer

t = Tokenizer()

str = "代替の効かない状態を換える"

tokens = t.tokenize(str)

for token in tokens:
    print(token)

