# OOP concepts using classes , inheritance,encapsulation and theoratical concept of abstraction
# Banking example
print("X")

# list
# x=[2,3,4,5,6,7,False,"Hello"]
# print(x)
# print(len(x))
# print(type(x))
# print(x[0])

# print(x[-8])
# print(x[0:2]) # slicing
# print(x[2:])
# print(x[:5])

# find value from list
# x=[2,3,4,5,22.2,33,31,False,"Hello"]
# if False in x:
#     print("yes")
# else:
#     print("no")


# change 
# x=[2,3,4,5,22.2,33,31,False,"Hello"]
# x[-1]=100
# print(x)

# x[2:4]=[100,200,300]
# print(x)


# add
# x=[3,4,333,321]
# x.insert(0,"hello") 
# print(x)

# a=[1,2,3,4,5,6,7]
# x=[3,2,4,2,1,3,4,2,1,3455555]
# x.append(True)
# x.insert(3,"hello")
# print(x)

# a.extend(x)

# print(a)
# x.extend(a)


# sorting

# x=[4,2,46,1,0,2,221]
# x.sort()  # sort the list
# print(x)
# x.sort(reverse=True)  # sort the list in reverse order
# print(x)
# x.reverse()  # reverse the list
# print(x)

# remove / delete/pop

# a=[1,2,3,4,5,6,7]
# a.remove(3)  remove the value
# print(a)
# a=[1,2,3,4,5,6,7]
# a.pop(3)  # pop index
# print(a)
# # or

# del a[4]
# print(a)

# a=[1,2,3,4,5,6,7]
# del a
# print(a)

# x=[44,33214,313,2424,2,43]
# x.clear()
# print(x)




# tuple
# x=(2,3,4,5,63,2,2,"Hello")
# # tuples are immutable so if i want to change you first convert it into list and then change it and then convert it back to tuple
# y=list(x)
# print(y)
# y[2]="welcome"
# y.append(True)
# x=tuple(y)
# print(x)


# same scnerio for the remove

# now add tuple into a tuple
# x=(2,3,4,5,63,2,2,"Hello")
# y=(1,2,3,4,5,6,7)

# x+=y
# print(x)


# dictionary

# x={
#     "name":"Abdullah",
#     "age":21,
#     "semester":7,
#     "fav food":["pizza", "burger"],
#     "grades": {
#         "A":90,
#         "B":80,
#         "C":70
#     }
# }

# print(x)
# print(type(x))
# # to access name without any error
# print(x.get("name")) 
# x["grades"]["B"]=81
# print(x)
# x["name"]="Abdullah Jawaid"
# print(x)

# x["fav hobby"]=["coding", "gaming"]
# print(x)

# x.update({"fav food":["pizza", "burger", "pasta"]})
# print(x)

# methods
# print(x.keys())
# print(x.values())
# print(x.items())
# print(list(x.keys( )))
# print(list(x.values( )))
# print(list(x.items( )))
# print(len(list(x.keys( ))))


# exercise for dictionary
# q1

# marks={}
# x=int(input("Enter the number of students: "))
# marks.update({"Phy":x})
# y=int(input("Enter the number of subjects: "))
# marks.update({"Maths":y})
# z=int(input("Enter the number of marks: "))
# marks.update({"Chem":z})
# print(marks)


# list exercise ex 1

# mov=[]
# mov.append(str(input("Enter the number of movies: ")))
# mov.append(str(input("Enter the number of movies: ")))
# mov.append(str(input("Enter the number of movies: ")))
# mov.append(str(input("Enter the number of movies: ")))
# mov.append(str(input("Enter the number of movies: ")))
# print(mov)



# q2

# x=[3,2,3,3]
# y=x.copy()
# print(y)
# y.reverse()
# print(y)
# if x==y:
#     print("Palindrome")
# else:
#     print("Not Palindrome")




# example

# stdrecords={
#     "name":{"Abdullah","Ahsan","Ali","tayyab"},
#     "age":{21,22,23,24},
#     "semester":{7,7,7,7}

# }

# print(stdrecords["name"])


# stdrec=[
#     {
#         "name":"Abdullah",
#         "age":21,
#         "semester":7
#     },
#     {
#         "name":"Ahsan",
#         "age":22,
#         "semester":7
#     },
#     {
#         "name":"Ali",
#         "age":23,
#         "semester":7

