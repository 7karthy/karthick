a=int(input("range:"))
k=int(input("check:"))
b=[]
for i in range(a):
  c=int(input("enter the values:"))
  b.append(c)
if k in b:
  print("yes")
else:
  print("no")
