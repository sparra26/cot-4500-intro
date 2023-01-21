#Sherly Parra Guzman
#COT4500-Sring2023


import numpy as np

matrix1 = np.eye(3)
print(matrix1)
print("\n")

matrix2 = np.eye(3) + 3*(1-np.eye(3))
print(matrix2)
print("\n")

matrix3 = np.delete(matrix2, 2, 1)
print(matrix3)