#     }

# ]

# print(stdrec[0]["name"])
# stdrec[1]["name"]="Talha"
# print(stdrec)

# x={
#     "name":"Abd",
#     "age":24,
#     "semester":6

# }

# stdrec.append(x)
# print(stdrec)

# x={}
# name=input("Enter the name: ")
# x.update({"name":name})
# age=int(input("Enter the age: "))
# x.update({"age":age})
# semester=int(input("Enter the semester: "))
# x.update({"semester":semester})

# print(x)

# stdrec.append(x)
# print(stdrec)





# i=1
# while(i<=29):
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=100
# while(i>=1):
#    print(i)
#    i-=1

# n=int(input("Enter any number"))
# i=1
# while(i<=10):
#     print(n*i)
#     i+=1

# n=[2,3,4,5,2,1,4,5411]
# i=1
# while (i<len(n)):
#     print(n[i])
#     i+=1

# n=[2,3,4,5,6,3,1]
# c=28
# i=0
# while(i<len(n)):
#     if(n[i]==c):
#         print("Found at index",i)
#         break
#     else:
#         print("finding")
#         i+=1
    

# x="Hell"
# for a in x:
#     if(a=="e"):
#         print("Found")
#         break
#     print(a)

# x=[2,3,4,2,1,2]
# for i in x:
#     print(i)



# for x in range(1,9,1):
#     if(x==3):
#         break
#     else:
#         print("found")

# x=int(input("Enter your no"))
# for i in range(1,11,1):
#     print(x*i)
    


# list comprehension

# n=[2,3,2,1]
# res=[i for i in n ]


# n = int(input("Enter a no"))

# for i in range(2, n):
#     if n % i == 0:
#         print("not a pn")
#         break
# else:
#    print("prime no")





# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# fib = []

# for i in range(n):
#     fib.append(a)

#     c = a + b
#     a = b
#     b = c

# # x = [10, 20, 30, 40, 50]

# a = x[0]
# b = x[1]

# fib = [a, b]

# for i in range(5):
#     c = a + b
#     fib.append(c)
#     a = b
#     b = c

# print(fib)


# numbers = [10, 20]

# for i in range(3):
#     numbers.append(numbers[-1] + numbers[-2])

# print(numbers)



# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# fib = []

# for i in range(n):
#     fib.append(a)

#     c = a + b
#     a = b
#     b = c

# print(fib)


# x=int(input("Enter a no"))
# a=0
# b=1
# f=[]
# for i in range(x):
#     f.append(a)
#     c=a+b
#     a=b
#     b=c
# print(f)









# prime no from a list identify

# n = [1, 23, 234, 23, 245, 9]

# for num in n:

#     for i in range(2, num):

#         if num % i == 0:
#             print(num, "is not a prime number")
#             break

#     else:
#         print(num, "is a prime number")


# num=[]
# for i in range(5):
#     x=int(input("Enter a number"))
#     num.append(x)

# print(num)
# for x in num:
#     if x<2:
#         print("Numbers less than 2 are not prime no")
#     else:
#         for i in range(2,x):
#             if x%i==0:
#                 print(x,"NO its not a prime no")
#                 break
#         else:
#             print(x,"Yes its a prime number")



# functions

# def sum(a,b):
#     return a+b

# print(sum(21,3))



# def avg(a,b,c):
#     sum=a+b+c
#     x=sum/3
#     print(x)
#     return(x)
# print(avg(5,5,5))


# def mul(a,d):
#     c=a*d
#     print(c)
#     return c
# mul(2,3)

# def sq(n):
#     return n*n
# print(sq(4))

# def e_o(n):
#     if n%2==0:
#        return "even number"
#     else:
#         return "odd number"

  
# print(e_o(1))
# print(e_o(7))


# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(max(2,3))


# def ctof(c):
#     f =(c * 9/5) + 32
#     return f
# print(ctof(5))

# x=int(input("enter a number"))
# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f*=i
#         print(f)
# fact(x)

# n=[10,20,3,5,3]
# def countw(n):
#      return len(n)
# print(countw(n))

# n = [10, 20, 30, 2, 20, 22022222, 32442445]

# def larg(n):
#     largest = n[0]

#     for i in n:
#         if i > largest:
#             largest = i

