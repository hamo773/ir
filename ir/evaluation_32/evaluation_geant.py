import pandas as pd
import numpy as np
import json

init_num=10
total=10
indicator= np.zeros((total,37,3))
uti_list = np.zeros((total,37))

mlu_list = np.zeros(total)
delay_list = np.zeros(total)
loss_list = np.zeros(total)
troughput_list = np.zeros(total)
lu_sd_list = np.zeros(total)

for i in range(total):
    #file = './../ours_geant/Metrics/'+str(init_num+i)+'_net_metrics.csv'
    file = './../result/100/DQN_PS/TM12/'+ 'metrics' +  str(i+1)+ '.csv'
    data = pd.read_csv(file)
    for j in range(37):
        indicator[i][j][0] = data["used_bw"][j]/1000
        indicator[i][j][1] = data["delay"][j]
        indicator[i][j][2] = data["pkloss"][j]

u_s_sum = 0
u_v_sum = 0
delay_sum = 0
delay_sum_temp = 0
loss_sum = 0
loss_sum_temp = 0
max_uti = 0
max_uti_temp = 0
first_max_uti = 0
throughput_sum = 0
average_uti = 0
mlu_3 = 0
mlu_5 = 0
bwd = [100000,100000,100000,100000,100000,100000,100000,25000,25000,100000,
25000,1550,100000,100000,25000,25000,1550,1550,100000,25000,
100000,25000,25000,100000,25000,100000,100000,100000,100000,1550,
100000,25000,25000,100000,25000,25000,25000]

bwd = [x * 2 for x in bwd]

for i in range(total):
    delay_sum_temp = 0
    for j in range(37):
        delay_sum_temp += indicator[i][j][1]
    delay_sum = delay_sum + delay_sum_temp/37
    delay_list[i] = delay_sum_temp/37
    

for i in range(total):
    #print(i)
    loss_sum_temp = 0
    for j in range(37):
        loss_sum_temp += indicator[i][j][2]
    loss_sum = loss_sum + loss_sum_temp/37
    loss_list[i] = loss_sum_temp/37

for i in range(total):
    max_uti_temp = 0
    throughput_temp = 0 
    mlu_i =0
    avg_uti_temp = 0
    for j in range(37):
        uti = indicator[i][j][0]/bwd[j]
        uti=uti*100
        uti_list[i][j] = uti
        avg_uti_temp = avg_uti_temp + uti
        throughput_temp += indicator[i][j][0]/1000
        if uti > max_uti_temp:
            max_uti_temp = uti
            mlu_i = j
    max_uti = max_uti + max_uti_temp 
    average_uti = average_uti +avg_uti_temp/37
    throughput_sum = throughput_sum + throughput_temp/37
    mlu_list[i] = max_uti_temp 
    troughput_list[i] = throughput_temp/37

for j in range(37):
        uti = indicator[0][j][0]/bwd[j]
        if uti > first_max_uti:
            first_max_uti = uti

for i in range(total):
    variance = np.var(uti_list[i])
    std = np.std(uti_list[i])
    uti_list.sort()
    mlu_3 += np.mean(uti_list[i][-3:])
    mlu_5 += np.mean(uti_list[i][-5:])
    u_s_sum += std
    u_v_sum += variance 
    lu_sd_list[i] = std


#print(mlu_list)
print("delay:",delay_sum/total)
print("loss:",loss_sum/total)
print("max_uti:",max_uti/total)
#print("mlu_3:",mlu_3/total)
#print("mlu_5:",mlu_5/total)
#print("avg uti:",average_uti/total)
print("throughput",throughput_sum/total)
print("variance:",u_v_sum/total)
print("std:",u_s_sum/total)
print("delay_std: " ,np.std(delay_list))
print("loss_std: " ,np.std(loss_list))
print("throughtput_std: " ,np.std(troughput_list))
print("mlu_std: " ,np.std(mlu_list))
print("lu_sd_std: " ,np.std(lu_sd_list))

