# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:01:52 2017

@author: kyw1r13
"""
#This program selects the Turing points closest to the reference point in the parametric space. It requires an input file: 'turing1_band.txt'.#

#Import modules.#
import string
import numpy as numpy
import heapq as heapq
from matplotlib import *
from sympy import *
from scipy import *

#First, we load the file containing the Turing points and their dispersion relations. We will put them in a list; each element contains the parameters of a Turing point and its dispersion relation.#

file=open('turing1_band.txt','r')
band_temp=file.read().splitlines()
file.close()

band=[]
for i in band_temp:
    band.append(eval(i))

#Define the reference point in the parametric space.#

parameters=[1.9e5, 1.13e1, 2.25e1, 3.56, 3.6e1, 4.51, 2.66, 1.07, 1.81]

#Calculate the distance between each Turing point and the reference point.#    

band_distance=[]
for i in band:
    summation=0
    for j in range(9):
        summation=summation+((parameters[j]-i[j])/parameters[j])**2
    band_distance.append(sqrt(summation))

#Pick out the ten Turing points closest to the reference point. This algorithm does not distinguish among Turing points that lie at the same distance from the reference point. For example, if we input twelve Turing points with the same distance from the reference point, the algorithm will return all of them.#

band10_distance=heapq.nsmallest(10, band_distance)

band10_distance_set=[]
for i in set(band10_distance):
    band10_distance_set.append(i)
band10_distance_set.sort()

band10_index=[]
for i in band10_distance_set:
    for j, x in enumerate(band_distance):
        if x==i:
            band10_index.append(j)

band10=[]
for i in band10_index:
    band10.append(band[i])

#Finally, we will export our results.#

dataFile = open('band10.txt', 'w')
for eachitem in band10:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()