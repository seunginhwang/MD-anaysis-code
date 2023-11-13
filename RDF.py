# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:01:29 2023

@author: iiz20
"""

import numpy as np
import MDAnalysis as mda
import pandas as pd
from math import pi

atom = 14
num_mol = 200
dr = 0.5
density = 110.11*200/714000

frame_number = 1001
t_inter = 50
num_tpr = 0  #tpr의 마지막 number (갯수 x)


def distance(p1, p2):
    res_dis = np.sqrt(np.sum(np.square(p1 - p2)))
    return res_dis 

def spere(r):
    answer = (4*pi*((r)*3))/3
    return answer

def ratio(universe):
    UNK = universe.select_atoms("resname UNK")
    for ts in universe.trajectory[1000:frame_number:t_inter]:  
        co = [0]
        pos = []
        count = []
        total = np.zeros((20, num_mol))
        
        for i in range(num_mol):
            stt_n = atom*i
            fin_n = atom*(i+1)-1
            for_UNK = UNK[stt_n:fin_n]
            co = for_UNK.center_of_mass()
            pos.append(list(co))
            #pos : 리간드들의 좌표가 저장된 2차원 리스트
        
        for i in range(num_mol): #0~49, UNK0부터 분석 시작
            for radius in range(20): #radius 10A까지, 0.5A 단위로 스캔
                point_1 = np.array(pos[i])
                count = 0
                for j in range(num_mol):
                    if j == i:
                        continue
                    point_2 = np.array(pos[j])
                    res_dis = distance(point_1, point_2)
                    if radius/2 <= res_dis <= (radius/2)+dr:
                        count+=1
                        
                #데이터 기록과 현황 출력      
                gr = count / (spere((radius/2)+dr)-spere(radius/2)) / density
                total[radius][i] = gr
                print("mol%d, radius %f : %d" %(i, radius/2, count))
       
    return total


######################################################################################################

final = np.zeros((20, 2))
rad = np.zeros((20, 1))

##tpr 분석 시작
for i in range(1, 2):
    result = ratio(mda.Universe(f"md_{i}" + '.tpr', f"300hqn_md_{i}" + '.xtc'))

avg_y = result.mean(axis=1)

for j in range (20):
    final[j][0] = j/2
    final[j][1] = avg_y[j]
for j in range (20):
    rad[j][0] = j/2
final2 = np.concatenate((rad, result),axis=1)

##최종 result 내보내기
df = pd.DataFrame(final)
df.to_csv('avg_result_05A.csv', index=False, header=False)

df = pd.DataFrame(final2)
df.to_csv('total_result_05A.csv', index=False, header=False)
for i in range(num_mol):
    df.to_csv(f"result_mol{i}_05A" + ".csv", columns = [0, i+1], index=False, header=False)









