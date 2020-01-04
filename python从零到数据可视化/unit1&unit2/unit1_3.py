"""
    Author:sumu
    data:2019-12-31

"""
if __name__ == "__main__":

    seconds = 12315
    m,s = divmod(seconds,60)
    h,m = divmod(m,60)
    print(f"{h}:{m}:{s}")