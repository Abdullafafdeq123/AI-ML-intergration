# Pandas Basics using Series & Data Frames
# Exercise is  Load Csv file and Filtering


# exercise 1 filtering using data frame because df is 2d dimensional

import pandas as pd

d={
    "Name":["Abdullah","Ali","Haseem","Waleed","Falak","Rameen"],
    "Age":[21,20,19,24,22,17],
    "Marks":[88,47,71,52,91,81],
    "Gender":["M","M","M","M","F","F"],
    "City":["Lahore","Islamabad","Karachi","Faislabad","Lahore","Karachi"]
    
    
}
p=pd.DataFrame(d)
print(p)

print(p[p["Marks"]>80])
print(p[p["Age"]>22])
print(p[p["City"]=="Lahore"])
print(p[p["Marks"].between(60,90)])
print(p[(p["City"]=="Lahore") & (p["Marks"]>80) ])
print(p[(p["City"]=="Lahore")|(p["City"]=="Karachi")])
print(p[(p["Gender"]=="F") & (p["Marks"]>75)])
p["Passed"]=p["Marks"]>=50
print(p[p["Passed"]])
print(p[(p["Age"]<22)&(p["Marks"]>75)&((p["City"]=="Lahore")|(p["City"]=="Karachi"))])
print(p[(p["Age"]<22)&(p["Marks"]>75)&(p["City"].isin(["Lahore","Karachi"]))])
print(p["Marks"].mean())
print(p[p["Marks"] > 70]["Marks"].sum())
print(p[p["City"]=="Lahore"]["Marks"].max())
print(p[p["City"]=="Karachi"]["Marks"].min())
print(p[p["Marks"]>75].count())
print(p[p["Gender"]=="F"]["Marks"].mean())
print(p[(p["Gender"]=="M")&(p["City"]=="Lahore")]["Marks"].sum())
print(p[p["Age"]<22]["Marks"].max())
print(p[p["City"].isin(["Lahore","Karachi"])])
print(p[(p["Age"]<22)&(p["Marks"]>75)&(p["City"].isin(["Lahore","Karachi"]))])
print(p[(p["Passed"])&(p["City"]=="Islamabad")])
print(p[(p["Gender"]=="F")&(p["Age"]<22)]["Marks"].max())
print(p[(p["City"]=="Lahore")&(p["Marks"].between(60,90))])





# Exercise 2 read csv 

import pandas as pd


x=pd.read_csv("s.csv")
print(x)
print(x[x["Marks"]>80])
print(x[x["Age"]<22])
print(x[x["City"]=="Lahore"])
print(x[x["Marks"].between(50,70)])
print(x[(x["City"]=="Lahore")&(x["Marks"]>80)])
print(x[x["City"].isin(["Lahore","Islamabad"])])
print(x[(x["Gender"]=="F")&(x["Marks"]>75)])
new_student = {
    "Name": "Ahmed",
    "Age": 21,
    "Marks": 85,
    "Gender": "M",
    "City": "Lahore"
}
x.loc[len(x)]=new_student
print(x)

x["Passed"]=x["Marks"]>=50
print(x[x["Passed"]])

print(x["Marks"].mean())

print(x[x["Marks"]>75]["Marks"].sum())
print(x[x["Marks"]>75]["Marks"].count())

print(x[(x["Age"]<22)&(x["Marks"]>75)&(x["City"].isin(["Lahore","Faislabad"]))])

print(x[(x["Passed"])&(x["City"]=="Karachi")])

print(x["Marks"].describe())

print(x.drop(x[x["Passed"]].index))
print(x.drop(x[x["Marks"]<50].index))

x.loc[x["Name"]=="Ahmed","Marks"]=90
print(x)

x.loc[x["Marks"]<50,"Marks"] +=5
print(x)

x.loc[x["City"]=="Faislabad","City"] = "Fbd"
print(x)
