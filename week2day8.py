# NUMPY BASICS(ARRAYS>INDXING>SLICING>BROADCASTING)
# Exercise is Matrix Multiplication

import numpy as np
mat1=np.array([
    [2,5,3],
    [5,6,7]
])
mat2=np.array([
    [32,55,35],
    [52,263,74]
])
mat3=np.array([
    [43,44],
    [65,77]
])
mat4=np.array([
    [132,55,135],
    [522,27,24]
])

print(mat1)
print(mat2)
print(mat3)
print(mat4)

print(mat1.shape)
print(mat2.shape)
print(mat3.shape)


res=np.matmul(mat1,mat2.T)
print(res)
print(mat1@mat2.T)
res1=np.matmul(mat1.T,mat3)
print(res1)
print(mat1.T@mat3)

det=np.linalg.det(mat3)
print(det)

inv=np.linalg.inv(mat3)
print(inv)

rank1=np.linalg.matrix_rank(mat1)
print(rank1)
rank2=np.linalg.matrix_rank(mat2)
print(rank2)

pow1=np.linalg.matrix_power(mat3.T,2)
print(pow1)
pow2=np.linalg.matrix_power(mat3,4)
print(pow2)


print(np.eye(3))

mat5=np.linalg.multi_dot([mat1,mat2.T,mat4])
print(mat5)

print(mat1[0,1])

print(mat2[1])
print(mat2[:,0])

x=np.array([2,3,55])
print(mat1+x)
