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
