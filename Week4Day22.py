from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
i=fetch_california_housing()
X=i.data
y=i.target
print(X.shape)
print(y.shape)

print(X[0:5])
print(i.feature_names)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


sc=StandardScaler()
X_train_s=sc.fit_transform(X_train)
print(X_train_s)
X_test_s=sc.transform(X_test)
print(X_test_s)


mlp=MLPRegressor(
    hidden_layer_sizes=(10,),
    activation="relu",
    max_iter=1000,
    random_state=42
)

mlp.fit(X_train_s,y_train)
yps=mlp.predict(X_test_s)
print(yps)


mae=mean_absolute_error(y_test,yps)
print(mae)

mse=mean_squared_error(y_test,yps)
print(mse)

r2=r2_score(y_test,yps)
print(r2)


print(mlp.coefs_)
print(mlp.intercepts_)

for i in mlp.coefs_:
    print(i.shape)
for x in mlp.intercepts_:
    print(x.shape)
    
print(mlp.loss_)
print(mlp.loss_curve_)

