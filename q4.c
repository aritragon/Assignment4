#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define ymin 0
#define ymax 5
double expo(double x)
{
	return(2*exp(-2*x));	//Exponential distribution with mean = 0.5
}

int main()
{
	
	FILE *mptr,*kptr;
	mptr=fopen("exp.dat","w");   // Opening files to write data
    	kptr=fopen("exp_hist.dat","w");
	int num=50000;
	int n_bins=50;
	int pts=50;

	double x[num];
	double Exp[num];
	double y[pts];
	double dy,runi;

	dy=(ymax-ymin)/(double)(pts-1.0);

	int i;
	for (i=0;i<num;i++)
	{	
		runi = (double)rand() / (double)RAND_MAX ;  //Random nos between 0 and 1
		
		x[i]=-0.5*log(runi);  //Exponentially distributed random numbers

		fprintf(kptr,"%e\n",x[i]); //Writing in datafile	
	}
		
	for (i=0;i<pts;i++)
	{

		y[i]=ymin+dy*i;    
		Exp[i]=expo(y[i]); 		//To match with the distribution function generating data for exp distribution for plotting purpose
		fprintf(mptr,"%e\t%e\n",y[i],Exp[i]); // writing in datafile
	}

	
//Will plot histogram using GNUplot separately
	
  return(0);
}












