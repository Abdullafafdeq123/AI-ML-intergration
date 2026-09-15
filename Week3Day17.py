import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score

df=pd.read_csv("Titanic.csv")
# print(df)tell me in bullet poinsts
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df["Survived"].unique())
print(df["Survived"].nunique())
print(df["Survived"].value_counts())

print(df["Survived"].dtypes)

print(df[["Pclass","Sex","Age","Fare"]])
print(df[["Pclass","Sex","Age","Fare"]].isnull().sum())
print(df["Age"].median())
df["Age"]=df["Age"].fillna(df["Age"].median())
print(df)

print(df["Age"].isnull().sum())
print(df["Sex"].unique())

df["Sex"]=df["Sex"].replace({"male":0,"female":1})
print(df["Sex"].unique())
print(df["Sex"].dtypes)

print(df["Sex"].value_counts())

df["Sex"]=df["Sex"].astype(int)
print(df["Sex"].dtypes)


X=df[["Pclass","Sex","Age","Fare"]]
y=df["Survived"]
print(X.head())
print(y.head())
print(X.shape)
print(y.shape)


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train)
print(X_test)
print(y_train)
print(y_test)
print(X_train.shape)
print(X_test.shape)


model=LogisticRegression()

model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(y_pred)
print(y_pred.shape)

acc=accuracy_score(y_test,y_pred)
print(acc)

con=confusion_matrix(y_test,y_pred)
print(con)

pre=precision_score(y_test,y_pred)
print(pre)

rec=recall_score(y_test,y_pred)
print(rec)

f1=f1_score(y_test,y_pred)
print(f1)

cross=cross_val_score(model,X,y,cv=5)
print(cross)

print(cross.mean())

prob=model.predict_proba(X_test)
print(prob)
print(prob[0:5])

print(prob[0])
print(y_pred[0])
print(prob[0][0])
print(prob[0][1])


print(y_test.iloc[0])
print(y_pred[0])
print(prob[0][1])

print(model.coef_)
print(model.intercept_)