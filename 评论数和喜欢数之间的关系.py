import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# 加载数据路径
us_file_path = "./USvideos01.csv"
uk_file_path = "./GBvideos01.csv"

# 加载数据
us_data = np.loadtxt(us_file_path, dtype=np.int, delimiter=",", unpack=False)
uk_data = np.loadtxt(uk_file_path, dtype=np.int, delimiter=",")
# print(us_data)
# print("*"*100)

# 选择喜欢数比比500000小的数据
us_data = us_data[us_data[:, 1] <= 500000]
print(us_data)
# 获取评论的数据
us_data_comments = us_data[:, -1]
us_data_likes = us_data[:, 1]
print(us_data_comments)
print(us_data_likes)
print("*" * 100)

# uk_data_comments = uk_data[:, -1]
# uk_data_likes=uk_data[:,1]
# print(uk_data_comments)
# print(uk_data_likes)
# print("*" * 100)

# 选择比5000小的数据
# us_data_comments=us_data_comments[us_data_comments<=5000]
# # print(us_data_comments.max(), us_data_comments.min())
#
# d = 50
# bin_nums = (us_data_comments.max()-us_data_comments.min())// d
# print(bin_nums)
#
# 绘图
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(us_data_likes, us_data_comments)

# 绘制网格
plt.grid(alpha=0.4)
plt.show()
