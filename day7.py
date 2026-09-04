#Advanced pyhton using iterators,generators,decorators
# #   iterators python

# num=[10,20,30]
# it=iter(num)
# print(next(it))
# print(next(it))
# print(next(it))

# str="Pyhton"  if you use for loopp you dont need next
# it=iter(str)
# for i in it:
#     print(i)
# try:
#     str="Pyhton"
#     it=iter(str)
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     print("Iteration completed")
    
# try:    
#     num=[3,2,4]
#     it=iter(num)
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     print("Iteration completed")
    

        
# n=[3,4,5]
# it=iter(n)
# print(type(it))

# class Count:
#     def __init__(self):
#         self.a = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.a <= 5:
#             value = self.a
#             self.a += 1
#             return value
#         else:
#             raise StopIteration


# c = Count()

# for x in c:
#     print(x)
# try:
#     class evennum:
#      def __init__(self):
#       self.a=2
#     def __iter__(self):
#       return self
#     def __next__(self):
#      if self.a<=20:
#         val=self.a
#         self.a+=2
#         return val
# except StopIteration:
#     print("iteration is stop")
# class c:
#     def __init__(self):
#         self.a=5
#     def __iter__(self):
#         return self
#     def __next__(self):
#       if self.a>=1:
#           val=self.a
#           self.a-=1
#           return val
#       else:
#           raise StopIteration
    
        
        
# class mul:
#     def __init__(self):
#         self.a=3
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.a<=20:
#             val=self.a
#             self.a+=3
#             return val
#         else:
#             raise StopIteration

# 
        
# class sq:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=5:
#             val=self.num **2
#             self.num+=1
#             return val   
#         else:
#             raise StopIteration


# decorators
# class sq:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=5:
#             val=self.num **2
#             self.num+=1
#             return val   
#         else:
#             raise StopIteration

# def showi(func):

#     def wrapper():
#         print("before")
#         func()
#         print("after")

#     return wrapper


# @showi
# def hello():
#     print("hello")


# hello()

# def welcom(func):
#     def w():
#         print("Welcome")
#         func()
#         print("Have a nice day")
        
#     return w
# @welcom
# def hello():
#     print("hello abd")
# hello()

        
# def ev(func):
#     def a():
#         val=func()
#         if val%2==0:
#             print("even")
#         else:
#             print("odd")
    
#     return a
        

# @ev
# def num():
#     return 5
# num()


# def show(func):
#     def w(a,b):
#         res=func(a,b)
#         print(res)
#     return w
        
    

# @show
# def add(a,b):
#     return a+b
# add(5,3)

# def lg(func):
#     def a():
#         logged_in=True
#         if logged_in:
#             func()
#         else:
#             print("Please login first")
        
#     return a
# @lg
# def dash():
#     print("Welcome to dahsboard")
# dash()




# generators

# def even():
#     yield 2
#     yield 4
#     yield 6
#     yield 8
#     yield 10


# for x in even():
#     print(x)

# def num():
#     yield 10
#     yield 20
#     yield 30
#     yield 40
#     yield 50
# for i in num():
#     print(i)


# def sq():
#     for i in range(1,6):
#         yield i**2
# for x in sq():
#     print(x)

# def mul():
#     for i in range(1,11):
#         yield i*5
# for x in mul():
#     print(x)
# import time


# log time exercise

# import time

# def logtime(func):
#     def w():
#         start=time.time()
#         func()
#         end=time.time()
#         execution=end-start
#         print("the execution time is",execution)
#     return w
# @logtime
# def hel():
#     print("hello")
#     time.sleep(5)
# hel( )

# execution time with decorators and generators
# import time
# def log(func):
#     def w():
#         s=time.time()
#         func()
#         e=time.time()
#         execution=e-s
#         print(execution)
#     return w
# @log   
# def num():
#     for i in range(1,11):
#         yield i






import time

def logtime(func):
    def wrapper():
        print("Started")

        start = time.time()

        for i in func():
            print(i)

        end = time.time()

        print("Finished")

        execution = end - start
        print("Execution time:", execution)

    return wrapper


@logtime
def num():
    for i in range(1, 11):
        yield i


num()