
s = "hello,python"
l =s.upper()
print(l,id(l))
print(s,id(s))
b=s.lower()
print(b,id(b))
print(s,id(s))
print(b==s)
print(b is s)

s2 ="hello,Python"
print(s2.swapcase())

print(s2.title())