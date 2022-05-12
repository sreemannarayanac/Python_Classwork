import matplotlib.pyplot as mp, numpy as np
x = np.linspace(2,12,num=10)
print(x)
y = x ** 2
mp.plot(x,y)
mp.show()