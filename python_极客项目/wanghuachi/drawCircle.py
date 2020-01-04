"""
    @Author:sumu
    @Date:2020-01-03 14:21
    @Email:xvzhifeng@126.com

"""

import math
import turtle

#draw the circle using tuitle

def drawCircleTurtle(x,y,r):
    """
    利用turtle画圆。

    :param x: 圆心的x坐标
    :param y: 圆心的y坐标
    :param r: 半径的长度
    :return:
    """
    turtle.shape('turtle')
    # move to the start of circle

    # up()函数是告诉python提笔，就是让笔离开虚拟的纸，这样移动海龟也不会画图。
    turtle.up()
    #定位，这里(x,y)也就是圆心所在的位置，(x+r,y)也就是圆弧所在的位置。
    turtle.setpos(x+r,y)
    #down()顾名思义就就知道，这里是让python放下笔。
    turtle.down()

    #draw the circle

    for i in range(0,365,5): # i从0到365，步长为五的循环。
        #变量i作为角度参数，将传入圆的参数方程

        #radians() 将角度转化为弧度值。
        a = math.radians(i)
        #让海龟在这些点之间移动以便画出圆，其实本质上画的是一个多变形但是由于每一条边足够短，所以就会看出来是一个圆
        turtle.setpos(x+r*math.cos(a),y+r*math.sin(a))

if __name__ == "__main__":

    for i in range(1,500,6):
        drawCircleTurtle(100,100,i)
    #mainloop()为了保持tkinter窗口打开，以便你欣赏到你的画。
    turtle.mainloop()