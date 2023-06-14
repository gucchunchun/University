import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(1)
n = 100 #sample size
beta0, beta1, beta2, beta3 = 3, -2, 0.5, 1
array_beta = np.array([beta1, beta2, beta3])

array_x = np.random.uniform(-2, 2, n)
list2d_x = []
for x in array_x:
    list2d_x += [[x, x**2, x**3]]
arr2d_x = np.array(list2d_x)
print(list2d_x)

array_f = np.dot(arr2d_x, array_beta) + beta0
# print(array_f )
array_y = array_f + np.random.normal(0, 1, n)
plt.scatter(array_x, array_y, c="red")
# plt.show()

reg = LinearRegression()
reg.fit(arr2d_x, array_y)
# print(reg.coef_)
# print(reg.intercept_)

array_predX = np.arange(-2, 2.1, 0.1)
list2d_predX = []
for x in array_predX:
    list2d_predX += [[x, x**2, x**3]]
arr2d_predX = np.array(list2d_predX)
array_predy = reg.predict(arr2d_predX)
plt.scatter(array_x, array_y, c="red")
plt.plot(array_predX, array_predy, c="blue")
plt.show()