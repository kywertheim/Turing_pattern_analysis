# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:34:13 2017

@author: kyw1r13
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:59:18 2016

@author: kyw1r13
"""
#This program generates figures 6.2, 6.3, and 6.6. It requires an input file: 'band10.txt'.#

#Import modules.#

import string
import numpy as numpy
import heapq as heapq
from matplotlib import *
from sympy import *
from scipy import *

#Import results.#

file=open('band10.txt','r')
band10_temp=file.read().splitlines()
file.close()

band10=[]
for i in band10_temp:
    band10.append(eval(i))

#Define the relevant range of wavenumbers.#
n=range(0,88)

#Plot figures 6.2(a) and 6.2(b).#
pyplot.figure()
pyplot.plot(n,band10[1][11],marker='.',linestyle='None',color='blue',label='a1m2=0.451, a1vc=2.66')
pyplot.plot(n,band10[2][11],marker='*',linestyle='None',color='red',label='a1m2=4.51, a1vc=26.6')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.legend(loc=3)
pyplot.suptitle('b1=1900000, b2=1.13, b3=22.5, b4=35.6, b5=3.6, a2m2=107, a2vc=18.1')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Plot figures 6.2(c) and 6.2(d).#
pyplot.figure()
pyplot.plot(n,band10[3][11],marker='.',linestyle='None',color='blue',label='a1m2=0.451, a1vc=2.66')
pyplot.plot(n,band10[8][11],marker='*',linestyle='None',color='red',label='a1m2=4.51, a1vc=26.6')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.legend()
pyplot.suptitle('b1=190000, b2=1.13, b3=22.5, b4=356, b5=36, a2m2=107, a2vc=18.1')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Plot figures 6.2(e) and 6.2(f).#
pyplot.figure()
pyplot.plot(n,band10[7][11],marker='.',linestyle='None',color='blue',label='a1m2=0.0451, a1vc=0.266')
pyplot.plot(n,band10[5][11],marker='*',linestyle='None',color='red',label='a1m2=0.451, a1vc=2.66')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.legend()
pyplot.suptitle('b1=19000, b2=1.13, b3=22.5, b4=356, b5=36, a2m2=107, a2vc=18.1')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Plot figure 6.3.#
big=pyplot.figure()

#Plot figure 6.3(a).#
big.add_subplot(2,2,1)
pyplot.plot(n,band10[0][11],marker='*',linestyle='None',color='red')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.title('b1=1900000, b2=1.13, b3=22.5, b4=35.6, b5=3.6,\n a1m2=0.0451, a1vc=2.66, a2m2=107, a2vc=1.81')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Plot figure 6.3(b).#
big.add_subplot(2,2,2)
pyplot.plot(n,band10[4][11],marker='*',linestyle='None',color='red')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.title('b1=1900000, b2=1.13, b3=22.5, b4=356, b5=36,\n a1m2=0.0451, a1vc=2.66, a2m2=107, a2vc=1.81')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Plot figure 6.3(c).#
big.add_subplot(2,2,3)
pyplot.plot(n,band10[6][11],marker='*',linestyle='None',color='red')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.title('b1=19000000, b2=1.13, b3=22.5, b4=35.6, b5=3.6,\n a1m2=0.0451, a1vc=2.66, a2m2=107, a2vc=1.81')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Plot figure 6.3(d).#
big.add_subplot(2,2,4)
pyplot.plot(n,band10[9][11],marker='*',linestyle='None',color='red')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.title('b1=1900, b2=113, b3=2250, b4=3.56, b5=36,\n a1m2=0.451, a1vc=2.66, a2m2=107, a2vc=18.1')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')

#Plot figure 6.6.#
pyplot.figure()
pyplot.plot(n,band10[4][11],marker='.',linestyle='None',color='blue',label='5')
pyplot.plot(n,band10[8][11],marker='*',linestyle='None',color='red',label='9')
pyplot.axhline(y=0, xmin=0, xmax=100, hold=None, color='black')
pyplot.legend(loc=1)
pyplot.suptitle('Turing Point for Simulation')
pyplot.xlabel('n')
pyplot.ylabel('Maximum Eigenvalue (Real Part)')