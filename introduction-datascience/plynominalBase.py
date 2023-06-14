import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# print(arr2d_x)

# beta0, beta1, beta2, beta3 = 3, -2, 0.5, 1
# array_beta = np.array([beta1, beta2, beta3])
# array_f = np.dot(arr2d_x, array_beta) + 0
# print(array_f)
# plt.scatter(array_x, array_f)
# plt.show()


#f(x) = ß0 + ß1X + ß2X**2 + ß3X**3 + E

array_y = [4.12434536, 0.38824359, 8.47182825, 1.92703138, 5.36540763]

array_x = ([1, -2, 2, 0, -1])

#二次の形にする
list2d_x = []
for x in array_x:
    list2d_x += [[x, x**2, x**3]]
arr2d_x = np.array(list2d_x)

#回帰分析を行う
reg =LinearRegression()
reg.fit(arr2d_x, array_y)
print(reg.coef_)
print(reg.intercept_) #ßの値

array_predx = np.arange(-2, 2.1, 0.1)
print(array_predx)
list2d_predX = []
for x in array_predx:
    list2d_predX += [[x, x**2, x**3]]
arr2d_predX = np.array(list2d_predX)
array_predy = reg.predict(arr2d_predX)
plt.scatter(array_x, array_y, c="red")
plt.plot(array_predx, array_predy, c="blue")
plt.show()