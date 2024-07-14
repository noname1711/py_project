import numpy as np
from scipy.optimize import minimize


def objective(z):
    z = complex(z[0], z[1])
    expr = abs(abs(z / ((2 - 3j) * abs(z) + 1j + 1)) - 1j - 3)
    return -expr  

z0 = [1, 1]


result = minimize(objective, z0, method='BFGS')

max_value = -result.fun
print("Giá trị lớn nhất của biểu thức là:", max_value)

