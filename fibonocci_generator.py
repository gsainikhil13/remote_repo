# To generate fibonacci number less than n
def fibonacci_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

g = fibonacci_generator()
n= int(input('enter number up to which the fibonacci number are required : '))
for x in g:
    if x<= n:
        print(x)
    else:
        break
 


 



 
# To generate first n fibonacci numbers
def fibonacci_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

g = fibonacci_generator()
count=1
n= int(input('enter number of fibonacci number required : '))
while count <= n:
    print(next(g))
    count= count+1


