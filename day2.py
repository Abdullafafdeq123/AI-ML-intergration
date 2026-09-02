# Data structures python (list,tuples,sets,dictionaries)


# Student Record System

stdrec=[
    {
        "name":"Abdullah Jawaid",
         "age":21,
        "semester":7,
        "Cgpa":3.4,
        "Hobbies":("cricket","football","reading")
    },
    {
        "name":"Talha Ahmed",
        "age":22,
        "semester":7,
        "Cgpa":3.1,
        "Hobbies":("cricket","football")
    },
    {
        "name":"Ali Raza",
        "age":20,
        "semester":7,
        "Cgpa":3.8,
        "Hobbies":("cricket",)

    },
    {
        "name":"Ahsan Ali",
        "age":21,
        "semester":7,
        "Cgpa":3.5
    },
    {
        "name":"Maryam Tayyab",
        "age":22,
        "semester":7,
        "Cgpa":3.2,
        "Hobbies":("reading","Swimming")
    }
]
print(stdrec)
print(type(stdrec))
print(len(stdrec))

# value change in dictionary

stdrec[0]["name"]="Abdullah Jawaid Siddiqui"
stdrec[0]["Cgpa"]=3.44

print(stdrec[0])
print(stdrec)

# Add another std record
x={}
name=str(input("Enter your name:"))
x.update({"name":name})
age=int(input("Enter your age:"))
x.update({"age":age})
semester=int(input("Enter your semester:"))
x.update({"semester":semester})
cgpa=float(input("Enter your cgpa:"))
x.update({"cgpa":cgpa})
print(x)


stdrec.append(x)
print(stdrec)

# Acessing the data in the dictionary
print(stdrec[2]["Hobbies"])
# Accessing the  indiviual item in the dictionary
print(stdrec[2]["Hobbies"][0])

# removing the 2nd std record
stdrec.remove(stdrec[1])
print(stdrec)

# Add new department 
stdrec[0]["department"]="Computer Science"
stdrec[1]["department"]="AI"
print(stdrec)
# remove the department
stdrec[0].pop("department")
print(stdrec)
# check whether the department is still on the records or not

if "department" in stdrec[0]:
    print("yes")
else:
    print("no")
