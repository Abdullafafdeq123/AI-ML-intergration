# Day 3 Control Flows If else , Loops and List comprehension
# Exercise Fabonachii & Prime Numbers


# Prime Number
# 1
# x=int(input("Enter a number"))
# if x<2:
#     print("No less than 2 are not the prime numbers")
# else:
#     for i in range(2,x):
#      if x%i==0:
#         print("No it's not a prime number")
#         break
#     else:
#      print("It's a prime number")
  
# 2

# num=[]
# for i in range(7):
#     a=int(input("Enter a number"))
#     num.append(a)

# for a in num:
#     if a<2:
#         print(a,"Num less than 2 are not the prime numbers")

#     else:
#         for i in range(2,a):
#             if a%i==0:
#                 print(a, "is not a prime number")
#                 break
#         else:
#             print(a, "is a prime number")


# Fabonaciii
# 1
# a=int(input("Enter First number"))
# b=int(input("Enter the second number"))
# num=[a,b]
# for i in range(8):
#     c=a+b
#     num.append(c)
#     a=b
#     b=c
# print(num)


# 2
# a=int(input("Enter First number"))
# b=int(input("Enter the second number"))
# num=[a,b]
# for i in range(8):
#     c=num[-1]+num[-2]
#     num.append(c)
# print(num)