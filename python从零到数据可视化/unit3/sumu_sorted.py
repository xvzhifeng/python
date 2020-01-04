"""
    @Author:sumu
    @Date:2020-01-02 16:17
    @Email:xvzhifeng@126.com

"""

def quick_sort(l,ascending=None):

    """
    :param l:列表
    :param ascending:是否是升序
    :return:列表

    默认从小到大，如果ascending参数为真，则从大到小

    基本思想：快速排序，选取中间值作为基准，然后根据这个基准，把它比他小的值放左边，比他大的值放右边，然后分类好之后，
    左边和右边的列表继续调用自身，一直到它们的长度小于2时，结束调用返回列表。
    """
    if len(l) >= 2:
        mid = l[len(l)//2]
        left,right = [],[]
        l.remove(mid)
        for i in l:
            if ascending:
                if i>mid:
                    left.append(i)
                else:
                    right.append(i)
            else:
                if i<mid:
                    left.append(i)
                else:
                    right.append(i)
        return quick_sort(left,ascending) + [mid] + quick_sort(right,ascending)
    else:
        return l



def Merge_sort(l,ascending=None):
    """
    :param l: 列表
    :param ascending: 是否是升序
    :return: 列表

    基本思想：把一个列表从中间分开，一直到列表中只剩下两个元素，然后在调用合并算法
    """
    if len(l)<=1:
        return l
    mid = len(l)//2
    left = Merge_sort(l[mid:],ascending)
    right = Merge_sort(l[:mid],ascending)
    return Merge(left,right,ascending)

def Merge(left,right,ascending=None):
    """

    :param left: 列表
    :param right: 列表
    :param ascending: 是否是升序
    :return: 合并之后的列表

    基本思想：依次比较两个列表的值的大小，把小的放入结果列表之中，直到一个列表为空时，结束循环，
    在最终列表的后面添加上剩下的元素
    """

    l,r = 0,0
    result = []

    while l<len(left) and r<len(right):
        if ascending:
            if left[l] < right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
        else:
            if left[l] < right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
    result +=left[l:]
    result +=right[r:]
    return result

