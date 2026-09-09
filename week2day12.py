# Matplotlib

# plot()

# x=[2,3,4,3]
# m1=[66,33,44,59]
# m2=[86,23,46,33]

# plt.plot(x,m1,label="Marks1",marker="s",color="black",linestyle=":")
# plt.plot(x,m2,label="Marks2",marker="o",color="grey",linestyle="--")

# plt.title("Hello there")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.grid()
# plt.legend()
# plt.show()

# bar
# import matplotlib.pyplot as plt

# x=["Hello","hi","hello"]
# y=[3,4,5,]

# # vertical bar
# # plt.bar(x,y)
# # horizontal bar
# plt.barh(x,y)
# plt.title("Bar")
# plt.xlabel("X")
# plt.ylabel("Y")

# plt.show()

# Scatter plot

# age1=[44,21,22]
# mark1=[33.3,66.5,66]

# age2=[66,55,44]
# mark2=[55,54,75]

# plt.scatter(age1,mark1,label="Std1",marker="s",color="red",s=200,alpha=0.7)
# plt.scatter(age2,mark2,label="Std2",marker="o",color="black",s=100,alpha=1)
# plt.grid()
# plt.title("Hello")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend()
# plt.show()



# Full exercise

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Ali", "Ahmed", "Usman", "Hassan", "Rameen", "Zain",
             "Hamza", "Ayesha", "Bilal", "Sara"],

    "Age": [18, 19, 20, 21, 22, 23, 20, 19, 22, 21],

    "Math": [55, 65, 72, 80, 88, 92, 70, 85, 78, 95],

    "Science": [60, 68, 75, 82, 85, 90, 73, 88, 80, 93],

    "City": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi",
             "Lahore", "Islamabad", "Lahore", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

# part1
print(df)
df.info()

print(df["Math"].mean())
print(df["Science"].max())
print(df[df["Math"]>80])
print(df[df["City"]=="Lahore"])
print(df["Math"].max())
print(df[df["Math"]==df["Math"].max()])

# part2
df["Average"]=df[["Math","Science"]].mean(axis=1)
print(df)
# part3

plt.plot(df["Name"],df["Average"],marker="o",label="Average")
plt.title("Student AVg Marks")
plt.xlabel("Students")
plt.ylabel("Avg marks")
plt.legend()
plt.grid()
plt.show()

# part4

x=np.arange(len(df))
w=0.33
plt.bar(x-w/2,df["Math"],width=w,label="Math")
plt.bar(x+w/2,df["Science"],width=w,label="Science")
plt.title("Math vs Science")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.xticks(x,df["Name"])
plt.show()

# part5
plt.scatter(df["Age"],df["Average"],marker="o",s=100,alpha=0.7,label="Age and Marks")
plt.title("Age and Marks ")
plt.xlabel("Age")
plt.ylabel(" Avg Marks")
plt.legend()
plt.grid()
plt.show()

# part6
l=df[df["City"]=="Lahore"]
k=df[df["City"]=="Karachi"]

plt.scatter(l["Age"],l["Average"],label="Lahore",marker="s")
plt.scatter(k["Age"],k["Average"],label="Karachi",marker="o")
plt.title("Avg")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
