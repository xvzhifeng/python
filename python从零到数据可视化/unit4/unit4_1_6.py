"""
    @Author:sumu
    @Date:2020-01-01 11:34
    @Email:xvzhifeng@126.com

"""


def add_to(num, target=[]):
    if len(target) > 0:
        target.append(num)

    print(num, target)


if __name__ == "__main__":
    add_to(5)