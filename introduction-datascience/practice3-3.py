import numpy as np
from sklearn.linear_model import LinearRegression

arr2d_data = np.loadtxt(fname = "polyreg.csv", delimiter = ",")
array_x = arr2d_data[:,0]
array_y = arr2d_data[:,1]
n = array_x.size
sigma = 1
list2d_maxX = []
for x in array_x:
    list2d_maxX += [[x, x**2, x**3, x**4, x**5]]
arr2d_maxX = np.array(list2d_maxX)
reg = LinearRegression()
for k in range(1,6):
    reg.fit(arr2d_maxX[:,:k],array_y)
    array_yhat = reg.predict(arr2d_maxX[:,:k])
    a = (n/2)*np.log(2*np.pi*(sigma**2))
    b = 1/(2*(sigma**2))*sum((array_y[:n]-array_yhat)**2)
    c = ((k+1)/2*np.log(n))
    print("{0:.2f}".format(a+b+c))