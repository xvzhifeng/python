



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