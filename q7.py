#chi sq test
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

cnt1=np.asarray([4,10,10,13,20,18,18,11,13,14,13])
cnt2=np.asarray([3,7,11,15,19,24,21,17,13,9,5])
score=np.asarray([2,3,4,5,6,7,8,9,10,11,12])

ps=np.asarray([1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36]) #theoretical probabilities for different sums to come out of two throws of  dice

sum1=sum(cnt1)
sum2=sum(cnt2)
n_ps=144*ps
V1=0
V2=0
for i in range (0,11):
	V1=V1+np.square(cnt1[i]-n_ps[i])/n_ps[i] #Finding relative sq  difference value 
	V2=V2+np.square(cnt2[i]-n_ps[i])/n_ps[i]

perc1=100*(1.0 -chi2.cdf(V1, 10.0))

#chances in percentages of getting a value more than or equal to V1 and V2 in a trial
perc2=100*(1.0 -chi2.cdf(V2, 10.0))

print('V1=',V1,'\t','V2=',V2,'\n')
print('perc of getting a value equal to or more than V1 is ',perc1,'\n')
print('perc of getting a value equal to or more than V1 is ',perc2,'\n')
print('The random no generator is not a good one')
