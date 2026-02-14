import numpy as np
from scipy import constants , special


result_addition = np.add(5,3)
result_exponent = np.exp(3)
result_bessel = special.jn(2,3)      


print("Addition result :" , result_addition)
print("Exponential Result : " , result_exponent)
print("Result of bessel function :" , result_bessel)



'''Constants'''
'''constant.constant name '''

speed_of_light = constants.speed_of_light
gravitational_constant = constants.gravitational_constant
boltzmann_constant = constants.Boltzmann
pi = constants.pi
golden_ratio = constants.golden_ratio

print(speed_of_light)
print(gravitational_constant)
print(boltzmann_constant)
print(pi)
print(golden_ratio)





'''Unit Conversion'''
inch_to_meter = constants.inch
cm_to_km = constants.centi

print(inch_to_meter)
print(cm_to_km)