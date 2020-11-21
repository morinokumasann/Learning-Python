
s1 ={10,20,30,40}
s2 ={40,30,20,10}

print(s1 == s2)
print(s1 != s2)

print("...........................")

s1 ={10,20,30,40,50,60}
s2 ={10,20,30,40}
s3 ={10,20,90}

print(s2.issubset(s1))
print(s3.issubset(s1))

print("............................")

print(s1.issuperset(s2))
print(s1.issuperset(s3))

print(".............................")

print(s2.isdisjoint(s3))
s4 ={100,200,300}

print(s2.isdisjoint(s4))