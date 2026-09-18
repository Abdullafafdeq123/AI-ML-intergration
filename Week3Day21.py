import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier


p=pd.read_csv("heart.csv")
print(p)

print(p.head())
print(p.tail())
print(p.shape)
print(p.columns)
print(p.dtypes)

print(p.isna().sum())
print(p.duplicated().sum())
print(p["target"].value_counts())
print(p.describe())

# remove duplicates
p=p.drop_duplicates()
print(p.shape)
print(p.duplicated().sum())
print(p["target"].value_counts())


X=p[["age","sex","cp","chol","trestbps","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]]
y=p["target"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


sc=StandardScaler()
X_train_s=sc.fit_transform(X_train)
print(X_train_s)
print(X_train_s.shape)

X_test_s=sc.transform(X_test)
print(X_test_s)
print(X_test_s.shape)


model=LogisticRegression()
model.fit(X_train_s,y_train)
y_pred=model.predict(X_test_s)
print(y_pred)
print(y_pred.shape)


acc=accuracy_score(y_test,y_pred)
print(acc)

pre=precision_score(y_test,y_pred)
print(pre)

rec=recall_score(y_test,y_pred)
print(rec)

f1=f1_score(y_test,y_pred)
print(f1)

con=confusion_matrix(y_test,y_pred)
print(con)

cr=classification_report(y_test,y_pred)
print(cr)

cv=cross_val_score(model,X_train_s,y_train,cv=5)
print(cv)
print(cv.mean())

y_prob=model.predict_proba(X_test_s)
print(y_prob)
print(y_prob.shape)


y_prob1=y_prob[:,1]
print(y_prob1)
print(y_prob1.shape)


rc=roc_curve(y_test,y_prob1)
fpr,tpr,thresholds=rc
print(fpr)
print(tpr)
print(thresholds)
print(rc)

rac=roc_auc_score(y_test,y_prob1)
print(rac)


plt.plot(fpr,tpr,label="ROC Curve")

plt.title("ROC Curve")
plt.xlabel("False positive rate")
plt.ylabel("True Positive Rate")
plt.plot([0,1],[0,1],linestyle="--",label="Random")
plt.legend()
plt.grid()
plt.show()


model1=RandomForestClassifier(n_estimators=100,max_depth=3,random_state=42)

model1.fit(X_train,y_train)
y_pred1=model1.predict(X_test)
print(y_pred1)

acc1=accuracy_score(y_test,y_pred1)
print(acc1)

pre1=precision_score(y_test,y_pred1)
print(pre1)

rec1=recall_score(y_test,y_pred1)
print(rec1)

f11=f1_score(y_test,y_pred1)
print(f11)

con1=confusion_matrix(y_test,y_pred1)
print(con1)

cr1=classification_report(y_test,y_pred1)
print(cr1)

y_prob2=model1.predict_proba(X_test)
print(y_prob2)


y_prob3=y_prob2[:,1]
print(y_prob3)


rc1=roc_curve(y_test,y_prob3)
fpr1,tpr1,thresholds1=rc1
print(fpr1)
print(tpr1)
print(thresholds1)

rac1=roc_auc_score(y_test,y_prob3)
print(rac1)

plt.plot(fpr1,tpr1,label="Random Forest")
plt.plot([0,1],[0,1],linestyle=":",label="random baseline")
plt.title("Random Forest")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.grid()
plt.show()



res=pd.DataFrame(
    {
        "Metrics":["Accuracy","Precision","Recall","F1","Auc"],
        "Logistic Regression":[acc,pre,rec,f1,rac],
        "Random Forest":[acc1,pre1,rec1,f11,rac1]
        
        
    }
)
print(res)
