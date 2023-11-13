# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:12:23 2023

@author: iiz20
"""

import numpy as np
import pandas as pd

def distance(p1, p2):
    res_dis = np.sqrt(np.sum(np.square(p1 - p2)))
    return res_dis 

s_overlap = []
square = []
ratio = []
num_dat = 21

for i in range(0, num_dat):
    if i >= 1:
        print("(overlap f%d, f%d) / (f%d) is %f" %(i-1,i,i-1,(s_overlap[i-1]/square[i-1])))
        ratio.append((s_overlap[i-1]/square[i-1]))
        
    old1 = 1
    print("\nanalysis f%d data ..." %i)
    g1 = np.zeros((20, 2))
    g2 = np.zeros((20, 2))
    
    with open(f"f{i}" + '.dat' , 'r') as lis:
        line = lis.read().splitlines()
    for j in range(5, 25):
        line_split = line[j].split()
        g1[j-5][0] = line_split[0]
        g1[j-5][1] = line_split[1]
    
    with open(f"f{i+1}" + '.dat' , 'r') as lis:
        line = lis.read().splitlines()
    for j in range(5, 25):   #20줄
        line_split = line[j].split()
        g2[j-5][0] = line_split[0]
        g2[j-5][1] = line_split[1]

    for k in range(19):
        minus = []
        for l in range(19):
            minus.append(abs(g1[k][0]-g2[l][0]))
        
        ab = abs(g1[k][1]-g2[minus.index(min(minus))][1])
        if 18> k > 8 and ab < old1:
            old1 = ab
            index = k
            index2 = minus.index(min(minus))
    
    print("\nindex is ...",index, index2)
    print("x_g1 is", g1[index][0])
    print("x_g2 is", g2[index2][0])
    print("y_g1 is", g1[index][1])
    print("y_g2 is", g2[index2][1])
    
    s1=0
    s2=0
    s_a=0
    s_b=0

    for i in range(19):
        s_a += ((g1[i+1][0])-(g1[i][0]))*(g1[i][1])
    if i == 0:
        square.append(s_a)
    for i in range(19):
        s_b += ((g2[i+1][0])-(g2[i][0]))*(g2[i][1])
    square.append(s_b)
        
    for i in range(index, 19):
        s1 += ((g1[i+1][0])-(g1[i][0]))*(g1[i][1])
    for j in range(0, index2+1):
        s2 += ((g2[j][0])-(g2[j-1][0]))*(g2[j][1])

    s_overlap.append(s1+s2)
    
ratio.append((s_overlap[len(s_overlap)-1]/square[len(square)-1]))        
result = np.zeros((num_dat,2))
for i in range(num_dat):
    result[i][0] = i
    result[i][1] = ratio[i]

df = pd.DataFrame(result)
df.to_csv('overlap_ratio.csv', index=False, header=False)

             
         
             
         
            
         
            
         
            