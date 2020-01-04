

1. int("1.4"),int(1.4)输出结果？
	- int("1.4") 报错
	- int(1.4) 输出1
2. 单引号，双引号，三引号的区别
	>
	单引号和双引号没有什么区别，只是在双引号中使用单引号时不需要转义字符反之亦然，但是在单引号中使用单引号需要转移字符。
	三引号：可以使用多行，适合用于大段的形式。
	
3. 请用两种方法保留两位小数p=3.1415


		
		from decimal import Decimal

		if __name__ == "__main__":
	
	    	PI = 3.1415
	
	   		PI1 = round(PI,2)
	
	    	PI2 = Decimal(PI).quantize(Decimal("0.00"))
	    	print(PI1)
	    	print("%.2f"%PI)
	    	print(PI2)
4.使用python将字符串“1.2.3.4.5”转换为字符串“5|4|3|2|1”

            """
                Author:sumu
                data:2019-12-31
            
            """
            
            
            if __name__ == "__main__":
            
                s = "1.2.3.4.5"
                s1 = s.split(".")
                s1.sort(reverse=True)
                print("|".join(s1))
                s2 = "|".join(s.split("."))[::-1]
                print(s2)
                s3 = s.replace(".","|")[::-1]
                print(s3)

	
5. [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]

			import numpy as np

		if __name__ == "__main__":

   			a = [[1,2],[3,4],[5,6]]

    		s = [j for i in a for j in i]

    		print (s)

    		s1 = np.array(a).flatten().tolist()

    		print (s1)

6. x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果

		x.join(y)-> dabceabcf
		x.join(z)-> dabceabcf
	
7. 两个列表a=[1,5,7,9]和b=[2,2,6,8]合并为[1,2,2,5,6,7,8,9]

        """
            Author:sumu
            data:2019-12-31
        
        """
        
        
        if __name__=="__main__":
            a = [1, 5, 7, 9]
            b = [2, 2, 6, 8]
            c = list(set(a+b))
            print (c)


8. list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]（自己写算法）

        if __name__ == "__main__":
            list_ = [2, 3, 5, 4, 9, 6]
            list3 = list_[:]
            list1 = []
            while len(list_) > 0:
                a = min(list_)
                list1.append(a)
                list_.remove(a)
            print (list1)
        
            list2 = list(set(list3))
            print(list2)
	
	
9. python实现列表去重的方法[1,2,2,3,6,7,8,9]


		if __name__ == "__main__":

    		a = [1,2,2,3,6,7,8,9]

    		b = []

    		for i in a:
        		if i not in b:
            		b.append(i)
    		print(b)
    	c = list(set(a))
        print(c)

	

