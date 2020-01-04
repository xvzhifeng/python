"""
    @Author:sumu
    @Date:2020-01-03 15:59
    @Email:xvzhifeng@126.com

"""
import random
import turtle

# a class for animating Spirographs
from spiro import Spiro

class SpiroAnimator:

    """
    SpiroAnimator 类让我们同时绘制随机的裸线，该类使用一个计时器，每次绘制曲线一段等。这种
    技术定期更新图像，并允许程序处理事件，比如按键，鼠标点击，等
    """
    def __init__(self,N):
        # set the timer value in milliseconds
        # 设置以毫秒为间隔的单位，将用于定时器
        self.deltaT =10
        # get the window dimensions
        #保存海龟画图的窗口大小
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # create the Spiro objects
        #创建一个spiros的列表用于存放一些Spiro对象
        self.spiros = []
        for i in range(N):
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters
            #由于Spiro的构造函数需要一个列表参数所以用python的*运算符将元祖转化为参数列表
            spiro = Spiro(*rparams) # 创建一个新的Spiro对象，将它添加到列表中
            self.spiros.append(spiro)
            # call timer
            turtle.ontimer(self.update,self.deltaT)

    # generate random parameters

    def genRandomParams(self):
        """
        随机产生一些曲线的参数
        :return:
        """
        # randint 随机产生指定范围的随机数，以及uniform()对对浮点数进行同样的操作。
        width,height = self.width, self.height
        # 将R设置为50到窗口边一半长度的随机整数
        R = random.randint(50,min(width,height)//2)
        # 将r设置在R的的10%-90%之间
        r = random.randint(10,9*R//10)
        # 将l设置成0.1~0.9之间的随机小数
        l = random.uniform(0.1,0.9)
        # 在屏幕中间随机选择x，y的坐标，选择屏幕上的随机一点作为螺旋线中心
        xc = random.randint(-width//2,width//2)
        yc = random.randint(-height//2,height//2)
        # 随机设定颜色
        col = (random.random(),
                random.random(),
               random.random())
        # 将所有的参数以元祖的方式进行返回
        return (xc,yc,col,R,r,l)

    # restart spiro drawing
    def restart(self):
        """
        它遍历所有的spiro对象，清除以前绘制的每条螺旋线，分配新的螺旋线，然后重新启动程序
        :return:
        """
        for spiro in self.spiros:
            # clear
            spiro.clear()
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro paramters
            spiro.setparams(*rparams)
            # restart drawing
            spiro.restart()


    def update(self):

        """
        用一个计数器ncomplete记录画的Spiro对象的数目
        :return:
        """
        # update all spiro
        nComplete = 0
        # 遍历Spiro对象列表
        for spiro in self.spiros:
            # update
            spiro.update()
            #count completed spiros
            if spiro.drawingComplete:
                nComplete += 1
        # restart if all spiros are complete
        if nComplete == len(self.spiros):
            self.restart()
        # call the timer
        turtle.ontimer(self.update(),self.deltaT)

    # toggle turtle cursor on and off
    def toggleTurtles(self):
        """
        用来隐藏或显示光标
        :return:
        """
        for spiro in self.spiros:
            if spiro.t.isvisble():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()
