import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra                      ; '''2nd part '''
from scipy.sparse import csr_matrix

arr = np.array([
    [1,0,0] ,
    [1,2,0] ,
    [2,0,0]
])

newarray = csr_matrix(arr)

print(newarray)



'''2nd part'''
array2 = dijkstra(newarray)