#     return largest

# print(larg(n))


# def cal(a,b):
#     c=a+b
#     s=a-b
#     e=a/b
#     r=a*b
#     return c,s,e,r
# print(cal(10,5))

# sq=lambda x: x*x
# cube=lambda a:a*a*a
# add=lambda a,b: a+b
# e_o=lambda x:  x%2==0
# g=lambda a,b: a if a>b else b
# ctof=lambda c: (c*9/5) + 32

# import math
# print(math.sqrt(144))
# x=int(input("Enter a number"))
# area=math.pi * x**2
# cir=2*math.pi * x
# import random
# print(random.randint(1,10))
# import datetime
# print(datetime.datetime.now())




# import math
# a=int(input("Enter a number"))
# b=float(input("Enter another no"))

# print(math.sqrt(a))
# print(math.sqrt(b))
# print(math.pow(a,b))
# print(math.factorial(a))
# print(math.ceil(b))
# print(math.floor(b))

# import random
# for i in range(1,6):
#     print(random.randint(1,100))
# print(random.randint(1,10))


# import datetime
# print(datetime.datetime.now())


# import statistics
# n=[10,20,30,40,40,502,10]
# print(statistics.mean(n))



# day 4 task
# import math
# import random
# import datetime
# import statistics
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# sq=lambda a: a*a
# def cube(b):
#     return b*b*b
# def factorial(a):
#     if a==0 or a==1:
#         return a 
    
#     return a * factorial(a-1)

# is_even=lambda b: b%2==0

# while True: 
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Square")
#     print("6. Cube")
#     print("7. Factorial")
#     print("8. Check Even")
#     print("9. Square Root")
#     print("10. Power")
#     print("11. Ceiling")
#     print("12. Floor")
#     print("13. Random Number")
#     print("14. Date time")
#     print("15. Mean")
#     print("16. Exit")

#     ch=int(input("Select any of the number for the desired operation"))
#     if ch==1:
#         x=int(input("Enter 1st num"))
#         y=int(input("Enter 2nd num"))
#         print(add(x,y))
#     elif ch==2:
#         x=int(input("Enter 1st num"))
#         y=int(input("Enter 2nd num"))
#         print(sub(x,y))
#     elif ch==3:      
#         x=int(input("Enter 1st num"))
#         y=int(input("Enter 2nd num")) 
#         print(mul(x,y))
#     elif ch==4:  
#         x=int(input("Enter 1st num"))
#         y=int(input("Enter 2nd num"))
#         print(div(x,y))
#     elif ch==5:
#         x=int(input("Enter the num"))
#         print(sq(x))
#     elif ch==6:
        
#         y=int(input("Enter the num"))
#         print(cube(y))
#     elif ch==7:
#         x=int(input("Enter the num"))

#         print(factorial(x))
#     elif ch==8:
       
#         y=int(input("Enter the num"))
#         print(is_even(y))
#     elif ch==9:
#         x=int(input("Enter the num"))

#         print(math.sqrt(x))
#     elif ch==10:
#         x=int(input("Enter 1st num"))
#         y=int(input("Enter 2nd num"))
#         print(math.pow(x,y))
#     elif ch==11:
       
#         y=float(input("Enter the num"))
#         print(math.ceil(y))
#     elif ch==12:
     
#         y=float(input("Enter the num"))
#         print(math.floor(y))
#     elif ch==13:
#         x=int(input("Enter 1st num"))
#         y=int(input("Enter 2nd num"))
#         print(random.randint(x,y))
#     elif ch==14:
     
#         print(datetime.datetime.now())
#     elif ch==15:
#         num=[]
#         for i in range(4):
#             z=int(input("Enter the  numbers"))
#             num.append(z)
#         print(statistics.mean(num))
#     elif ch==16:
#         print("Exiting the program")
#         break 
     

#     else:
#         print("Invalid choice")

#     again=input("Do you want to continue? (y/n)")
#     if again=="n":
#         print("Completed")
#         break
#     elif again == "y":
#         continue 

#     else:
#      print("Invalid input")
#      break




# def countdowm(a):
#     if a==0:
#         return
    
#     print(a)
#     countdowm(a-1)
# countdowm(x)
# def up(b):

#     if b == 5:
#         return

#     print(b)
#     up(b + 1)

