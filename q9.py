#Use the Metropolis algorithm to get a sample from a density that is uniform for 3 < x < 7 and zero elsewhere.
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x):
	y=(1/np.sqrt(2*np.pi))*np.exp(-0.5*x*x)
	return(y)

def random_gaussian():
	x1 = np.random.rand(1)
	x2 = np.random.rand(1)
	y1 = np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2) #Box-Muller to give one random number distributed according to a gaussian distribution.
	return(y1)

def uniform(x):
	if(x>3 and x<=7):  #Unifor distribution function -not normalised 
		return(1)
	else:
		return(0)
	
num = 50000
x1=np.linspace(3,7,100)
y1=np.ones(100)*0.25 #Normalised uniform distribution to compare
x=np.zeros(num)
x[0]=0
for i in range (1,num):
	xprime=x[i-1]+random_gaussian()
	r=np.random.rand()
	if(uniform(x[i-1])==0):
		x[i]=xprime           #Metropolis algorithm
	elif(uniform(xprime)/uniform(x[i-1])>r):
		x[i]=xprime
	else:
		x[i]=x[i-1]

num_bins = 50
fig1=plt.figure()
plt.hist(x[10000:num],num_bins, density=True,label="Histogram")  #Plotting histogram
plt.plot(x1,y1,'-r',label="uniform distribution")
plt.legend()
fig2=plt.figure()
plt.plot(x[0:2000],'.y')
plt.show()	
