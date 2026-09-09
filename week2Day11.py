import pandas as pd

x=pd.read_csv("students.csv")
y=pd.read_csv("marks.csv")
z=pd.read_csv("fees.csv")
print(x)
print(y)
print(z)
m1=pd.merge(x,y,on="STDID")
m2=pd.merge(m1,z,on="STDID")
print(m1)
print(m2)

print(m2.loc[m2.isna().any(axis=1)])

m2["Age"]=m2["Age"].fillna(m2["Age"].mean())
print(m2)
m2["Marks"]=m2["Marks"].fillna(m2["Marks"].mean())
print(m2)
m2["Fee"]=m2["Fee"].fillna(m2["Fee"].mean())
print(m2)

print(m2.sort_values("Marks",ascending=False))

m2=m2.dropna(subset=["City"])
print(m2)
m2=m2.reset_index(drop=True)
print(m2)

print(m2.groupby("City").agg(
    {
        "Marks":["mean","min","max"],
        "Name":["count"]
        
    }
))
print(m2[m2["Marks"]>80])

m2.to_csv("final_students.csv", index=False)
print(m2)
