"""
    @Author:sumu
    @Date:2020-01-03 17:06
    @Email:xvzhifeng@126.com

"""


# save drawings as Png files
import argparse
from datetime import datetime
import turtle
import random
import turtle

# a class for animating Spirographs
from spiro import Spiro
from spiroAnimator import SpiroAnimator

from PIL import Image


def saveDrawing():
    # hide the turtle cursor
    turtle.hideturtle()
    # generate unique filenames
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = 'spiro-' + dateStr
    print('saving drawing to %s .eps/png' %fileName)
    # get the tkinter canvas
    canvas = turtle.getcanvas()
    #save the drawing as a postscipt image
    canvas.postscript(file = fileName+".eps")
    # use the pillow module to convert the postscript image file to PNG
    img = Image.open(fileName+'.eps')
    img.save(fileName+'.png','png')
    #show the turtle cursor
    turtle.showturtlr()

# main() function

def main():
    #use sys.argv if needing
    print("generating spirograph....")
    # create parser
    descStr = """this program draws Spirograph using the Turtle module.
    when run with no arguments, this program...
    
    """
    parser = argparse.ArgumentParser(description=descStr)

    # add expected arguments
    parser.add_argument('--sparams',nargs=3,dest='sparams',required=False,
                        help="The three arguments in sparams:R,r,l.")

    #parse args
    args = parser.parse_args()

    # set the cursor shape to turtle
    turtle.setup(width=0.8)

    # set the cursor shape to Spirographs!
    turtle.shape('turtle')

    # set the title to Spirographs!
    turtle.title("Spirographs!")

    # add the key hander to save our drawings
    turtle.onkey(saveDrawing,"s")

    #start listening
    turtle.listen()

    #hide the main turtle cursor
    turtle.hideturtle()

    # check for any arguments sent to -- sparams and draw the Spirograph
    if args.sparams:
        params = [float(x) for x in args.sparams]
        # draw the Spirograph with the given parameters
        col = (0.0, 0.0 , 0.0)
        spiro = Spiro(0,0,col,*params)
        spiro.draw()
    else:
        # create the animator abject
        spiroAnim = SpiroAnimator(4)
        # add a key handler to toggle the turtle cursor
        turtle.onkey(spiroAnim.toggleTurtles,'t')
        # add
        turtle.onkey(spiroAnim.restart,'space')
    #start the turtle main loop
    turtle.mainloop()

if __name__ == '__main__':
    main()


