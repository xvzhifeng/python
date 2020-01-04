"""
    Author:sumu
    data:2019-12-31

"""
if __name__ == "__main__":


    for i in range(100,1000):
        a = int(i/100)
        b = i%10
        c = int((i%100-b)/10)
        # print (f"{a},{b},{c}")
        if (a**3+b**3+c**3) == i:
            print(i)