import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.feature_selection import SelectKBest,f_classif

p=pd.read_csv("Titanic.csv")
print(p)

print(p.head())
print(p.columns)
print(p.shape)
print(p.dtypes)
print(p.isna().sum())


X=p[["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
print(X.head())
print(X.dtypes)
y=p["Survived"]
print(y.head())


X["Age"]=X["Age"].fillna(X["Age"].median())
X["Embarked"]=X["Embarked"].fillna(X["Embarked"].mode()[0])

print(X.isna().sum())


ohe=OneHotEncoder()
e1=ohe.fit_transform(X[["Sex","Embarked"]])
print(e1)
print(e1.shape)
print(ohe.categories_)


e1_arr=e1.toarray()
print(e1_arr)

e1_df=pd.DataFrame(
    e1_arr,
    columns=ohe.get_feature_names_out(["Sex","Embarked"])
    
)
print(e1_df.head())

X.drop(["Sex","Embarked"],axis=1,inplace=True)

X=pd.concat([X,e1_df],axis=1)
print(X.head())
print(X.dtypes)
print(X.columns)
print(X.shape)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

sc=StandardScaler()
X_train_Scaled=sc.fit_transform(X_train)
print(X_train_Scaled)
X_test_Scaled=sc.transform(X_test)
print(X_test_Scaled)

X_train_Scaled_or=X_train_Scaled.copy()
X_test_Scaled_or=X_test_Scaled.copy()





model=LogisticRegression()
rfe=RFE(
    estimator=model,
    n_features_to_select=5
)
X_train_Scaled=rfe.fit_transform(X_train_Scaled,y_train)
# show which feature was selected or which not
print(rfe.support_)
# select feature higher num lower priority
print(rfe.ranking_)



fn=X.columns
selected=fn[rfe.support_]
# check which one is selected or not
print(selected)
print(rfe.support_)
print(rfe.ranking_)

X_test_selected=rfe.transform(X_test_Scaled)
print(X_test_selected.shape)



model.fit(X_train_Scaled,y_train)
y_pred=model.predict(X_test_selected)
print(y_pred)


acc=accuracy_score(y_test,y_pred)
print(acc)

cm=confusion_matrix(y_test,y_pred)
print(cm)

pre=precision_score(y_test,y_pred)
print(pre)

re=recall_score(y_test,y_pred)
print(re)

f1=f1_score(y_test,y_pred)
print(f1)

cr=classification_report(y_test,y_pred)
print(cr)


k=SelectKBest(score_func=f_classif,k=2)
sk=k.fit_transform(X_train_Scaled_or,y_train)
print(sk)

# score every feature
print(k.scores_)
# get support showing which 5 features were selected
print(k.get_support())



fn=X.columns
sele=fn[k.get_support()]
print(sele)

sk_test=k.transform(X_test_Scaled_or)
print(sk_test)
print(sk_test.shape)

model1=LogisticRegression()
model1.fit(sk,y_train)

y_pred1=model1.predict(sk_test)
print(y_pred1)



acc1=accuracy_score(y_test,y_pred1)
print(acc1)

cm1=confusion_matrix(y_test,y_pred1)
print(cm1)

pre1=precision_score(y_test,y_pred1)
print(pre1)

re1=recall_score(y_test,y_pred1)
print(re1)

f11=f1_score(y_test,y_pred1)
print(f11)

cr1=classification_report(y_test,y_pred1)
print(cr1)


df={
    "Metric":["Accuracy","Precision","Recall","F1"],
    "RFE":[acc,pre,re,f1],
    "SelectKBest":[acc1,pre1,re1,f11]
}

df=pd.DataFrame(df)
print(df)