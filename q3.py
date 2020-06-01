#Time to run the codes to generate random nos using lib func and lin. cong. generator
import numpy as np
import matplotlib.pyplot as plt
import time
a=566446
c=118367464   #seed
m=1001    #range between 0 to (m-1)
x=2

num=10000
res=[]

t=time.time()
for i in range(num):   #generating random nos using linear congruential generator
	x=0.001*((a*x+c)%m)  #to generate nos between 0 and 1 multiplying by 0.001
	res.append(x)

T_lcg=time.time()-t

t=time.time()

x = np.random.rand(10000) #using the library function

T_rand=time.time()-t

print("The time taken by linear congruential generator is:\t",T_lcg,'\n')  #printing Time taken
print("The time taken by numpy.random.rand() is:\t",T_rand,'\n')
