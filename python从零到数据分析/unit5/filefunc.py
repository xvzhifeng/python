"""
    @Author:sumu
    @Date:2020-01-03 19:59
    @Email:xvzhifeng@126.com

"""
import csv


def read_file(filepath):
    """
    :param filepath: 文件的路径
    :return: 文件的内容
    """
    with open(filepath) as fp :
        content = fp.read()
    return content


def read_file_layout(filepath):
    """
    :param filepath: 文件的路径
    :return: 文件的内容
    """
    str = ""
    fp = open(filepath)
    content = fp.readlines()
    for c in content:
        str += c.replace('\n', '\n')
    fp.close()
    return str


def write_file(filepath,mode,content=str):
    """
    :param filepath: 文件的路劲
    :param mode: 打开的方式
    :param content: 写入的内容
    :return: 返回值
    """
    with open(filepath, mode) as rwf:
        rwf.write(content)
    return "successful"

def write_file(filepath,mode,content=list):
    """
    :param filepath: 文件的路劲
    :param mode: 打开的方式
    :param content: 写入的内容
    :return: 返回值
    """
    with open(filepath, mode) as rwf:
        for i in content:
            rwf.write(str(i)+'\n')
        #rwf.write(content)
    return "successful"


# stu1 = [lid, k, pre_count_data[k]]
# # 打开文件，写模式为追加'a'
# out = open('../results/write_file.csv', 'a', newline='')
# # 设定写入模式
# csv_write = csv.writer(out, dialect='excel')
# # 写入具体内容
# csv_write.writerow(stu1)

def write_cvs_file(filepath,mode,t1,t2,t3,t4,t5,t6):
    """
    功能：把51同城搜索只有网页的源码的数据清理之后的数据整理成表格的形式写入csv表中；进行存储，备份。
    :param filepath: 文件存放的路径
    :param mode: 写入方式例如；'w','a'等
    :param t1: 职位列表
    :param t2: 公司列表
    :param t3: 地区列表
    :param t4: 最小薪资列表
    :param t5: 最大薪资列表
    :param t6: 发布的日期
    :return:
    """
    f = open(filepath,mode,newline='', encoding='utf-8')
    # 2. 基于文件对象构建 csv写入对象
    print(len(t1),len(t2),len(t3),len(t4),len(t5),len(t6))
    csv_writer = csv.writer(f)
    for i in range(len(t1)):
        csv_writer.writerow([str(t1[i]),str(t2[i]),str(t3[i]),str(t4[i]),str(t5[i]),str(t6[i])])
    f.close()





