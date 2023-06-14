import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#y = 3 -2x + 0.5x**2 + 3x**3 + e

#save random number
np.random.seed(0)

max_n = 1000
sigma = 1
beta0, beta1, beta2, beta3 = 3, -2, 0.5, 1
array_beta = np.array([beta1, beta2, beta3])
#rando.uniform(low, high, size)
array_x = np.random.uniform(-1.8, 1.5 , max_n)
list2d_x = []
for x in array_x:
    #polynomial = 3
    list2d_x += [[x, x**2, x**3]]
arr2d_X = np.array(list2d_x)
array_f = np.dot(arr2d_X, array_beta) + beta0
#np.normal(loc, scale, size)
#loc = mean of distribution
#scale = SD
array_y = array_f + np.random.normal(0, sigma, max_n)
plt.scatter(array_x, array_y, color="red")
plt.show()

#calculation of likelihood






#polynomial = 5
list2d_x += [[x, x**2, x**3, x**4, x**5]]