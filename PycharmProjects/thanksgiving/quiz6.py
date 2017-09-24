# Richard Graham: Quiz 6

from tkinter import *

# Question 1:
#
# A method is a function defined within a class that operates on a specific
# instance of an object, and called for that specific instance. A function is defined independently of a class and can
# be given any instance of an object to operate on--or no object at all.

# Question 2:


class SmallCounter:
    """Objects of this class track the smallest number assigned to them either on construction
    or through calls to the addValue method. getSmallest returns the tracked value."""
    def __init__(self, startvalue):
        self.small = startvalue

    def addValue(self, newvalue):
        if newvalue < self.small:
            self.small = newvalue

    def getSmallest(self):
        return self.small

# Question 3:


class RangeFinder:
    """This class is identical to SmallCounter, except that objects track through both the largest
    and smallest values assigned to them, and can return both"""
    def __init__(self, startvalue):
        self.small = startvalue
        self.big = startvalue

    def addValue(self, newvalue):
        if newvalue < self.small:
            self.small = newvalue
        elif newvalue > self.big:
            self.big = newvalue

    def getSmallest(self):
        return self.small

    def getLargest(self):
        return self.big


def smallcountertests():
    sc1 = SmallCounter(3)  # 3 is the "initial" smallest number sc1.addValue(7)
    sc1.addValue(100)
    sc1.addValue(2)
    sc1.addValue(23)
    sc1.addValue(-10)
    sc1.addValue(10)
    sc1.addValue(2)
    print(sc1.getSmallest())  # prints -10

    sc2 = SmallCounter(-30)  # 30 is the "initial" smallest number sc2.addValue(7)
    sc2.addValue(100)
    sc2.addValue(2)
    sc2.addValue(23)
    sc2.addValue(-10)
    sc2.addValue(10)
    sc2.addValue(2)
    print(sc2.getSmallest())  # prints -30

    sc2.addValue(-100)
    print(sc2.getSmallest())  # prints -100
    sc3 = SmallCounter("z")
    sc3.addValue("c")
    sc3.addValue("r")
    print(sc3.getSmallest())  # prints c


def rangefindertests():
    rf = RangeFinder(3)  # 3 is the "initial" smallest/largest number
    print(rf.getSmallest())  # prints 3
    print(rf.getLargest())  # prints 3

    rf.addValue(7)
    print(rf.getSmallest())  # prints 3
    print(rf.getLargest())  # prints 7

    rf.addValue(1)
    print(rf.getSmallest())  # prints 1
    print(rf.getLargest())  # prints 7

    rf.addValue(100)
    rf.addValue(2)
    rf.addValue(23)
    rf.addValue(-10)
    rf.addValue(10)
    rf.addValue(2)
    print(rf.getSmallest())  # prints -10
    print(rf.getLargest())  # prints 100

smallcountertests()
rangefindertests()

# Question 4:

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Quiz 6")
        self.textlabel = Label(self.root, text="Enter Text Below")
        self.textlabel.grid(row=0, column=0)

        self.entry = Entry(self.root)
        self.entry.grid(row=1, column=0)

        self.updatebutton = Button(self.root, text="Change text", command=self.changetext)
        self.updatebutton.grid(row=1, column=2)

        self.redbutton = Button(self.root, text="Red", command=self.bgred)
        self.redbutton.grid(row=2, column=0)

        self.orangebutton = Button(self.root, text="Orange", command=self.bgorange)
        self.orangebutton.grid(row=2, column=1)

        self.yellowbutton = Button(self.root, text="Yellow", command=self.bgyellow)
        self.yellowbutton.grid(row=2, column=2)

        self.greenbutton = Button(self.root, text="Green", command=self.bggreen)
        self.greenbutton.grid(row=3, column=0)

        self.bluebutton = Button(self.root, text="Blue", command=self.bgblue)
        self.bluebutton.grid(row=3, column=1)

        self.purplebutton = Button(self.root, text="Purple", command=self.bgpurple)
        self.purplebutton.grid(row=3, column=2)

    def bgred(self):
        self.textlabel.config(bg="red")

    def bgorange(self):
        self.textlabel.config(bg="orange")

    def bgyellow(self):
        self.textlabel.config(bg="yellow")

    def bggreen(self):
        self.textlabel.config(bg="green")

    def bgblue(self):
        self.textlabel.config(bg="blue")

    def bgpurple(self):
        self.textlabel.config(bg="purple")

    def changetext(self):
        newtext = self.entry.get()
        self.textlabel.config(text=newtext)

    def go(self):
        self.root.mainloop()

win = Window()
win.go()
