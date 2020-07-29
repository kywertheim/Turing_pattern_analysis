# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:16:43 2017

@author: kyw1r13
"""
#This program generates figure 6.5.#

#Import modules.#
import string
import numpy as numpy
import heapq as heapq
from matplotlib import *
from sympy import *
from scipy import *

#First, define a function that calculates the real part of the maximum eigenvalue of a Turing point candidate at a wavenumber.#

def turing_senb4(b4,k2):

#This function takes two arguments, the b4 value and wavenumber under consideration.#
#The other parameters are held constant as follows.#
    
    b1=1.9e3
    b2=113.0
    b3=2250.0
    b5=36.0
    a1m2=0.451
    a1vc=2.66
    a2m2=107.0
    a2vc=18.1
    a3=1.19e-1
    a4=3e-1

#Calculate the homogeneous steady state for the b4 value under consideration.#

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

#Create a list of the b4 values of interest. This is a wide range.#

testb4_wide=[0.0356,0.356,3.56,35.6,356.0]

#Create a list to hold the dispersion relations for the b4 values of interest.#

b4dispersion_wide=[]

#Consider the b4 values one by one.#
 
for i in testb4_wide:

#Create a list to hold the real part of the maximum eigenvalue of B at each wavenumber.#

    dispersion=[]
		
#Use the function defined earlier to compute the real part of the maximum eigenvalue of B at each wavenumber.#

    for k2 in [(n*pi)**2 for n in range (0,88)]:
        dummy=turing_senb4(i,k2)
        dispersion.append(dummy)
				
#Place the complete dispersion relation for the b4 value under consideration into the list of dispersion relations.#            

    b4dispersion_wide.append(dispersion)
    
#Do the same for a narrower range of b4 values.#

testb4_narrow=[3.56/10,3.56/5,3.56,3.56*5,3.56*10]
b4dispersion_narrow=[]

for i in testb4_narrow:
    dispersion=[]

    for k2 in [(n*pi)**2 for n in range (0,88)]:
        dummy=turing_senb4(i,k2)
        dispersion.append(dummy)
            
    b4dispersion_narrow.append(dispersion)
		
#There are two groups of b4 values, wide and narrow. We will create one big figure with two subplots, one for each group.#
#For each subplot, the x-axis represents n which goes from 0 to 87.#
    
n=range(0,88)

#Create and title one big figure that contains both subplots.#

big=pyplot.figure()
pyplot.suptitle('Bifurcation Analysis of the following Turing Point with Respect to b4: \n b1=1900, b2=113, b3=2250, b4=3.56, b5=36, a1m2=0.451, a1vc=2.66, a2m2=107, a2vc=18.1')

#Create the first subplot: the wide range of b4 values.#

big.add_subplot(211)
pyplot.plot(n,b4dispersion_wide[0],marker='.',linestyle='None',color='blue',label='b4=0.0356')
pyplot.plot(n,b4dispersion_wide[1],marker='*',linestyle='None',color='red',label='b4=0.356')
pyplot.plot(n,b4dispersion_wide[2],marker='o',linestyle='None',color='green',label='b4=3.56')
pyplot.plot(n,b4dispersion_wide[3],marker='x',linestyle='None',color='magenta',label='b4=35.6')
pyplot.plot(n,b4dispersion_wide[4],marker='s',linestyle='None',color='yellow',label='b4=356')
pyplot.legend()
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Create the second subplot: the narrow range of b4 values.#

big.add_subplot(212)
pyplot.plot(n,b4dispersion_narrow[0],marker='.',linestyle='None',color='blue',label='b4=0.356')
pyplot.plot(n,b4dispersion_narrow[1],marker='*',linestyle='None',color='red',label='b4=0.712')
pyplot.plot(n,b4dispersion_narrow[2],marker='o',linestyle='None',color='green',label='b4=3.56')
pyplot.plot(n,b4dispersion_narrow[3],marker='x',linestyle='None',color='magenta',label='b4=17.8')
pyplot.plot(n,b4dispersion_narrow[4],marker='s',linestyle='None',color='yellow',label='b4=35.6')
pyplot.legend()
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')