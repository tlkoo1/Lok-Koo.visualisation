from graphics import *
import random
#random.display.init()

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
#for line in datafile: print(line)

# Do some simple drawing
window = GraphWin("Visualisation", 600, 600)


i=0
for line in datafile:
    line = Line(Point(300,i*5),Point(300,i*5))
    line.setWidth(10)
    
    time.sleep(0.5)
    
    ball = Circle(Point(100,300), i)
    ball.setFill(color_rgb(i*5,i*5,i*5))
    
    ball1 = Circle(Point(100,400), i)
    ball1.setFill(color_rgb(i*5,i*5,i*5))
    
    ball2 = Circle(Point(100,500), i)
    ball2.setFill(color_rgb(i*5,i*5,i*5))
    
    box = Rectangle(Point(200,i*20),Point(i*20,200))
    box.setOutline(color_rgb(0,0,i*5))
   
    
    box1 = Rectangle(Point(600,i*20),Point(i*20,200))
    box1.setOutline(color_rgb(0,0,i*5))
    box.setFill(color_rgb(i*5,i*5,i*5))
    
    i+=1
    
    line.draw(window)
    ball.draw(window)
    ball1.draw(window)
    ball2.draw(window)
    box.draw(window)
    box1.draw(window)
    



#random.display.update(int)

#text = Text(Point(50,200),"hi")
#text.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()