
lst = [10,20,30]
print(lst,id(lst))
lst.append(100)
print(lst,id(lst))
lst2 = ["hello","world"]
#lst.append(lst2)
#print(lst)
print("............")
lst.extend(lst2)
print(lst)
lst.insert(1,57)
print(lst)

lst3 = [True,False,"hello"]
lst[1:] = lst3
print(lst)