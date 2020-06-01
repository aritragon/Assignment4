#Using the Box-Muller method in a Python code to produce 10,000 random numbers.
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x):
	y=(1/np.sqrt(2*np.pi))*np.exp(-0.5*x*x) #Defining the gausssian function
	return(y)

num=10000

x1 = np.random.rand(num)
x2 = np.random.rand(num)      #Box-Muller transformations
y1 = np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

ymin=min(y1)
ymax=max(y1)
dy=(ymax-ymin)/(num-1)

y=np.zeros(num)
gau=np.zeros(num)

for i in range (num):
	y[i] = ymin+i*dy
	gau[i] = gaussian(y[i])

num_bins=20
plt.hist(y1,num_bins, density=True, label="historgram of random numbers") #Histogram
plt.plot(y,gau,'-r',label="gaussian distribution")
plt.xlabel('x')			
plt.ylabel('g(x)')
plt.legend()
plt.title('Histogram of random nos between 0 and 1')
plt.show()
