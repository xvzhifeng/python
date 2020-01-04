
import pandas as pd
import numpy as np
# 进行具体的sum,count等计算时候要用到的

if __name__ == "__main__":




    df = pd.read_csv('/Users/xzf-naber/Documents/山东科技大学/池星教育/作业/data/athlete_events.csv') # 这里绝对路径一定要用/,windows下也是如此,不加参数默认csv文件首行为标题行


    df1 = df[df.Medal == "Gold"]
    pf = df1.groupby(["NOC"])["Medal"].count()


    r=pf.sort_values()
    print(r[:-4:-1])

