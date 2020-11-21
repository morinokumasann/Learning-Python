
lst =[10,20,30]
print(id(lst))
lst.append(100)
print(id(lst))

print("........................")

s="hello"
print(id(s))
s=s+"world"
print(id(s))
print(s)