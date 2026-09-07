# numpy advances using stack,reshape and aggregate 
# exercise is implement the linear algebra operations



import numpy as np

arr1=np.array([
    [80,55,83],
    [85,75,73]
    
])
arr2=np.array([
    [63,75,93],
    [97,65,83]
    
])
comb=np.vstack((arr1,arr2))
print(comb)

res=comb.reshape(2,2,3)

print(np.sum(comb))
print(np.sum(comb,axis=1))
print(np.mean(comb))
print(np.max(comb))
print(np.min(comb))

new=np.array([
    [0,3],
    [0,3],
    [0,4]
    
])
print(np.matmul(comb,new))
print(comb@new)
print(comb.T)

print(np.linalg.matrix_rank(comb))



sc=np.array([20,30,40,50])
print(np.cumsum(sc))
print(np.cumprod(sc))
