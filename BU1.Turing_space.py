# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:33:46 2017

@author: kyw1r13
"""
#This program samples the parametric space to find Turing points.#

#Import modules.#

import string
import numpy as numpy
import heapq as heapq
from matplotlib import *
from sympy import *
from scipy import *

#First of all, we need to define two functions used to test a Turing point candidate.#

def turing_cand(b1,b2,b3,b4,b5):

#This function checks if the kinetic parameters of a Turing point candidate satisfy the first three constraints.#
		
    score=0
    
#Constraint two.#

    if b2<b3:
        score=score+1
        print 'Good. Properly scaled.'
    else:
        print 'Bad. Beyond the concentration scales.'
    
#Use the kinetic parameters to calculate the concentrations at the homogeneous steady state.#

    vc_ss=sqrt(b2/b3)
    c1_ss=sqrt(b2/b3)
    m2_ss=b2/b3
    vcc1_ss=b2/b3

#Constraint one.#

    if c1_ss*5.29e-4>1e-4:
        score=score+1
        print 'Good. There is enough collagen I.'
    else:
        print 'Bad. There is too little collagen I.'
        
#Find out the eigenvalues of the matrix named A.#

    homo=numpy.array([[-1,c1_ss,vc_ss,0],[0,-1-b1*c1_ss,1-b1*vc_ss,b1],[-b3,-b4*c1_ss,-b4*vc_ss,b4],[0,b5*c1_ss,b5*vc_ss,-b5]])
    homo_eig,homo_eigv=numpy.linalg.eig(homo)
    
#Constraint three.#

    if max(homo_eig.real)<0:
        score=score+1
        print 'Good. The steady state is stable with respect to homogeneous perturbations.'
    else:
        print 'Bad. The steady state is unstable with respect to homogeneous perturbations.'
    
#Return the number of constraints out of constraints one, two, and three that are satisfied.#

    return score
      
def turing_in(b1,b2,b3,b4,b5,a1m2,a1vc,a2m2,a2vc,a3,a4,k2):

#This function calculates the real part of the maximum eigenvalue of a Turing point candidate at a wavenumber.#
#Use the kinetic parameters to calculate the concentrations at the homogeneous steady state.#

    vc_ss=sqrt(b2/b3)
    c1_ss=sqrt(b2/b3)
    m2_ss=b2/b3
    vcc1_ss=b2/b3

#Find out the eigenvalues of the matrix named B.#

    d1m2=a1m2*exp(-a2m2*sqrt(a3*c1_ss+a3*b4*vcc1_ss/b5))/(1-a4*c1_ss-a4*b4*vcc1_ss/b5)
    d2m2=a1m2*exp(-a2m2*sqrt(a3*c1_ss+a3*b4*vcc1_ss/b5))*a4*m2_ss/(1-a4*c1_ss-a4*b4*vcc1_ss/b5)**2
    d3m2=a1m2*exp(-a2m2*sqrt(a3*c1_ss+a3*b4*vcc1_ss/b5))*a4*b4*m2_ss/(b5*(1-a4*c1_ss-a4*b4*vcc1_ss/b5)**2)
    d1vc=a1vc*exp(-a2vc*sqrt(a3*c1_ss+a3*b4*vcc1_ss/b5))/(1-a4*c1_ss-a4*b4*vcc1_ss/b5)
    d2vc=a1vc*exp(-a2vc*sqrt(a3*c1_ss+a3*b4*vcc1_ss/b5))*a4*vc_ss/(1-a4*c1_ss-a4*b4*vcc1_ss/b5)**2
    d3vc=a1vc*exp(-a2vc*sqrt(a3*c1_ss+a3*b4*vcc1_ss/b5))*a4*b4*vc_ss/(b5*(1-a4*c1_ss-a4*b4*vcc1_ss/b5)**2) 
        
    hete=numpy.array([[-1-k2*d1m2,c1_ss,vc_ss-k2*d2m2,-k2*d3m2],[0,-1-b1*c1_ss-k2*d1vc,1-b1*vc_ss-k2*d2vc,b1-k2*d3vc],[-b3,-b4*c1_ss,-b4*vc_ss,b4],[0,b5*c1_ss,b5*vc_ss,-b5]])
    hete_eig,hete_eigv=numpy.linalg.eig(hete)
    
#Return the real part of the maximum eigenvalue of B.#

    return max(hete_eig.real)

#Having defined the functions, we will now use them to study our 1953125 Turing point candidates. They have 3125 combinations of kinetic parameters. Our first step is to shortlist these combinations using the first three constraints.#

#We will create a list to contain the shortlisted combinations of kinetic parameters.#

candidate=[]

#Vary each kinetic parameter by two orders of magnitude in each direction. Test if each resulting combination of kinetic parameters satisfies the first three constraints.#

for i in [1,0.1,0.01,10,100]:
    for j in [1,0.1,0.01,10,100]:
        for k in [1,0.1,0.01,10,100]:
            for l in [1,0.1,0.01,10,100]:
                for m in [1,0.1,0.01,10,100]:
                    b1=1.9e5*i
                    b2=1.13e1*j
                    b3=2.25e1*k
                    b4=3.56*l
                    b5=3.6e1*m
                    
                    if turing_cand(b1,b2,b3,b4,b5)==3:
                        candidate.append([b1,b2,b3,b4,b5])
												
#There are 537 combinations of kinetic parameters in the shortlist. It means 67125 Turing point candidates satisfy the first three constraints. We will test if they satisfy the final three constraints and obtain their dispersion relations.#   
       
#The shortlisted candidates are either stable or unstable with respect to heterogeneous perturbations. Create two lists to contain the two groups of candidates.#

unstable=[]
stable=[]
count=0

#Vary each diffusion coefficient and viscosity by two orders of magnitude in each direction. Obtain the dispersion relation of each resulting Turing point candidate. Check if it satisfies constraint four.#

for i in [1,0.1,0.01,10,100]:
    for j in [1,0.1,0.01,10,100]:
        for k in [1,0.1,0.01,10,100]:
            for l in candidate:
                a1m2=4.51*i
                a1vc=2.66*j
                a2m2=1.07/i/k
                a2vc=1.81/j/k
                a3=1.19e-1
                a4=3e-1
                b1=l[0]
                b2=l[1]
                b3=l[2]
                b4=l[3]
                b5=l[4]
                
#For each relevant wavenumber (n from 0 to 87, inclusive), find out the eigenvalue of B with the maximum real part. The collection of these eigenvalues is the dispersion relation of the Turing point candidate under consideration.#

                dispersion=[]
                for k2 in [(n*pi)**2 for n in range (0,88)]:
                    dummy=turing_in(b1,b2,b3,b4,b5,a1m2,a1vc,a2m2,a2vc,a3,a4,k2)
                    dispersion.append(dummy)
                
#Constraint four. If the Turing point candidate satisfies constraint four, it is unstable with respect to heterogeneous perturbations.#

                if max(dispersion)>0:
                    count=count+1
                    print 'New unstable candidate:', count
                    unstable.append([b1,b2,b3,b4,b5,a1m2,a1vc,a2m2,a2vc,a3,a4,dispersion])
                else:
                    stable.append([b1,b2,b3,b4,b5,a1m2,a1vc,a2m2,a2vc,a3,a4,dispersion])
                         
#Next, we will test if the Turing point candidates that are unstable with respect to heterogeneous perturbations satisfy constraints five and six. If a candidate satisfies both constraints, it qualifies as a Turing point. If a candidate satisfies constraint five only, its dispersion relation has a maximum in the relevant range of wavenumbers (2<n<87), but it does not have a bounded positive region in the assessed range (n from 0 to 87, inclusive).#
#Create two lists to contain these two classes of Turing point candidates.#

band=[]
maximum=[]
count1=0
count2=0

#Test all the Turing point candidates that are unstable with respect to heterogeneous perturbations.#

for i in unstable:

#Pick out the dispersion relation of the candidate being tested.#

    dispersion=i[11]
    
#Find out its maximum and the corresponding wavenumber or value of n.#

    max_value=max(dispersion)
    max_index=dispersion.index(max(dispersion))
    
#Constraint five. If the maximum does not lie where n is 0, 1, 2, or 87, the candidate satisfies constraint five.#

    if max_index != 0 and max_index !=1 and max_index !=2 and max_index !=87:
        dispersion_short=dispersion[max_index:]

#Constraint six.#

        if max(dispersion_short)*min(dispersion_short)<0:
            band.append(i)
            count1=count1+1
            print 'New Turing point:', count1
        else:
            maximum.append(i)
            count2=count2+1
            print 'New maximum:', count2
            
#Finally, we will export our results.#
            
#This file contains the shortlisted combinations of kinetic parameters. There are 537 of them, corresponding to 67125 Turing point candidates.#

dataFile = open('shortlist.txt', 'w')
for eachitem in candidate:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()

#This file contains the shortlisted Turing point candidates that are stable with respect to heterogeneous perturbations. There are 14951 of them.#

dataFile = open('stable.txt', 'w')
for eachitem in stable:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()

#This file contains the shortlisted Turing point candidates that are unstable with respect to heterogeneous perturbations. There are 52174 of them.#

dataFile = open('unstable.txt', 'w')
for eachitem in unstable:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()

#This file contains the Turing points. There are 94 of them.#

dataFile = open('turing1_band.txt', 'w')
for eachitem in band:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()

#This file contains the Turing point candidates that do not satisfy constraint six only. There are 32 of them.#

dataFile = open('turing2_maximum.txt', 'w')
for eachitem in maximum:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()