numbers=[1,2,3]

a,b,c=numbers
print(a)
print(b)
print(c)

a,_,_=numbers
print(a)

a,*b=numbers
print(a)
print(b)