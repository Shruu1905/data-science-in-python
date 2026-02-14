from scipy.optimize import minimize_scalar
from scipy.optimize import differential_evolution        ; '''for global'''

def quadractic (x) :
    return (x - 3) ** 2 + 5

result = minimize_scalar(quadractic)
print(result)
print("Optimial Solution :" , result.x)
print("Minimum value :" , result.fun)



'''For Global'''

def global_objective (x) :
    return x[0] ** 2 + x[1] ** 2

result = differential_evolution(global_objective  , [(-2 , 2) ,  (-2,2) ] )
print(result)
print("Global Optimial Solution :" , result.x)
print("Global Minimum value :" , result.fun)