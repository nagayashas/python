import numpy as np
import array
a=np.ndarray((3,3),dtype=np.int64)
a[:]=[[1,2,3],[4,5,6],[7,8,9]]
# print(a)
# print(a.shape)
# print(a.diagonal())
# print(np.fliplr(a).diagonal())
n = int(a.shape[0])
print(a,"<---------------------before swapping")
for i in range(n) :
    a[i][i],a[i][n-i-1] = a[i][n-i-1],a[i][i]
print(a)