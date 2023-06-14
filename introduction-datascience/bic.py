import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


max_n = 1000
sigma = 1 #SD　surface = variation
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

list2d_maxX = []
for x in array_x:
    list2d_maxX += [[x, x**2, x**3, x**4, x**5]]
arr2d_maxX = np.array(list2d_maxX)


reg = LinearRegression()
list_n = range(10, 151, 5)
for k in range(1,6):
    list_BICk = []
    for n in list_n:
        #polkynomial num = k、sample size = n　の時の回帰係数Bを求める
        reg. fit(arr2d_maxX[:n, :k],array_y[:n])
        array_yhat = reg.predict(arr2d_maxX[:n, :k])
        a = (n/2)*np.log(2*np.pi*(sigma**2))
        b = 1/(2*(sigma**2))*sum((array_y[:n]-array_yhat)**2)
        c = ((k+1)/2*np.log(n))
        list_BICk += [a + b + c]
    plt.plot(list_n, list_BICk, label="k={0}".format(k))
plt.legend(loc="upper left")
plt.show()
        
