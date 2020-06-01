#Use the Rejection Method in a Python code to produce random numbers
import numpy as np
import matplotlib.pyplot as plt

def gau(x):
	y=(np.sqrt(2/np.pi))*np.exp(-0.5*x*x)  #Gaussian fuction- need to obtain random nos distributed according to gaussian diatribution.
	return(y)

def dis(x):
	return(np.tan(x)) #transformation rule to generate numbers according to the distribution fuction below.

def f(x):
	return(1/(1+x**2))  #This is the overlapping distribution fuction.
	
num=5000

z=np.linspace(0,5,100)
g1=gau(z)

x = np.random.rand(num)*np.pi/2  # Multiplied by pi/2 so to cover the range between 0 to inf...as tan(pi/2) is inf.
x = dis(x)
y=np.random.rand(num)*f(x) #To obtain a random no between 0 to f(x)-ie the enveloping fn.
y_g=[]
x_g=[]
for i in range (num):
	if(y[i]<gau(x[i])):
		y_g.append(y[i])  #Algorithm for the selection method
		x_g.append(x[i])

y_g=np.asarray(y_g)
x_g=np.asarray(x_g)
num_bins=20
plt.hist(x_g,num_bins, facecolor='green', density=True, label="Historgram") #Plotting Histogram
plt.plot(z,g1,'-k',label="Gaussian distribution")
plt.xlabel('x')		
plt.ylabel('g(x)')
plt.legend()
plt.show()
