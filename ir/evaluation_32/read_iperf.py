import os
import re

# 指定文件目录
directory = 'serveroutputs'
output_file = 'bitrate_summary.txt'

# 提取文件名中包含 '_to_3.json' 的文件
files_to_read = [f for f in os.listdir(directory) if f.endswith('_to_3.json')]

# 创建一个字典来保存每个文件的比特率信息
bitrate_info = {}

# 定义正则表达式匹配比特率，包括 Kbits/sec 和 Mbits/sec，且前面可以是整数或小数
bitrate_pattern = re.compile(r'(\d+(\.\d+)?)\s+(Kbits/sec|Mbits/sec)')

# 读取并提取比特率信息
for file in files_to_read:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
        bitrate_list = []
        for line in lines:
            match = bitrate_pattern.search(line)
            if match:
                value = float(match.group(1))
                unit = match.group(3)
                if unit == 'Kbits/sec':
                    value /= 1000  # 将 Kbits/sec 转换为 Mbits/sec
                bitrate_list.append(value)
        bitrate_info[file] = bitrate_list

# 计算每个 interval 的平均比特率
average_bitrate = []
if bitrate_info:
    num_intervals = max(len(bitrates) for bitrates in bitrate_info.values())
    for i in range(num_intervals):
        interval_bitrates = [bitrates[i] for bitrates in bitrate_info.values() if len(bitrates) > i]
        if interval_bitrates:
            average_bitrate.append(sum(interval_bitrates) / len(interval_bitrates))

# 将比特率信息和平均比特率写入文件
with open(output_file, 'w') as f:
    for file, bitrates in bitrate_info.items():
        f.write(f"File: {file}\n")
        for i, bitrate in enumerate(bitrates):
            f.write(f"  Interval {i+1}: {bitrate:.2f} Mbits/sec\n")
        f.write("\n")
    
    f.write("Average Bitrate per Interval:\n")
    for i, avg_bitrate in enumerate(average_bitrate):
        f.write(f"  Interval {i+1}: {avg_bitrate:.2f} Mbits/sec\n")

print(f"比特率信息和平均比特率已写入 {output_file}")
