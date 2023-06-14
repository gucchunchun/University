import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

arr2d_data = np.loadtxt(fname = "polyreg.csv", delimiter =",")
# print(arr2d_data) = [[x,y][x,y][x,y][x,y]...[x,y]]
array_x = arr2d_data[:, 0] #value of index 0 of all values in the array
# print(array_x)
array_y = arr2d_data[:, 1]

list2d_x = []
for x in array_x:
    list2d_x += [[x, x**2, x**3]]
arr2d_X = np.array(list2d_x)

reg = LinearRegression()
reg.fit(arr2d_X, array_y)

#小数点第二位まで
print("{0:.2f}".format(reg.coef_[0]))
print("{0:.2f}".format(reg.coef_[1]))
print("{0:.2f}".format(reg.coef_[2]))
print("{0:.2f}".format(reg.intercept_))
