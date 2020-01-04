

if __name__ == "__main__":

    a = "i love good food"
    s = "i love good food"

    print(a.title())

    s = ' '.join([ch[0].upper() + ch[1 :] for ch in s.split(' ')])

    print (s)