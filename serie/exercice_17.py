s = input("Donnez un phrase ou un mot : ")
ma_dictionnaire = dict()
for i in s:
    ma_dictionnaire[i] = 0

for i in s:
    ma_dictionnaire[i] += 1


for lettre in ma_dictionnaire :
    print(f"La lettre {lettre} figure {ma_dictionnaire[lettre]} fois")
