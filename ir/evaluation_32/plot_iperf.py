import matplotlib.pyplot as plt

# 文件名列表
input_files = ['dqn_ps_a_iperftest.txt', 'dqn_ps_iperftest.txt', 'dqn_iperftest.txt', 'drsir_iperftest.txt']
plt.rcParams.update({'font.size': 14})

# 初始化变量
intervals_list = []
total_transfer_list = []

# 读取并解析文件内容
for input_file in input_files:
    intervals = []
    total_transfer = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        total_section = False
        for line in lines:
            if 'Total Transfer per Interval:' in line:
                total_section = True
                continue
            if total_section and 'Interval' in line:
                parts = line.split(':')
                interval_number = int(parts[0].split()[-1])
                if 102 <= interval_number <= 202:
                    transfer_value = float(parts[1].strip().split()[0])
                    mapped_interval_number = interval_number - 102
                    intervals.append(mapped_interval_number)
                    total_transfer.append(transfer_value)
    intervals_list.append(intervals)
    total_transfer_list.append(total_transfer)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.ylim(86,109) 

optimal_total_throughput = 0
with open('optimal_iperftest.txt', 'r') as f:
    line = f.readline().strip()
    optimal_total_throughput = float(line.split(':')[-1].strip().replace('k', ''))
    print(optimal_total_throughput)
optimal_total_throughput_list = [optimal_total_throughput/1023] * 101

# 为每个文件绘制一条线
#for i in range(len(input_files)):
plt.plot(intervals_list[0], total_transfer_list[0], color='springgreen',label='DQN_PS_A')
plt.plot(intervals_list[1], total_transfer_list[1], color='dodgerblue',label='DQN_PS')
plt.plot(intervals_list[2], total_transfer_list[2], color='red',label='DQN')
plt.plot(intervals_list[3], total_transfer_list[3], color='m',label='DRSIR')
#plt.plot(intervals_list[3], optimal_total_throughput_list, color='orange', label='Optimal')

#plt.title('Total Transfer per Interval')
plt.xlabel('Times (second)')
plt.ylabel('Total troughput (Mbits)')
plt.legend(loc='upper center',ncol=5,fontsize='small')
#plt.grid(True)
plt.savefig('total_transfer_per_interval.png',dpi=200, bbox_inches='tight')  # 保存图表为图片文件
plt.show()  # 显示图表

