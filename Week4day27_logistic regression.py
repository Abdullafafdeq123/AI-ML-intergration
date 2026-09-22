import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)
from sklearn.feature_extraction.text import TfidfVectorizer
p=pd.read_csv("IMDB Dataset.csv")
print(p.head())
print(p.shape)
print(p.columns)
print(p.isna().sum())
print(p["sentiment"].value_counts())


X=p["review"]
y=p["sentiment"]


p["sentiment"]=p["sentiment"].replace({"positive":1,"negative":0})

y=p["sentiment"].astype(int)
print(y.value_counts())


X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

model_cv=CountVectorizer()
cv_train=model_cv.fit_transform(X_train)
cv_test=model_cv.transform(X_test)

print(cv_train.shape)
print(cv_test.shape)

model_lr=LogisticRegression()
model_lr.fit(cv_train,y_train)
y_pred=model_lr.predict(cv_test)
print(y_pred)

acc1=accuracy_score(y_test,y_pred)
print(acc1)

cr1=classification_report(y_test,y_pred)
print(cr1)

cm1=confusion_matrix(y_test,y_pred)
print(cm1)


new_reviews = [
    "This movie was absolutely amazing and I loved it",
    "The movie was terrible and completely boring",
    "I really enjoyed the acting and the story",
    "I hated this movie, it was a waste of time",
    "Excellent movie, I would definitely watch it again"
]

newrevie_pred=model_cv.transform(new_reviews)

newlr=model_lr.predict(newrevie_pred)

print(newrevie_pred)
print(newlr)

# positive negative with names
for i in range(len(new_reviews)):
    print(new_reviews[i])
    if newlr[i]==1:
        print("Positive")
    else:
        print("Negative")
        

model_tfidf=TfidfVectorizer()
train_tfidf=model_tfidf.fit_transform(X_train)
test_tfidf=model_tfidf.transform(X_test)

print(train_tfidf.shape)
print(test_tfidf.shape)


model_lr1=LogisticRegression()
model_lr1.fit(train_tfidf,y_train)
y_pred1=model_lr1.predict(test_tfidf)
print(y_pred1)


acc2=accuracy_score(y_test,y_pred1)
print(acc2)

cr2=classification_report(y_test,y_pred1)
print(cr2)

cm2=confusion_matrix(y_test,y_pred1)
print(cm2)

print(acc1)
print(acc2)
print(cr1)
print(cr2)
print(cm1)
print(cm2)