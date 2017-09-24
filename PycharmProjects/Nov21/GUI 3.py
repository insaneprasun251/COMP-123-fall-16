from tkinter import *


class ButtonGUI:
    def __init__(self):
        self.rootWin = Tk()
        self.rootWin.title("Button and Label GUI")

        self.contents = StringVar()
        self.contents.set("Welcome")

        self.label = Label(self.rootWin, textvariable=self.contents)
        self.label.grid(row=0, column=8)

        self.quitButton = Button(self.rootWin, text="Quit", command=self.quit)
        self.quitButton.grid(row=0, column=2)

        self.helloButton = Button(self.rootWin, text="Hello", command=self.hello)
        self.helloButton.grid(row=0, column=4)

        self.goodbyeButton = Button(self.rootWin, text="Goodbye", command=self.goodbye)
        self.goodbyeButton.grid(row=0, column=6)

    def go(self):
        self.rootWin.mainloop()

    def quit(self):
        self.rootWin.destroy()

    def hello(self):
        self.contents.set("Hello")

    def goodbye(self):
        self.contents.set("Goodbye")


myG = ButtonGUI()
myG.go()