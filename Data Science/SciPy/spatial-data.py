import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull ;             '''For 2nd part i.e convex hull'''
from scipy.spatial import KDTree ;     '''3rd part i.e KD tree'''
import matplotlib.pyplot as plt

points = np.array([
    [2,4] ,
    [4,5] ,
    [3,0] ,
    [3,2] ,
    [4,1] 
])        

simplices = Delaunay(points).simplices

plt.triplot(points[:,0] , points[:,1] , simplices)
plt.scatter(points[:,0] , points[:,1] , color='r')    ; '''r means red'''

plt.show()




'''Convex Hull'''
points = np.array([
    [2,4] ,
    [4,5] ,
    [3,0] ,
    [3,2] ,
    [4,1] ,
    [1,2] ,          
    [5,0] ,
    [3,1] ,
    [1,2] ,
    [0,2] 
])        


hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0] , points[:,1])
for simplex in hull_points:
    plt.plot(points[simplex ,0] , points[simplex,1] , 'k-')

plt.show()


'''KD tree'''

pts = [(1,-1) , (2,3) , (-2,3) , (2,-3)]
kdtree = KDTree(pts)
res = kdtree.query((1,1))
print(res)