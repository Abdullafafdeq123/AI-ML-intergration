import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

d=pd.read_csv("Titanic.csv")
print(d)

print(d.head())
print(d.tail())
print(d.info())

# 891,12
print(d.shape)

print(d.columns)



sns.histplot(data=d,x="Age")
plt.show()
sns.histplot(data=d,x="Age",bins=10)
plt.show()
sns.histplot(data=d,x="Age",kde=True)
plt.show()
sns.histplot(data=d,x="Age",hue="Sex")
plt.show()

sns.countplot(data=d,x="Sex")
plt.show()
sns.countplot(data=d,x="Survived")
plt.show()
sns.countplot(data=d,x="Pclass")
plt.show()

sns.countplot(data=d,x="Sex",hue="Survived")
plt.show()
sns.countplot(data=d,x="Pclass",hue="Survived")
plt.show()
sns.countplot(data=d,x="Sex",hue="Pclass")
plt.show()


sns.scatterplot(data=d,x="Age",y="Fare")
plt.show()
sns.scatterplot(data=d,x="Age",y="Fare",hue="Sex")
plt.show()

sns.histplot(data=d,x="Age",hue="Survived")
plt.show()
sns.histplot(data=d,x="Fare",hue="Survived")
plt.show()

sns.boxplot(data=d,x="Sex",y="Age")
plt.show()
sns.boxplot(data=d,x="Pclass",y="Fare")
plt.show()


c=d.corr(numeric_only=True)
print(c)

sns.heatmap(c,annot=True)
plt.show()

sns.pairplot(d,hue="Survived")
plt.show()

sr=d["Survived"].mean()
print(sr)


sr_gender=d.groupby("Sex")["Survived"].mean()*100
print(sr_gender)
print(d.isna().sum())