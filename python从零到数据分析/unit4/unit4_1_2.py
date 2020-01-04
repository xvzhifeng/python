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