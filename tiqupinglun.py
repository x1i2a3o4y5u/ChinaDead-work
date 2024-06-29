# -*- coding: gb18030 -*-
#用于抖音评论数据筛选，将爬取到的抖音评论区数据进行提取(只保留昵称、IP、评论内容)


import csv
import pandas as pd

# 指定CSV文件路径
file_path = 'I:\\Program Files\\MediaCrawler-main\\data\\douyin\\1_detail_comments_2024-06-29.csv'
output_file_path = 'C:\\Users\\XiaoYu\\Desktop\\temp.csv'

# 定义编码列表
encodings = ['utf-8', 'gbk', 'gb2312', 'big5', 'gb18030']

# 初始化一个空的DataFrame来存储数据
df = pd.DataFrame()

# 尝试使用不同的编码读取文件
for encoding in encodings:
    try:
        # 读取CSV文件
        with open(file_path, 'r', encoding=encoding) as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        # 提取需要的列数据
        extracted_data = [{'ip_location': row['ip_location'], 'content': row['content'], 'nickname': row['nickname']} for row in data]
        # 创建DataFrame
        df = pd.DataFrame(extracted_data)
        print(f'Successfully read the file with {encoding} encoding.')
        break  # 成功读取文件后退出循环
    except UnicodeDecodeError:
        print(f'Failed to read CSV file with {encoding} encoding.')
    except Exception as e:
        print(f'Error reading CSV file with {encoding} encoding: {e}')

# 检查是否成功读取到数据
if not df.empty:
    # 保存为CSV文件
    df.to_csv(output_file_path, index=False, encoding='gb18030')
    print(f'Successfully saved content data to {output_file_path}.')
else:
    print('Failed to read the file with all provided encodings.')
