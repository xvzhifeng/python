"""
    Author:sumu
    data:2019-12-31

"""
if __name__ == "__main__":
    a = 1
    b = 3
    print(f"old a = {a} and b = {b}")
    c = a+b
    b = c-b
    a = c-b
    print(f"new a = {a} and b = {b}")