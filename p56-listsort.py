
lst =[10,30,50,60,20]
print(lst,id(lst))
lst.sort()
print(lst,id(lst))

print("............")

'''lst.sort(reverse=True)
print(lst)

lst.sort(reverse=False)
print(lst)'''

new_lst = sorted(lst)

print(new_lst)