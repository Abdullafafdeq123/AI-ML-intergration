import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

i=load_iris()
print(i.data)
print(i.feature_names)
print(i.target)
print(i.target_names)

X=i.data
print(X.shape)

model=KMeans(n_clusters=3,random_state=42)

# model.fit(X)
# labels=model.labels_

# get cluster label for each point and train 
labels=model.fit_predict(X)
print(labels)

# Centroid
center=model.cluster_centers_
print(center)

inertia=model.inertia_
print(inertia)


plt.scatter(X[:,0],X[:,1],c=labels)
plt.scatter(center[:,0],center[:,1],marker="s",s=200)
plt.title("K means Clustering")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()

pred=model.predict([[3,4,5,6]])
print(pred)


m=[]
for i in range(1,11):
    km=KMeans(n_clusters=i,random_state=42)
    km.fit(X)
    m.append(km.inertia_)
print(m)

k=range(1,11)
plt.plot(k,m)
plt.title("Elbow Method")
plt.xlabel("No of Clusters")
plt.ylabel("Inertia")


plt.show()