# for x in range(10):
#     print(x)
#     if x == 5:
#         break
    
# for y in range(10):
#     if y == 5:
#        break
#     print(y)
       
# for y in range(10):
#     if y == 5:
#        continue
#     print(y)
    
    
##functions

def wish(name, msg):
    print(name, msg)
    
wish("Krishna", "How are you")
wish("Krishna", "Where are you")

def getdata():
    print("Welcome to function")
    return 3.14,85
pi,a = getdata()
print(pi,a)


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))