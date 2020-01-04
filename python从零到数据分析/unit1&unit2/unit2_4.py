"""
    Author:sumu
    data:2019-12-31

"""


if __name__ == "__main__":

    s = "1.2.3.4.5"
    s1 = s.split(".")
    s1.sort(reverse=True)
    print("|".join(s1))
    s2 = "|".join(s.split("."))[::-1]
    print(s2)
    s3 = s.replace(".","|")[::-1]
    print(s3)