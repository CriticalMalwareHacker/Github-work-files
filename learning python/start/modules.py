#built in modules
'''import math
print(math.sqrt(5))
print(math.factorial(5))
'''
#importing using from
'''from math import factorial
print(factorial(5))'''

#importing modules with a different name
''''import math as mt
print(mt.sqrt(36))

import random as rand
print(rand.randrange(10,20,2))'''

#userdefined modules, importing from another file
import testmodule
city=testmodule.city_name[1]
print(city)
cities=testmodule.city_name
print(cities)