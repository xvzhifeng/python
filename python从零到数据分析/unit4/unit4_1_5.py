"""
    @Author:sumu
    @Date:2020-01-01 11:27
    @Email:xvzhifeng@126.com

"""

if __name__ == "__main__":

    list =[
        {"name" : "wang", "age" : 10},
        {"name" : "xiaoming", "age" : 20},
        {"name" : "banzhang", "age" : 10}
    ]

    print(sorted(list,key=lambda x:x['name']))
    print(sorted(list,key=lambda x:x['age']))
    print(sorted(list,key=lambda x:x['age'],reverse=True))
