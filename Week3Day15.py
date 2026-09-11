import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import KFold
n={
    "TV_Ads":[10,20,30,40,50,60,70,80,90,100],
    "Sales":[15,20,25,30,35,40,45,50,55,60]
}
p=pd.DataFrame(n)
print(p)
print(p.shape)
print(p.dtypes)

X=p["TV_Ads"]
y=p["Sales"]
print(X)
print(y)
X=X.values.reshape(10,1)
print(X)
print(X.shape)
print(y.shape)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(X_train)
print(X_test)
print(y_test)
print(y_train)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# regression part metrices

y_actual=[15,20,25,30,35]
y_predicted=[16,19,27,28,36]

mae=mean_absolute_error(y_actual,y_predicted)
print(mae)

mse=mean_squared_error(y_actual,y_predicted)
print(mse)

rmse=np.sqrt(mse)
print(rmse)

r2=r2_score(y_actual,y_predicted)
print(r2)

# classification metrices

ya=[1,1,1,0,0,0,1,0,1,1]
yp=[1,1,0,0,0,1,1,0,1,0]
print(ya)
print(yp)

acc=accuracy_score(ya,yp)
print(acc)

pre=precision_score(ya,yp)
print(pre)

recall=recall_score(ya,yp)
print(recall)

f1=f1_score(ya,yp)
print(f1)

con=confusion_matrix(ya,yp)
print(con)


# cross validation

kf=KFold(n_splits=5,shuffle=True,random_state=42)
print(kf)
