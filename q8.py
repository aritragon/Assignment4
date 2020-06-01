#Calculate the volume of d dim sphere using Monte Carlo integration
import numpy as np
import matplotlib.pyplot as plt

num = 60000 #no of random nos
d=2 # dimension of the sphere

R=np.zeros((num,d))

for i in range(d):
	R[:,i] = (np.random.rand(num)-0.5)*2# gerating random nos between -1 to +1 in d direction 

A=2**d # area of the d dim box of length 2 units (-1 to +1)
k=0
for i in range(num):
	radsq=0
	for j in range(d):
		radsq=radsq+R[i,j]**2 # collecting favourable points falling inside the d dim sphere
	if(radsq<=1):
		k+=1
I=(k*A)/num #Finding volume of d dim sphere by comparing ratios
print("Area of the circle is:\t",I)

###########################################################
#same process for d=10
num = 6000000
d=10

R=np.zeros((num,d))

for i in range(d):
	R[:,i] = (np.random.rand(num)-0.5)*2

A=2**d
k=0
for i in range(num):
	radsq=0
	for j in range(d):
		radsq=radsq+R[i,j]**2
	if(radsq<=1):
		k+=1
I=(k*A)/num
print("Area of the 10 d sphere is:\t",I)	
