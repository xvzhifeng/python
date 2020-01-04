1. 字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
      
        if __name__ == "__main__":
            dict = {"name" : "zs", "age" : 18, "city" : "深圳", "tel" : "1362626627"}
            dict1 = sorted(dict.items(),key = lambda x:x[0])
            print (dict1)    
2. 把上一题中字典的键保存到list_key列表中，值保存到list_value列表中

       if __name__ == "__main__" :
            dict = {"name" : "zs", "age" : 18, "city" : "深圳", "tel" : "1362626627"}

            list_key = dict.keys()
            list_value = dict.values()

            print (list_key)

            print (list_value)
       
3. 把字符串"i love good food" 每个单词的首字母大写，结果为"I Love Good Food"

       if __name__ == "__main__":

            a = "i love good food"
            s = "i love good food"

            print(a.title())

            s=' '.join([ch[0].upper()+ch[1:] for ch in s.split(' ')])
            print(s)
       
4. 把字符串"i love good food" 中重复的字符去除
   
   >集合(set)
    1.set是一个无序不重复的序列
    
   >2.可以用 { } 或者 set( ) 函数创建集合

   >3.集合存放不可变类型（字符串、数字、元组）

        # 结果无序,遍历列表s，把元素全部放入集合中，自动清除重复的字母
        s2=''.join(list(set([i for i in s ])))
        print(s2)
        
        # 结果有序,fromkeys创建一个字典，利用字典不能重复的原理，进行写入，然后只输出key部分

        dic={}.fromkeys([i for i in s ])

        print(''.join(dic.keys()))
        
5. 列表推导式一句话完成找出列表list=["iphone","sasung","oppen","iphone x"]元素中包含"iphone"的元素

        list=[k for k in list if 'iphone' in k]
        
        if __name__ == "__main__":
            list = ["iphone", "sasung", "oppen", "iphone x"]

            list1 = [i for i in list if "iphone" in i]

            print (list1)
6. 统计"i love good food" 每个字符出现的次数，结果展示为{"i":1,"o":5...

        res={i:s.count(i) for i in set([i for i in s])}
        
        if __name__ == "__main__":
            s = "i love good food"
            dict = {i:s.count(i) for i in s }
            print (dict)
7. ['a','b','c','d','e','f','g']每次从前往后顺序去三个字符，输出第n次取娜三个字符？

        if __name__ =="__main__":
            s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


            n = int(input("please input a number: "))

            for i in range(0,n):
            count = 3
            s1 = []
            for j in s:
                if(count == 0): break
                s1.append(j)
                count-=1
            if i != (n-1):
                for z in s1:
                    s.remove(z)
                    s.append(z)
                s1.clear()
            else:
                print (s1)

8. （选做题）根据athlete_events.csv 文件统计历史上金牌总数最高的三个国家和金牌数

        import pandas as pd
        import numpy as np
        # 进行具体的sum,count等计算时候要用到的

        if __name__ == "__main__":

            df = pd.read_csv('/Users/xzf-naber/Documents/山东科技大学/池星教育/作业/data/athlete_events.csv') # 这里绝对路径一定要用/,windows下也是如此,不加参数默认csv文件首行为标题行

            df1 = df[df.Medal == "Gold"]
            pf = df1.groupby(["NOC"])["Medal"].count()

            r=pf.sort_values()
            print(r[:-4:-1])