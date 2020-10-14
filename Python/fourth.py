n = int(input("Enter a Number: "))
counter = 0
for i in range(1,n+1):
    if n%i == 0:
        counter = counter + 1

if counter == 2:
    print("Prime Number")
else:
    print("Not a prime number")        
    
    
# for i in range(5):
#     if i ==3:
#         break
#     print("Hello",i)

for i in range(5):
    for j in range(5):
        print("* ",end="")
    print()
    
    
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()
    
for i in range(5):
    for j in range(5-i):
        print("* ",end="")
    print()


num =int(input("ENter a number: "))

for i in range(2,num):
    if num % i ==0:
        print("Not a prime")
        break
else:
    print("Prime")
































