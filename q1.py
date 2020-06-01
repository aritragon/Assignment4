#Generating random numbers with linear congruential generator
import numpy as np
import matplotlib.pyplot as plt

a=566446
c=118367464   #seed
m=1001    #range between 0 to (m-1)
x=2

num=10000
res=[]

for i in range(num):   #generating random nos using linear congruential generator
	x=0.001*((a*x+c)%m)  #to generate nos between 0 and 1 multiplying by 0.001
	res.append(x)

res=np.asarray(res)

num_bins = 30
fig=plt.figure()
plt.hist(res,num_bins, facecolor='green', density=True) #plotting histogram of random numbers
plt.title('Histogram of random nos between 0 and 1')
plt.show()
