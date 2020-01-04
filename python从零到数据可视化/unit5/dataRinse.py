"""
    @Author:sumu
    @Date:2020-01-03 21:12
    @Email:xvzhifeng@126.com

"""
#< span class ="t1" > 职位名 < / span >
import re


def select_span(data):
    """
    :param data: 原始数据html，保存为txt形式
    :return:

    基本思想：就是提取出<span></span>中的数据，进行第一步的筛选
    """
    regex01 = re.compile(r'< *span class.{1,}span *>')
    return re.findall(regex01,data)

def select_titleoffice(data):
    regex = re.compile(r'title="(.+[\u4e00-\u9fa5]+[a-zA-Z ]*)"')
    return re.findall(regex,data)

def select_positionName_and_companyName(data):
    """
    直接从源文件中取出职位和公司名
    :param data:
    :return:
    """
    # target="_blank" title="
    regex = re.compile(r'target="_blank" title="(.*)"')

    data = re.findall(regex,data)
    data1 = []
    for i in data:
        data1.append(str(i).split('"')[0])
    return data1

def temp_place_salary_date(content):
    """
    :param content: 获取之后的列表转化为字符串，避免清洗不彻底的情况
    :return:
    """
    data = []
    for i in content :
        data.append(str(i))
    data1 = [str(i) for i in data]
    data = "\n".join(data1)
    #print(data)
    return str(data)

#--------------下面三个数据都是通过class样式的id获取，寻找规律获得----------
def select_place(data):
    """
    :param data:
    :return:
    """
    data = select_span(data)
    data = temp_place_salary_date(data)
    regex =re.compile(r'class="t3">(.+)<')
    return re.findall(regex,str(data))

def select_salary(data):
    """
    :param data:
    :return:
    """
    data = select_span(data)
    data = temp_place_salary_date(data)
    regex =re.compile(r'class="t4">(.*)<')
    return re.findall(regex,str(data))

def select_date(data):
    """
    :param data:
    :return:
    """
    data = select_span(data)
    data = temp_place_salary_date(data)
    regex =re.compile(r'class="t5">(.+)<')
    return re.findall(regex,str(data))

def split_positon_and_companyName(data):
    """
    :param data: position和companyName一起组成的列表
    :return: position列表和company列表
    功能：分解position和company组成的list，转化成各自的list
    """
    position = []
    company = []
    for i in range(len(data)):
        if i%2 == 0:
            position.append(data[i])
        else:
            company.append(data[i])
    return position,company


"""

1.5-2万/月
1-1.5万/月
0.5-1万/月
5-8千/月

regx = re.compile(r'(\d*.?\d*)-(\d*.?\d+)')
    regx1 = re.compile(r'([\u4e00-\u9fa5])/([\u4e00-\u9fa5])')
    number = re.findall(regx, s)
    per = re.findall(regx1,s)
    number = list(number[0])
    per = list(per[0])
    mymax=0
    mymin=0
    if '千' in per and '月' in per:
        #print('True')
        mymax=float(number[1])*1000
        mymin=float(number[0])*1000
    elif '万' in per and '月' in per:
        mymax = float(number[1])*10000
        mymin = float(number[0])*10000
    elif '万' in per and '年' in per:
        mymax = round(float(number[1])*10000/12,2)
        mymin = round(float(number[0])*10000/12,2)
    elif '元' in per and '天' in per:
        mymax = number[0]
        mymin = number[0]
    else:
        
"""
def transfermation_k(data):#提取最大最小值,单位:千每月
    """
    :param data: 处理好的工资列表
    :return: 最大薪资和最小薪资列表

    功能：把工资列表里的暑假进行进一步的分解，分成最大值和最小值的列表，其中的空值用当前数据的平均值代替
    """
    regx = re.compile(r'(\d*.?\d*)-(\d*.?\d+)')
    regx1 = re.compile(r'([\u4e00-\u9fa5])/([\u4e00-\u9fa5])')
    minSalary = ['最小工资']
    maxSalary = ['最大工资']
    count = 1
    sum = 0
    for s in data:
        number = re.findall(regx, s)
        per = re.findall(regx1, s)
        if len(number) == 0 and len(per) == 0:
            minSalary.append('')
            maxSalary.append('')
            continue
        number = list(number[0])
        per = list(per[0])

        if '千' in per and '月' in per :
            # print('True')
            mymax = float(number[1]) * 1000
            mymin = float(number[0]) * 1000
        elif '万' in per and '月' in per :
            mymax = float(number[1]) * 10000
            mymin = float(number[0]) * 10000
        elif '万' in per and '年' in per :
            mymax = round(float(number[1]) * 10000 / 12, 2)
            mymin = round(float(number[0]) * 10000 / 12, 2)
        elif '元' in per and '天' in per :
            mymax = float(number[0])
            mymin = float(number[0])
        else :
            mymin = 0
            mymax = 0
        count+=1
        sum +=(mymin+mymax)/2
        minSalary.append(mymin)
        maxSalary.append(mymax)
    avarage = round(sum/count,2)
    for i in range(len(minSalary)):
        if minSalary[i]=='':
            minSalary[i] = avarage
            maxSalary[i] = avarage
    minSalary.pop()
    maxSalary.pop()
    return minSalary,maxSalary

def select_all(data):
    """
    :param data: 原始51job搜索之后页面的html数据，另存为txt的格式
    :return: 清洗之后的数据，取出个列，职位，公司，地区，薪资，日期
    """
    positionAndcompany = select_positionName_and_companyName(data)
    posi,company =split_positon_and_companyName(positionAndcompany)
    place = select_place(data)
    salary = select_salary(data)
    date1 =select_date(data)
    posi.insert(0,'职位')
    company.insert(0,'公司')
    minsalary,maxsalary = transfermation_k(salary)

    print(maxsalary)
    print(minsalary)

    return posi,company,place,minsalary,maxsalary,date1

    # print(posi)
    # print(company)
    # print(place)
    # print(salary)
    # print(date1)
