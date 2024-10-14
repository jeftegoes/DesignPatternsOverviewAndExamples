from sentence import Sentence

s = Sentence('alpha beta gamma')
s[1].capitalize = True
print(s)
