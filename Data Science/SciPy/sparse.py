import numpy as np
from scipy.sparse import csr_matrix

dense_matrix = np.array([[1,0,0] , 
                        [0,0,2] , 
                        [3,0,4]] )

sparse_matrix = csr_matrix(dense_matrix)


print("Dense matrix : " )
print(dense_matrix)
print("\n Sparse matrix : ")
print(sparse_matrix)