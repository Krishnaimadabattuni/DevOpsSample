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


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(4))
########################################

# av = 5
# x = int(input("How many Candies you want?"))
# i = 1
# while i <=x:
#     if i>av:
#         print("Out of stock")
#         break
#     print("candy")
#     i+=1
# print("Bye")

# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         continue
#     print(i)
# print("Bye")

for i in range(1,101):
    if(i%2!=0):
        pass
    else:
        print(i)
        
print("Bye")
   
  
































