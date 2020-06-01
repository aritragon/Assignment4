import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner
################################################
file1=open("fit.dat","r")
lines1=file1.readlines()
file1.close()
x=[]
y=[]
sigma_y=[]
for line in lines1[0:]:	
	delimiter = "&"		#To obtain data abt the x, y and corresponding errorbars
	p=line.split(delimiter)
	x.append(float(p[1]))
	y.append(float(p[2]))
	sigma_y.append(float(p[3]))
x=np.transpose(np.asarray(x))
y=np.transpose(np.asarray(y))
sigma_y=np.asarray(sigma_y)
################################################
def poly_fit(s,x):
	a,b,c=s
	y=a*x**2+b*x+c
	return( y)    #Model function to fit
###############################################

def log_likelihood(theta, x, y, yerr):
	a,b,c = theta
	model = a*x*x+b*x+c
	sigma_y2 = yerr**2
#negative lnL
	return (0.5*np.sum((y - model)**2/sigma_y2 +np.log(2*np.pi*sigma_y2)))

def log_prior(theta):
	a,b,c = theta
	if (-500.0< a <500.0 and -500.0< b <1000.0 and -500.< c <500.0):
		return (0.0)
	return (-np.inf)

def log_probability(theta, x, y, yerr):
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return (-np.inf)
	return (lp - log_likelihood(theta, x, y, yerr))

guess = (1.0, 8.0, 10.0)  #Guess soln to find the minimun of likelihood
soln = minimize(log_likelihood,guess,args=(x, y, sigma_y))

nchain, dim =50,3  #50 Markov chain to make for 3 different parameter each
pos = soln.x + 1e-4*np.random.randn(nchain, dim) #initial positions of the markov chains


sampler=emcee.EnsembleSampler(nchain,dim,log_probability,args=(x, y, sigma_y)) #Markov chain of 4000 steps

sampler.run_mcmc(pos, 4000)
p_data = sampler.get_chain() #getting about Markov chain-plotting purpose
parameter_data = sampler.get_chain(discard=200,thin=30,flat=True) #flattening data 

fig, axs = plt.subplots(3)
fig.suptitle('50 Markov chains for first 200 steps for three parameters')
axs[0].plot(p_data[1:200, :, 0],'-k',linewidth='0.5')
axs[0].set_title('Parameter a')
axs[1].plot(p_data[1:200, :, 1],'-k',linewidth='0.5')		#To plot Markov chains of 1st 200 steps for 3 parameters a,b,c
axs[1].set_title('Parameter b')
axs[2].plot(p_data[1:200, :, 2],'-k',linewidth='0.5')
axs[2].set_title('Parameter c')
for ax in axs.flat:
    ax.set(xlabel='Steps', ylabel='Range')
for ax in axs.flat:
    ax.label_outer()

medians = np.median(parameter_data,axis=0) #best fit values of the parameter-median of distribution
a_true,b_true,c_true= medians

labels=["a","b","c"]
fig2=corner.corner(parameter_data,labels=labels,truths=[a_true,b_true,c_true])  # plotting distribution and joint distributions for a,b,c

x0 = np.linspace(40, 300, num=500)

pts=np.random.randint(len(parameter_data), size=200)
fig3 = plt.figure()
for points in pts:
	sample = parameter_data[points]   #Plotting model function using 200 random values from distribution samples
	plt.plot(x0,poly_fit(sample[:3],x0), 'y')
plt.errorbar(x, y, yerr=sigma_y, fmt=".k", capsize=3, label="Given data with errorbars") #Plotting original data 
plt.plot(x0, a_true * x0**2 + b_true*x0 + c_true, "k", label="Best fit curve using the model function") # plotting best fit curve
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()









