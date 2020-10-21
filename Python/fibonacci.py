n = int(input("Enter a Number: "))

def fib(n):
    
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
        print(c)
fib(n)
    