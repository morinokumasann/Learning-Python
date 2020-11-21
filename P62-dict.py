
scores = {"TERU":1000,"ZARD":500,"HIDE":200}

print("HIDE" in scores)
print("HIDE" not in scores)

del scores["HIDE"]
print(scores)
#scores.clear()
print(scores)

scores["HI"]= 100
print(scores)