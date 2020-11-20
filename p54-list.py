
lst = [10,20,30,40,50,60,30]
lst.remove(30)
print(lst)

lst.pop(1)
print(lst)

lst.pop()
print(lst)

new_list= lst[1:3]
print(lst)
print(new_list )

lst[1:3]=[]
print(lst)

lst.clear()
print(lst)

del lst
print(lst)
