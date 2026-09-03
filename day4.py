# Functions & Modules 
# Function(Recursive) , Modules, lambdas
# Exercise is Math utilities
# day 4 task
import math
import random
import datetime
import statistics
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
sq=lambda a: a*a
def cube(b):
    return b*b*b
def factorial(a):
    if a==0 or a==1:
        return a 
    
    return a * factorial(a-1)

is_even=lambda b: b%2==0

while True: 
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Factorial")
    print("8. Check Even")
    print("9. Square Root")
    print("10. Power")
    print("11. Ceiling")
    print("12. Floor")
    print("13. Random Number")
    print("14. Date time")
    print("15. Mean")
    print("16. Exit")

    ch=int(input("Select any of the number for the desired operation"))
    if ch==1:
        x=int(input("Enter 1st num"))
        y=int(input("Enter 2nd num"))
        print(add(x,y))
    elif ch==2:
        x=int(input("Enter 1st num"))
        y=int(input("Enter 2nd num"))
        print(sub(x,y))
    elif ch==3:      
        x=int(input("Enter 1st num"))
        y=int(input("Enter 2nd num")) 
        print(mul(x,y))
    elif ch==4:  
        x=int(input("Enter 1st num"))
        y=int(input("Enter 2nd num"))
        print(div(x,y))
    elif ch==5:
        x=int(input("Enter the num"))
        print(sq(x))
    elif ch==6:
        
        y=int(input("Enter the num"))
        print(cube(y))
    elif ch==7:
        x=int(input("Enter the num"))

        print(factorial(x))
    elif ch==8:
       
        y=int(input("Enter the num"))
        print(is_even(y))
    elif ch==9:
        x=int(input("Enter the num"))

        print(math.sqrt(x))
    elif ch==10:
        x=int(input("Enter 1st num"))
        y=int(input("Enter 2nd num"))
        print(math.pow(x,y))
    elif ch==11:
       
        y=float(input("Enter the num"))
        print(math.ceil(y))
    elif ch==12:
     
        y=float(input("Enter the num"))
        print(math.floor(y))
    elif ch==13:
        x=int(input("Enter 1st num"))
        y=int(input("Enter 2nd num"))
        print(random.randint(x,y))
    elif ch==14:
     
        print(datetime.datetime.now())
    elif ch==15:
        num=[]
        for i in range(4):
            z=int(input("Enter the  numbers"))
            num.append(z)
        print(statistics.mean(num))
    elif ch==16:
        print("Exiting the program")
        break 
     

    else:
        print("Invalid choice")

    again=input("Do you want to continue? (y/n)")
    if again=="n":
        print("Completed")
        break
    elif again == "y":
        continue 

    else:
     print("Invalid input")
     break


