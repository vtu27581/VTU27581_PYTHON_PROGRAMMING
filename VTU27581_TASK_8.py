det fibonacci (limit):

a, b=0,1

while a<= limit:

Yeild a

a,b = b, a+b

n=int (input ("enter the limit for fibonacci sequence: "))

print (f"fibonacci sequence up to {n}:") 

for num in fibonacci(n):

print (num,end =" ")
