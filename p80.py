

s="hello world Python"
lst=s.split()
print(lst)

s1 ="hello|world|Python"
print(s1.split(sep="|",maxsplit=1))

print("..........................")

print(s.rsplit())
print(s1.rsplit("|"))
print(s1.rsplit(sep="|",maxsplit=1))
