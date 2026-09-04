# file handling,exception handling
# here is the practice

# f=open("demo.txt","x")
# f.close()
# f=open("demo.txt","w")
# f.write("Hello my name is abdullah")
# f.close()
# f=open("demo.txt","a")
# f.write("I am currently in six sem")
# f.close()

# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()

# f=open("demo.txt","a")
# f.write("I am")
# f.close()

# with open("demo.txt","r") as f:
#     print(f.read())
# with open("demo.txt") as f:
#     print(f.read(4))
# with open("demo.txt") as f:
#     print(f.readline())
# f=open("demo.txt") 
# print(f.readlines())

# # to delete the file
# import os 
# if os.path.exists("demo1.txt"):
#     os.remove("demo1.txt")
# else:
#     print("file doesnt exixts")
#  to deelete the entire folder use os.rmdir()
# you can only rmove empty folders
# os.rmdir("New Folder (5)")

# import os 
# # os.remove("demo.txt")
# os.remove("h.py")

# with open("demo.txt","w") as f:
#     f.write("Hello I am Abdullah.\nI am in six semster.\nI am working on ai ml intergration")

# with open("demo.txt") as f:
#     print(f.read())

# f=open("demo.txt","a")
# f.write("I am 21 years old.\nCurrently persuaing bscs")
# f.close()
# with open("demo.txt","r") as f:
#     print(f.readline())

# import os
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
# else:
#     print("file doesnt exixts")

# try:
#     age=int(input("enter your age"))
# except:
#     print("Plz enter valid value")
# try:
#     x=int(input("Enter 1st num"))
#     y=int(input("Enter 2nd num"))
#     c=x/y
#     print(c)
# except ValueError:
#     print("enter valid value")
# except ZeroDivisionError:
#     print("Canoot divide by 0")

# try:
#     with open("abc.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("file doesnt exixts")

# try:
#     x=10
#     y=3
#     print(x+y)

# except TypeError:
#     print("2 values with the diff types cannot be operated")

# try:
#     x=[10,20,30]
#     print(x[5])
# except IndexError:
#     print("Index doesnt exixts")
    
# try:
#     x={
#         "name":"Abdullah"
        
#     }
#     print(x["AGE"])
# except KeyError:
#     print("Key doenst exixts")

# try:
#     x=int(input("enter a num"))
#     print(x)
# except Exception:
#     print("Something went wrong")


# try:
#     x=int(input("Enter any number"))
#     print(100/x)
# except ValueError:
#     print("Value is wrong")
# except ZeroDivisionError:
#     print("cannot divide by 0")



# else in exception (else only run when there is no error in try)
# try:
#     x=int(input("enter a num"))
#     y=int(input("enter a num"))
#     print(x-y)

# except ValueError:
#     print("value is not appropoirate")
# else:
#     print("operation in done successfully")

# finally runs whether there is an error or not
# try:
#     x = int(input("Enter a number: "))
#     print(100 / x)

# except ValueError:
#     print("Invalid value")

# except ZeroDivisionError:
#     print("Cannot divide by 0")

# finally:
#     print("Program finished")


# Exercise Student storage system

# day 6 exercise

while True:
    try:
        print("1. Add Student")
        print("2. Display Student")
        print("3. Remove Student")
        print("4. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            x = input("Enter your name: ")
            y = int(input("Enter your age: "))
            z = float(input("Enter your marks: "))

            with open("Std.txt", "a") as f:
                f.write(f"Name:{x},Age:{y},Marks:{z}\n")

            print("Student Saved")

        elif ch == "2":
            with open("Std.txt", "r") as f:
                print(f.read())

        elif ch == "3":
            name = input("Enter the name of student you want to remove: ")

            with open("Std.txt", "r") as f:
                lines = f.readlines()

            with open("Std.txt", "w") as f:
                for i in lines:
                    if f"Name:{name}" not in i:
                        f.write(i)

            print("Student removed")

        elif ch == "4":
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Value is invalid")