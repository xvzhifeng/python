

if __name__ == "__main__":
    dict = {"name" : "zs", "age" : 18, "city" : "深圳", "tel" : "1362626627"}

    dict1 = sorted(dict.items(),key = lambda x:x[0])
    print (dict1)
    
