import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)
from sklearn.feature_extraction.text import TfidfVectorizer
p=pd.read_csv("IMDB Dataset.csv")
print(p.head())
print(p.shape)
print(p.info())
print(p.columns)
print(p.isna().sum())
print(p["sentiment"].value_counts())

X=p["review"]
y=p["sentiment"]

p["sentiment"]=p["sentiment"].map({"positive":1,"negative":0})

y=p["sentiment"].astype(int)

print(y.value_counts())


X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

cv1=CountVectorizer()
cv_train=cv1.fit_transform(X_train)
cv_test=cv1.transform(X_test)
print(cv_train)
print(cv_test)


mnb1=MultinomialNB()
mnb1.fit(cv_train,y_train)

y_pred1=mnb1.predict(cv_test)
print(y_pred1)



acc1=accuracy_score(y_test,y_pred1)
print(acc1)

cr1=classification_report(y_test,y_pred1)
print(cr1)

cm1=confusion_matrix(y_test,y_pred1)
print(cm1)



new_reviews = [
    "This movie was absolutely amazing and I loved it",
    "The movie was terrible and completely boring",
    "I really enjoyed the acting and the story",
    "I hated this movie, it was a waste of time",
    "Excellent movie, I would definitely watch it again"
]


cv2=cv1.transform(new_reviews)
mnb2=mnb1.predict(cv2)
print(cv2)
print(mnb2)

for i in range(len(new_reviews)):
    print(new_reviews[i])
    if mnb2[i]==1:
        print("positive")
    else:
        print("negative")
        
        
pred_proba=mnb1.predict_proba(cv2)
print(pred_proba)

for x in range(len(new_reviews)):
    print(new_reviews[x])
    # negative
    print(pred_proba[x][0])
    # positive
    print(pred_proba[x][1])
    
    
cv3=CountVectorizer(
    max_features=20000,
    stop_words="english",
    max_df=0.90,
    min_df=2
)

cv_train1=cv3.fit_transform(X_train)
cv_test1=cv3.transform(X_test)
print(cv_train1.shape)
print(cv_test1.shape)

mnb1.fit(cv_train1,y_train)
y_pred2=mnb1.predict(cv_test1)

acc2=accuracy_score(y_test,y_pred2)
print(acc2)

con2=confusion_matrix(y_test,y_pred2)
print(con2)

cr2=classification_report(y_test,y_pred2)
print(cr2)


tf=TfidfVectorizer()
tf_train=tf.fit_transform(X_train)
tf_test=tf.transform(X_test)
print(tf_train.shape)
print(tf_test.shape)

mnb3=MultinomialNB()
mnb3.fit(tf_train,y_train)
mnbpred=mnb3.predict(tf_test)

acc3=accuracy_score(y_test,mnbpred)
print(acc3)

con3=confusion_matrix(y_test,mnbpred)
print(con3)

cr3=classification_report(y_test,mnbpred)
print(cr3)
