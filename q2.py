#random nos using np.random.rand()
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10000) #using the library function

num_bins = 30
plt.hist(x,num_bins, range=(0.0, 1.0), density=True) #plotting histogram
plt.title('Histogram of random nos between 0 and 1')
plt.show()
