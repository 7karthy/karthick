a=(input("fk"))
a=a.split()
b=[]
for i in a:
  b.append(i[::-1])
print("".join(b))
