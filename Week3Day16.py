import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import numpy as np


# one linear regression
# a={
#     "Area":[1000,1200,1500,1800,2000],
#     "Price":[200000,240000,300000,360000,400000]
# }
# n=pd.DataFrame(a)
# print(n)

# print(n.head())
# print(n.shape)
# print(n.columns)
# print(n.dtypes)

# X=n["Area"].values.reshape(-1,1)
# y=n["Price"]




# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

# model=LinearRegression()
# model.fit(X_train,y_train)
# y_pred=model.predict(X_test)


# print(model.coef_)
# print(model.intercept_)

# print(y_test)
# print(y_pred)


# mae=mean_absolute_error(y_test,y_pred)
# print(mae)

# mse=mean_squared_error(y_test,y_pred)
# print(mse)

# rmse=np.sqrt(mse)
# print(rmse)

# r2=r2_score(y_test ,y_pred)
# print(r2)


# newval=[[800]]
# pred=model.predict(newval)
# print(pred)


# multiple regression 

data = {
    "Area": [1000, 1200, 1500, 1800, 2000],
    "Bedrooms": [2, 2, 3, 3, 4],
    "Bathrooms": [1, 2, 2, 3, 3],
    "Price": [200000, 250000, 320000, 380000, 450000]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

X=df[["Area","Bedrooms","Bathrooms"]]
y=df["Price"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4)

model=LinearRegression()

model.fit(X_train,y_train)
trained=model.predict(X_test)

print(y_test)
print(trained)

mae2=mean_absolute_error(y_test,trained)
print(mae2)

mse2=mean_squared_error(y_test,trained)
print(mse2)

rmse2=np.sqrt(mse2)
print(rmse2)

r21=r2_score(y_test ,trained)
print(r21)

nh=[[1600,3,2]]
nh1=model.predict(nh)
print(nh1)