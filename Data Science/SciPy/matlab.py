import scipy.io
import numpy as np

python_array = np.array([[2,3] , [4,5]])
scipy.io.savemat('python_data.mat' , {'myMatArray' : python_array} )

mat_data = scipy.io.loadmat('matlab_data.mat')

