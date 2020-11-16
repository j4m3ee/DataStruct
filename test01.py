def printN(n):
    if n != 0:
        print(n)
        printN(n-1)

def factorial(n):
    return n * factorial(n-1) if n != 1 else n

def summation(n):
    return n + summation(n-1) if n != 1 else n

def fibonacci(n):
    return 0 if n == 1 else 1 if n == 2 else fibonacci(n-1) + fibonacci(n-2) 

n = int(input('Enter number : '))
print("fac :",factorial(n))
print("sum :",summation(n))

print("fib :",fibonacci(n))

fib=[]
for i in range(1,n+1):
    fib.append(fibonacci(i))
print(' '.join(str(i) for i in fib))