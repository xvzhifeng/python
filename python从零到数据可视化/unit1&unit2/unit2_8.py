"""
    Author:sumu
    data:2019-12-31

"""



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