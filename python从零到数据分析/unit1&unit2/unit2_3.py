"""
    Author:sumu
    data:2019-12-31

"""
from decimal import Decimal

if __name__ == "__main__":

    PI = 3.1415

    PI1 = round(PI,2)

    PI2 = Decimal(PI).quantize(Decimal("0.00"))
    print(PI1)

    print("%.2f"%PI)

    print(PI2)

