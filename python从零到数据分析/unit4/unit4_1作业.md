1. 设计一个函数实现列表冒泡排序

            """
            @Author:sumu
            @Date:2020-01-01 09:47
            @Email:xvzhifeng@126.com

            """

            #设计一个函数实现列表冒泡排序


            def bubbling(list,ascending = None):
            
                n = len(list)
                for i in range(n):
                    for j in range(n-i-1):
                        if ascending == True:
                            if list[j] < list[j+1]:
                                list[j],list[j+1] = list[j+1],list[j]
                        else:
                            if list[j] > list[j+1]:
                                list[j],list[j+1] = list[j+1],list[j]
                return list
            
            if __name__ == "__main__":
                list = [1,9,3,4,5,6]
                print(bubbling(list,True))
2. 设计一个函数实现列表选择排序

            """
                @Author:sumu
                @Date:2020-01-01 10:09
                @Email:xvzhifeng@126.com
            
            """
            #设计一个函数实现列表选择排序
            
            def selectionSort(list,ascending=None):
                n = len(list)
            
                for i in range(n):
                    temp = i
            
                    for j in range(i,n-1):
                        if ascending==True:
                            if list[temp] < list[j+1]:
                                temp = j+1
                        else:
                            if list[temp] > list[j+1]:
                                temp = j+1
                    list[temp],list[i] = list[i],list[temp]
            
            
            
                return list
            
            if __name__ == "__main__":
            
                list = [1,23,32,9,2,3]
            
                print(selectionSort(list))

3. 设计一个函数实现列表排序，通过参数指定排序规则，升序还是降序

            """
                @Author:sumu
                @Date:2020-01-01 10:09
                @Email:xvzhifeng@126.com
            
            """
            #设计一个函数实现列表选择排序
            
            def selectionSort(list,ascending=None):
                n = len(list)
            
                for i in range(n):
                    temp = i
            
                    for j in range(i,n-1):
                        if ascending==True:
                            if list[temp] < list[j+1]:
                                temp = j+1
                        else:
                            if list[temp] > list[j+1]:
                                temp = j+1
                    list[temp],list[i] = list[i],list[temp]
            
            
            
                return list
            
            if __name__ == "__main__":
            
                list = [1,23,32,9,2,3]
            
                print(selectionSort(list,True))

4. 设计一个函数实现字典根据key的值排序

        """
            @Author:sumu
            @Date:2020-01-01 10:47
            @Email:xvzhifeng@126.com
        
        """
        
        def directionSotedKey(dict,ascending = None):
        
        
            dict1 = {}
            if ascending == True:
                for i in sorted(dict,reverse=True) :
                    dict1[i] = dict[i]
            else:
                for i in sorted(dict):
                    dict1[i]=dict[i]
            #sorted(dict.items(),key=lambda x:x[0])
            return dict1
        
        
        
        if __name__ =="__main__":
        
            dict= {"dsf":1,"xzf":100,"sumu":60,"aa":500}
            print(directionSotedKey(dict,True))

5. 设计一个函数实现字典列表根据字典的某一个key排序
        
        """
            @Author:sumu
            @Date:2020-01-01 11:27
            @Email:xvzhifeng@126.com
        
        """
        
        if __name__ == "__main__":
        
            list =[
                {"name" : "wang", "age" : 10},
                {"name" : "xiaoming", "age" : 20},
                {"name" : "banzhang", "age" : 10}
            ]
        
            print(sorted(list,key=lambda x:x['name']))
            print(sorted(list,key=lambda x:x['age']))
            print(sorted(list,key=lambda x:x['age'],reverse=True))

6.下面这段代码的输出结果是什么？请解释。
        def add_to(num, target=[]):
            target.append(num)
            print(num, target)
        append()方法是在target列表中添加一个num

        
        add_to(3,[1])
        add_to(4)
        add_to(5)

    请问怎么修改才可以得到以下结果

            3,[1,3]
            4,[]
            5,[]
    #如下代码就能实现。
            def add_to(num, target=[]):
                if len(target) > 0:
                    target.append(num)
    
                print(num, target)

7.（选做题）设计一个程序实现搜索、根据最低工资排序和分页显示（每页显示15个岗位信息）。
