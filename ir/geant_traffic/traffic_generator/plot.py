import matplotlib.pyplot as plt
from ast import literal_eval

file_path = 'output1_3.txt'

with open(file_path, 'r') as file:
    data_str = file.read()
    data = literal_eval(data_str)
    #data = [float(line.strip()) for line in file]

data2 = data[13:] + data[:13]
#index = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5,6]
#blue_indices = [13,15,17,19,20,22,23,0,2,4,7,8,9,11]
blue_indices = [0,2,4,6,7,9,10,11,13,15,18,19,20,22]
tms_14_hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
red_indices = [3, 6,10 , 16]
red_indices = [14, 17,21 , 3]
orange_indices = [12]


# 生成颜色列表
colors = []
# 绘制散点图
for i in range(len(data)):
    if i in blue_indices:
        plt.scatter(i, data2[i], color='blue')
    elif i in red_indices:
        plt.scatter(i, data2[i], color='red')
    elif i in orange_indices:
        plt.scatter(i, data2[i], color='orange')
#plt.scatter(range(len(data)), data)
#plt.scatter(index, data)
plt.xlabel('TMs')
plt.ylabel('Load (kbps)')
plt.title("GÉANT topology loads")
plt.xticks(tms_14_hours)
plt.grid()
plt.savefig('tm_geant.png', dpi=200, bbox_inches='tight')
plt.show()


# 指定你的檔案路徑
