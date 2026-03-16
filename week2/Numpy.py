import numpy as np
a = np.arange(15).reshape(3, 5)
# print(a)  # to print an array ->  [[ 0  1  2  3  4]
#                                    [ 5  6  7  8  9]
#                                    [10 11 12 13 14]]

print(a.shape) # gives the tuple of (columns,rows) -> (3,5)
print(a.ndim) # gives the dimension of the array , it is a 2D array -> 2 
print(a.dtype) # type of the array it has been store -> int64