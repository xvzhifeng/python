"""
    Author:sumu
    data:2019-12-31

"""

if __name__ == "__main__":

    a = [1,2,2,3,6,7,8,9]

    b = []

    for i in a:
        if i not in b:
            b.append(i)
    print(b)

    c = list(set(a))
    print(c)
