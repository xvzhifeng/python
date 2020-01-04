"""
    Author:sumu
    data:2019-12-31

"""
import  math

def sushu(a):
    j = 2
    while j<=math.sqrt(a):
        if a%j == 0:
            return 0
        j+=1
    return 1

if __name__ =="__main__":

    i = 2
    while i<= 1000:
        # print(i)
        if sushu(i) == 1:
            print (i)
        i += 1
