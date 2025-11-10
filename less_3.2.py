import const
import numpy
h = 100
α = 45
β = 35
from numpy import*
from const import *
v = ((g*h)* (math.tan(β)**2))/(2* (math.cos(α)**2)*(1-math.tan(β)*math.tan(α)))**0.5
print(v)