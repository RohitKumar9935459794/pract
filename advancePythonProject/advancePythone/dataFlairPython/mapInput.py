# here is the code of reading multiple varinble in single line
a,b=input('enter two number').split()
print(a+b)

a,b=map(int,input('enter the no')).split()
c=a+b
print(" Addition is %d and %d is %d"%(a,b,c))