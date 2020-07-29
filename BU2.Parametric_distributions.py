# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:27:07 2017

@author: kyw1r13
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:43:11 2016

@author: kyw1r13
"""
#This program generates figure 6.1. It requires an input file: 'turing1_band.txt'.#

#Import modules.#

import string
import numpy as numpy
import heapq as heapq
from matplotlib import *
from sympy import *
from scipy import *

#Import results.#

file=open('turing1_band.txt','r')
band_temp=file.read().splitlines()
file.close()

band=[]
for i in band_temp:
    band.append(eval(i))
    
#Create a list for each parameter.#

band_b1=[]
band_b2=[]
band_b3=[]
band_b4=[]
band_b5=[]
band_a1m2=[]
band_a1vc=[]
band_a2m2=[]
band_a2vc=[]
band_a3=[]
band_a4=[]

#For each list, add the values of the corresponding parameter at the Turing points.#
for n in band:
    band_b1.append(n[0])
    band_b2.append(n[1])
    band_b3.append(n[2])
    band_b4.append(n[3])
    band_b5.append(n[4])
    band_a1m2.append(n[5])
    band_a1vc.append(n[6])
    band_a2m2.append(n[7])
    band_a2vc.append(n[8])
    band_a3.append(n[9])
    band_a4.append(n[10])

#Find out the full set of distinct objects for each parameter.#
set_band=[set(band_b1), set(band_b2), set(band_b3), set(band_b4), set(band_b5), set(band_a1m2), set(band_a1vc), set(band_a2m2), set(band_a2vc)]

#For each parameter, find out the count of each distinct object.#
b11=set_band[0]
b1y1=[]
for i in b11:
    b1y1.append(band_b1.count(i))
    
b21=set_band[1]
b2y1=[]
for i in b21:
    b2y1.append(band_b2.count(i))
    
b31=set_band[2]
b3y1=[]
for i in b31:
    b3y1.append(band_b3.count(i))
    
b41=set_band[3]
b4y1=[]
for i in b41:
    b4y1.append(band_b4.count(i))
    
b51=set_band[4]
b5y1=[]
for i in b51:
    b5y1.append(band_b5.count(i))
    
a1m21=set_band[5]
a1m2y1=[]
for i in a1m21:
    a1m2y1.append(band_a1m2.count(i))
    
a1vc1=set_band[6]
a1vcy1=[]
for i in a1vc1:
    a1vcy1.append(band_a1vc.count(i))
    
a2m21=set_band[7]
a2m2y1=[]
for i in a2m21:
    a2m2y1.append(band_a2m2.count(i))
    
a2vc1=set_band[8]
a2vcy1=[]
for i in a2vc1:
    a2vcy1.append(band_a2vc.count(i))

#Plot the statistics in pie charts.#
pyplot.figure()
suptitle('Distributions of Parameters in the Turing Space', fontsize='x-large')

pyplot.subplot(331)
pyplot.pie(b1y1,labels=b11)
pyplot.axis("equal")
title('b1')

pyplot.subplot(332)
pyplot.pie(b2y1,labels=b21)
pyplot.axis("equal") 
title('b2')

pyplot.subplot(333)
pyplot.pie(b3y1,labels=b31)
pyplot.axis("equal") 
title('b3')

pyplot.subplot(334)
pyplot.pie(b4y1,labels=b41)
pyplot.axis("equal") 
title('b4')

pyplot.subplot(335)
pyplot.pie(b5y1,labels=b51)
pyplot.axis("equal") 
title('b5')

pyplot.subplot(336)
pyplot.pie(a1m2y1,labels=a1m21)
pyplot.axis("equal") 
title('a1m2')

pyplot.subplot(337)
pyplot.pie(a1vcy1,labels=a1vc1)
pyplot.axis("equal") 
title('a1vc')

pyplot.subplot(338)
pyplot.pie(a2m2y1,labels=a2m21)
pyplot.axis("equal") 
title('a2m2')

pyplot.subplot(339)
pyplot.pie(a2vcy1,labels=a2vc1)
pyplot.axis("equal") 
title('a2vc')