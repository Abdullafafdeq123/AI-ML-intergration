# spam detection

import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
texts = [
    "Congratulations you won a free prize",
    "Claim your free money now",
    "You have won a $1000 gift card",
    "Click this link to claim your reward",
    "Win cash instantly by clicking here",
    "Urgent you have been selected for a prize",
    "Hey are we meeting today",
    "Can you send me the assignment",
    "I will call you tonight",
    "Are you coming to university tomorrow",
    "Please bring my book with you",
    "What time should we meet"
]

labels = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

m1=[]

for i in texts:
    tok=word_tokenize(i)
    m1.append(tok)

print(m1)

model=CountVectorizer()
cv=model.fit_transform(texts)
print(cv)
print(model.get_feature_names_out())
print(cv.toarray())


model2=TfidfVectorizer()
tfidf=model2.fit_transform(texts)
print(tfidf.toarray())
print(model2.get_feature_names_out())

lr=LogisticRegression()
lr.fit(tfidf,labels)

newvar=["You won the new Iphone"]
tr=model2.transform(newvar)

lrpred=lr.predict(tr)
print(lrpred)


# check spam of only at 0 index
if lrpred[0]==1:
    print("Spam")
else:
    print("Not Spam")
    

# check all the messages
spam=lr.predict(tfidf)
print(spam)
for c in spam:
    if c==1:
        print("Spam")
    else:
        print("Not spam")
        
acc=accuracy_score(labels,spam)
print(acc)

X_train,X_test,y_train,y_test=train_test_split(texts,labels,random_state=42,test_size=0.2)

model3=TfidfVectorizer()
tfidf_train=model3.fit_transform(X_train)
tfidf_test=model3.transform(X_test)


lr1=LogisticRegression()
lr1.fit(tfidf_train,y_train)

y_pred=lr1.predict(tfidf_test)
print(y_pred)


acc_test=accuracy_score(y_test,y_pred)
print(acc_test)


print(X_test)
print(y_test)
print(y_pred)