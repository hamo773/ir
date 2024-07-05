import pandas as pd
import numpy as np
import json

init_num=47
total=10
indicator= np.zeros((total,60,3))
    
for i in range(total):
    file = './../ours_32node/Metrics/'+str(init_num+i)+'_net_metrics.csv'
    data = pd.read_csv(file)
    for j in range(60):
        indicator[i][j][0] = data["used_bw"][j]/1000
        indicator[i][j][1] = data["delay"][j]
        indicator[i][j][2] = data["pkloss"][j]
#print(indicator[0])

delay_sum = 0
delay_sum_temp = 0
loss_sum = 0
loss_sum_temp = 0
max_uti = 0
max_uti_temp = 0
first_max_uti = 0
throughput_sum = 0
bwd = [200000] * 60
#print(my_list)
"""bwd = [100000,100000,100000,100000,100000,100000,100000,25000,25000,100000,
25000,1550,100000,100000,25000,25000,1550,1550,100000,25000,
100000,25000,25000,100000,25000,100000,100000,100000,100000,1550,
100000,25000,25000,100000,25000,25000,25000]"""

for i in range(total):
    delay_sum_temp = 0
    for j in range(60):
        delay_sum_temp += indicator[i][j][1]
    delay_sum = delay_sum + delay_sum_temp/60
    

for i in range(total):
    #print(i)
    loss_sum_temp = 0
    for j in range(60):
        loss_sum_temp += indicator[i][j][2]
    loss_sum = loss_sum + loss_sum_temp/60

for i in range(total):
    max_uti_temp = 0
    throughput_temp = 0 
    for j in range(60):
        uti = indicator[i][j][0]/bwd[j]
        throughput_temp += indicator[i][j][0]/1000
        #print(uti)
        """if uti > max_uti:
            #print(i,j)
            print(i,j,indicator[i][j][0],bwd[j],uti)
            max_uti = uti"""
        if uti > max_uti_temp:
            max_uti_temp = uti
            #print(j)
    max_uti = max_uti + max_uti_temp 
    throughput_sum = throughput_sum + throughput_temp/60

for j in range(60):
        uti = indicator[0][j][0]/bwd[j]
        #print(uti)
        if uti > first_max_uti:
            #print(i,j,indicator[0][j][j],bwd[j],uti)
            first_max_uti = uti

print(init_num)
print("delay:",delay_sum/total)
print("loss:",loss_sum/total)
print("max_uti:",max_uti/total)
print("throughput",throughput_sum/total)
#print("first_max_uti:",first_max_uti)
