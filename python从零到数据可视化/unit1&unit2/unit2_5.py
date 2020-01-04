"""
    Author:sumu
    data:2019-12-31

"""
import numpy as np

if __name__ == "__main__":

    a = [[1,2],[3,4],[5,6]]

    s = [j for i in a for j in i]

    print (s)


    s1 = np.array(a).flatten().tolist()

    print (s1)