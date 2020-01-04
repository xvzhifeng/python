"""
    @Author:sumu
    @Date:2020-01-03 20:00
    @Email:xvzhifeng@126.com

"""
import pandas as pd

import matplotlib.pylab as plt

"""
import matplotlib.pyplot as plt
 
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
 
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
 
plt.tick_params(axis='both', labelsize=12)
plt.show()

"""

"""
# Pandas模块绘制直方图和核密度图
# 读入数据
Titanic = pd.read_csv('titanic_train.csv')
# 绘制直方图
Titanic.Age.plot(kind = 'hist', bins = 20, color = 'steelblue', edgecolor = 'black', normed = True, label = '直方图')
# 绘制核密度图
Titanic.Age.plot(kind = 'kde', color = 'red', label = '核密度图')
# 添加x轴和y轴标签
plt.xlabel('年龄')
plt.ylabel('核密度值')
# 添加标题
plt.title('乘客年龄分布')
# 显示图例
plt.legend()
# 显示图形
plt.show()

"""

def histogram_salary(filePath):
    """
    功能：生成关于工资的数据的统计直方图
    :param filePath: csv文件路径
    :return:
    """
    # Pandas模块绘制直方图和核密度图
    # 读入数据
    Titanic = pd.read_csv(filePath)
    # 绘制直方图
    Titanic.最小工资.plot(kind='hist', bins=20, color='steelblue', edgecolor='black', normed=True, label='直方图')
    # 添加x轴和y轴标签
    plt.xlabel('salary')
    # 添加标题
    plt.title('Salary graph')
    # 显示图例
    plt.legend()
    # 显示图形
    plt.savefig("./AnalyseGraph/salary_graph.png")
    plt.show()


def Datasolution():
    pass


