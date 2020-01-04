"""
    @Author:sumu
    @Date:2020-01-01 10:47
    @Email:xvzhifeng@126.com

"""

def directionSotedKey(dict,ascending = None):


    dict1 = {}
    if ascending == True:
        for i in sorted(dict,reverse=True) :
            dict1[i] = dict[i]
    else:
        for i in sorted(dict):
            dict1[i]=dict[i]

    #sorted(dict.items(),key=lambda x:x[0])
    return dict1



if __name__ =="__main__":

    dict= {"dsf":1,"xzf":100,"sumu":60,"aa":500}
    print(directionSotedKey(dict,True))