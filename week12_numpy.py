#week 12 numpy example
import numpy as np

matrix1 = np.ones((4,4))
print(matrix1)
matrix1 = matrix1 + matrix1
matrix1 = matrix1 * 5
print(matrix1)
matrix2 = np.diag((1,2,3,4))
print(matrix2)
print(matrix1*matrix2)