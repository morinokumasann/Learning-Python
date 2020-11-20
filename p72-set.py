s = {10,20,30,40,100,520}
print(10 in s )
print(100 in s )
print(10 not in s )
print(100 not in s )

s.add(80)
print(s)

s.update({200,400,500})
print(s)

s.update([100,88,55])
s.update((78,75,57))
print(s)

s.remove(200)
print(s)

#s.remove(200)

s.discard(200)

s.pop()
print(s)
