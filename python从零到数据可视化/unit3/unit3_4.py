



if __name__ == "__main__":

    s = "i love good food"


    # 结果无序
    s2 = ''.join(list(set([i for i in s])))

    print(s2)
    # 结果有序

    dic = {}.fromkeys([i for i in s])
    print(dic)
    print(''.join(dic.keys()))