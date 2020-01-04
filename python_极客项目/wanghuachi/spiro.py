"""
    @Author:sumu
    @Date:2020-01-03 14:58
    @Email:xvzhifeng@126.com

"""
import math
import turtle
from math import gcd
import fractions


class Spiro:
    #construtor
    def __init__(self,xc,yc,col,R,r,l):

        #create the turtle object
        self.t = turtle.Turtle()
        # set the cursor shape
        self.t.shape('turtle')
        # set the step in degrees
        # 将参数绘图角度的增量设置为5度
        self.step = 5
        # set the drawing complete flag
        self.drawingComplete = False

        # set the parameters
        self.setparams(xc, yc,col,R,r,l)

        #initialize the drawing
        self.restart()

    # set the parameters

    def setparams(self,xc,yc,col,R,r,l):
        """
        :param xc: 曲线的中心的坐标x
        :param yc: 曲线中心的坐标y
        :param col: 线的颜色
        :param R: 圆的半径
        :param r: 圆的半径
        :param l:
        :return:
        """

        # the Spirograph parameters
        # xc,yc 为曲线中心的坐标，保存曲线中心的坐标
        self.xc = xc
        self.yc = yc
        # 将每个圆的半径(R和r)转化为整数并保存这些值
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        # reduce r/R to its smallest from by dividing with the GCD
        # 用python模块fractions内置的gcd()方法来计算半径的GCD，我们将用这些信息，来确定曲线的周期性
        gcdVal = gcd(self.r, self.R)
        # 将它保存为self.nRot
        self.nRot =self.r//gcdVal
        # get ratio of radii
        self.k = r/float(R)
        # set the color
        self.t.color(*col)
        #store the current angle
        # 保存当前的角度，我们将用他们来创建动画
        self.a = 0


    # restart the drawing
    def restart(self):

        # set the flag
        self.drawingComplete = False     #用于判断当前的图形是否画完
        # show the turtle
        self.t.showturtle()
        # go to the first point
        self.t.up() # 提笔

        # 通过一系列的局部变量，计算角度a设为0时的x和y坐标，以获取曲线的起点
        R,k,l = self.R,self.k,self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x,self.yc +y)
        # 定位完成后，下笔
        self.t.down()


    # draw the whole thing
    def draw(self):

        # draw the rest of the points
        R, k, l = self.R, self.k,self.l
        # 迭代遍历参数i的完整范围，它表示，是360乘以nRot
        for i in range(0,360*self.nRot+1,self.step):
            a = math.radians(i)

            # 计算i参数对应的x，y的值，也就是计算它的坐标
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc+x,self.yc +y)

        # drawing is now done so the hide the turtle cursor
        self.t.hideturtle()


    # update by one step

    def update(self):

        # skip the rest of the steps if done
        if self.drawingComplete:
            return
        # increment the angle
        # update() 增加当前的角度
        self.a += self.step

        # draw a step
        R, k, l = self.R, self.k, self.l
        # set the angle
        a = math.radians(self.a)
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc +y)
        # if drawing is complete, set the flag
        # 检查角度是否达到这条特定的曲线计算完整范围，如果是就设置drawingComplete标志和隐藏标志
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide the turtle curser
            self.t.hideturtle()

