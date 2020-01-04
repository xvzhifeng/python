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
