# -*- coding: gb18030 -*-
#由于数据处理中经常出现识别不了编码的问题，所以在此进行转换



import csv
import pandas as pd

# 指定CSV文件路径
input_file_path = 'C:\\Users\\XiaoYu\\Desktop\\temp.csv'
output_file_path = 'C:\\Users\\XiaoYu\\Desktop\\output.csv'
converted_file_path = 'C:\\Users\\XiaoYu\\Desktop\\converted.csv'

# 定义编码列表
encodings = ['utf-8', 'gbk', 'gb2312', 'big5', 'gb18030']

# 尝试使用不同的编码读取文件并转换为目标编码
for encoding in encodings:
    try:
        # 读取CSV文件
        with open(input_file_path, 'r', encoding=encoding) as file:
            content = file.read()
        
        # 将文件内容转换为目标编码（如utf-8）
        with open(converted_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f'Successfully converted the file from {encoding} to utf-8.')
        break  # 成功读取文件后退出循环
    except UnicodeDecodeError:
        print(f'Failed to read CSV file with {encoding} encoding.')
    except Exception as e:
        print(f'Error reading CSV file with {encoding} encoding: {e}')

# 如果成功转换文件，则读取转换后的文件并提取所需列
try:
    # 读取转换后的CSV文件
    with open(converted_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # 提取需要的列数据
    extracted_data = [{'ip_location': row['ip_location'], 'content': row['content'], 'nickname': row['nickname']} for row in data]
    # 创建DataFrame
    df = pd.DataFrame(extracted_data)
    # 保存为CSV文件
    df.to_csv(output_file_path, index=False, encoding='gb18030')
    print(f'Successfully saved content data to {output_file_path}.')
except Exception as e:
    print(f'Error processing converted CSV file: {e}')
