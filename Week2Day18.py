from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


i=load_iris()
X=i.data
y=i.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_test.shape)
print(X_train.shape)
print(y_test.shape)
print(y_train.shape)


model=DecisionTreeClassifier()


model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(y_pred)

acc=accuracy_score(y_test,y_pred)
print(acc)


model2=DecisionTreeClassifier(max_depth=2)
model2.fit(X_train,y_train)
y_pred1=model2.predict(X_test)
print(y_pred1)

acc1=accuracy_score(y_test,y_pred1)
print(acc1)


model3=DecisionTreeClassifier(max_depth=3)
model3.fit(X_train,y_train)
y_pred2=model3.predict(X_test)
print(y_pred2)

acc2=accuracy_score(y_test,y_pred2)
print(acc2)

print(acc)
print(acc1)
print(acc2)


model4=DecisionTreeClassifier(min_samples_leaf=2)
model4.fit(X_train,y_train)
y_pred3=model4.predict(X_test)
print(y_pred3)

acc3=accuracy_score(y_test,y_pred3)
print(acc3)

model5=DecisionTreeClassifier(criterion="gini")
model5.fit(X_train,y_train)
y_pred4=model5.predict(X_test)
print(y_pred4)

acc4=accuracy_score(y_test,y_pred4)
print(acc4)



model6=DecisionTreeClassifier(criterion="entropy")
model6.fit(X_train,y_train)
y_pred5=model6.predict(X_test)
print(y_pred5)

acc5=accuracy_score(y_test,y_pred5)
print(acc5)

print(model5.feature_importances_)

plot_tree(model5)
plt.show()

# Random Forest


rf_model=RandomForestClassifier()
rf_model.fit(X_train,y_train)
m1=rf_model.predict(X_test)
print(m1)

rfacc=accuracy_score(y_test,m1)
print(rfacc)


rf_model1=RandomForestClassifier(n_estimators=10)
rf_model1.fit(X_train,y_train)
m2=rf_model1.predict(X_test)
print(m2)

rfacc1=accuracy_score(y_test,m2)
print(rfacc1)


rf_model2=RandomForestClassifier(n_estimators=50)
rf_model2.fit(X_train,y_train)
m3=rf_model2.predict(X_test)
print(m3)

rfacc2=accuracy_score(y_test,m3)
print(rfacc2)


rf_model2=RandomForestClassifier(n_estimators=50)
rf_model2.fit(X_train,y_train)
m3=rf_model2.predict(X_test)
print(m3)


rf_model3=RandomForestClassifier(max_depth=2)
rf_model3.fit(X_train,y_train)
m4=rf_model3.predict(X_test)
print(m4)

rfacc3=accuracy_score(y_test,m4)
print(rfacc3)


rf_model4=RandomForestClassifier(n_estimators=50,max_depth=3)
rf_model4.fit(X_train,y_train)
m5=rf_model4.predict(X_test)
print(m5)


rfacc4=accuracy_score(y_test,m5)
print(rfacc4)

print(rf_model.feature_importances_)


oob=RandomForestClassifier(n_estimators=50,oob_score=True,random_state=42)
oob.fit(X_train,y_train)
print(oob.oob_score_)