# up(1)
# def fab(a):
#     if a<=1:
#         return a
#     return fab(a-1) + fab(a-2)
# print(fab(x))

# just an example for error handling

# elif ch==4:
#     try:
#         x=int(input("Enter 1st num"))
#         y=int(input("Enter 2nd num"))
#         print(div(x,y))
#     except ValueError:
#         print("Please enter numbers only")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")



# oop concepts

# class std:
#     name="Abdullah"
# s=std()
# print(s.name)

# class car:
#     def __init__(self,name,brand,color):

#         self.name=name
#         self.brand=brand
#         self.color=color
# c=car("Corolla","Toyota","brown")
# print(c.name,c.brand,c.color)

# class avg:
#     def __init__(self,marks):
#         self.marks=marks
#     def calavg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#             print( "and their avg is ",sum/3)
# c=avg([44,33,22])
# print(c.marks)
# c.calavg()

# class car:
#     def __init__(self,nam):
#         self.name=nam

# class brand(car):
#     def __init__(self,brand,nam):
#         super().__init__(nam)

        
class bankaccount:
    def __init__(self,name,accountno,balance):
        self.name=name
        self.__accountno=accountno
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdrawl(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")
    def get_bal(self):
        return self.__balance
    def set_bal(self,amount):
         self.__balance=amount
    def get_accountno(self):
           return self.__accountno
        
   
        
    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.__accountno)
        print("Remaining Balance:", self.__balance)

       

class savingacc(bankaccount):
    def __init__(self,name,accountno,balance,interestrate):
        super().__init__(name,accountno,balance)
        self.interestrate=interestrate
    def add_interest(self):
        interest=self.get_bal()*self.interestrate/100
        self.set_bal(self.get_bal() + interest)
    def display(self):
        super().display()
        print("Interest rate is ",self.interestrate)
        
class currentacc(bankaccount):
        def __init__(self,name,accountno,balance,extralimit):
            super().__init__(name,accountno,balance)
            self.extralimit=extralimit
        def withdrawl(self, amount):
            if amount<=self.get_bal()+self.extralimit:
                self.set_bal(self.get_bal()-amount)
            else:
                print("Limit exceeds")
        def display(self):
            super().display()
            print("Extra limit is ",self.extralimit)
accounts = []
while True:           
    print("         Banking System             ")
    print("1. Open Saving Account")
    print("2. Open Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Display Account")
    print("6. Exit")         

    ch=int(input("Select any number"))
    if ch==1:
        print("Saving account selected")
        name=input("Enter your name")
        accountno=input("Enter your account no")
        if len(accountno)<8:
            print("Account now must have alteast 8 digits")
            continue

        balance=float(input("Enter the balance"))
        interestrate=float(input("Enter interest rate"))

        ac=savingacc(name,accountno,balance,interestrate)
        accounts.append(ac)
        print("Account created successfully")
        ac.display()

    elif ch==2:
        print("Current account Selected")
        name=input("Enter your name")
        accountno=input("Enter your account no")
        if len(accountno)<8:
            print("Account now must have alteast 8 digits")
            continue
        
        balance=float(input("Enter the balance"))
        extralimit=float(input("Enter the extra limit"))
        ac = currentacc(name, accountno, balance, extralimit)
        accounts.append(ac)
        print("Account created successfully")
    elif ch==3:
        accountno=input("Enter account number")
        found=False
        for account in accounts:
            if account.get_accountno()==accountno:
                amount=float(input("Enter the amount you want to deposit"))
                ac.deposit(amount)
                print("Amount deposit successfully" )
                print("Remainig balance is ",ac.get_bal())
                found=True
                break
        if found==False:
            print("Account no not found")
    elif ch==4:
        accountno=input("Enter account no")
        found=False
        for account in accounts:
            if account.get_accountno()==accountno:
                amount=float(input("Enter the amount you want to withdraw"))
                ac.withdrawl(amount)
                print("New balance is ",ac.get_bal())
                found=True
        if found==False:
            print("Account not found")

    elif ch==5:
        accountno = input("Enter account number: ")
        found=False
        for account in accounts:
            if account.get_accountno()==accountno:
                account.display()
                found=True
                break
        if found==False:
                 print("Account not found")
       
               
        


    elif ch==6:
        print("Thank you for using bank")
        break
    else:
        print("Invalid choice")
        


