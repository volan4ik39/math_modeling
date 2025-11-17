import numpy as np
def my_funk(arr):
    average = sum(arr) / len(arr)
    return average
n = np.array([1,2])
print(my_funk(n))

