"""
    @Author:sumu
    @Date:2020-01-03 20:25
    @Email:xvzhifeng@126.com

"""
import csv

from unit5.filefunc import *
from unit5.gainData import *
from unit5.dataRinse import *
from unit5.analyseData import *


def gain_csv_51job(filename,savename):
    dataPath = './data/'+filename
    savepath = './ransed_Data/'+savename

    t1,t2,t3,t4,t5,t6 = select_all(read_file(dataPath))
    write_cvs_file(savepath,'w',t1,t2,t3,t4,t5,t6)







if __name__ == '__main__':

    gain_csv_51job('51job_java.txt','51job_java.csv')

    # python2可以用file替代open
    #write_cvs_file(filePath,'w',t1,t2,t3,t4,t5,t6)


