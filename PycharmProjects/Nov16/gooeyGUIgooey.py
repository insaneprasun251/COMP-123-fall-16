from tkinter import *


class Addition:
    def __init__(self):

        self.root = Tk()

        aLabel = Label(self.root, text="A")
        aLabel.grid(row=0, column=0)

        bLabel = Label(self.root, text="B")
        bLabel.grid(row=1, column=0)

        abLabel = Label(self.root, text="A + B")
        abLabel.grid(row=2, column=0)

        self.resultLabel = Label(self.root, text=0)
        self.resultLabel.grid(row=2, column=1)

        self.aEntry = Entry(self.root)
        self.aEntry.grid(row=0, column=1)

        self.bEntry = Entry(self.root)
        self.bEntry.grid(row=1, column=1)

        self.goButton = Button(self.root, text="Go!", command=self.doAddition)
        self.goButton.grid(row=0, column=2)

        self.subtractButton = Button(self.root, text="Subtract", command=self.doSubtraction)
        self.subtractButton.grid(row=1, column=2)

        self.quitButton = Button(self.root, text="Quit", command=self.quit)
        self.quitButton.grid(row=2, column=2)

    def quit(self):
        self.root.destroy()

    def doAddition(self):
        aVal = self.aEntry.get()
        bVal = self.bEntry.get()

        aVal = int(aVal)
        bVal = int(bVal)

        abVal = aVal + bVal

        self.resultLabel.config(text=abVal)

    def doSubtraction(self):
        aVal = int(self.aEntry.get())
        bVal = int(self.bEntry.get())

        abVal = aVal - bVal

        self.resultLabel.config(text=abVal)

    def go(self):
        self.root.mainloop()

class Multiplier:
    def __init__(self):

        self.root = Tk()

        aLabel = Label(self.root, text="A")
        aLabel.grid(row=0, column=0)

        bLabel = Label(self.root, text="B")
        bLabel.grid(row=1, column=0)

        abLabel = Label(self.root, text="A * B")
        abLabel.grid(row=2, column=0)

        self.resultLabel = Label(self.root, text=0)
        self.resultLabel.grid(row=2, column=1)

        self.aEntry = Entry(self.root)
        self.aEntry.grid(row=0, column=1)

        self.bEntry = Entry(self.root)
        self.bEntry.grid(row=1, column=1)

        self.goButton = Button(self.root, text="multiply", command=self.doMultiply)
        self.goButton.grid(row=0, column=2)

        self.subtractButton = Button(self.root, text="divide", command=self.doDivide)
        self.subtractButton.grid(row=1, column=2)

        self.quitButton = Button(self.root, text="Quit", command=self.quit)
        self.quitButton.grid(row=2, column=2)


    def doMultiply(self):
        aVal = self.aEntry.get()
        bVal = self.bEntry.get()
        abVal = aVal * bVal
        self.resultLabel.config(text=abVal)


    def doDivide(self):
        aVal = self.aEntry.get()
        bVal = self.bEntry.get()
        abVal = aVal * bVal
        self.resultLabel.config(text=abVal)


    def quit(self):
        self.root.destroy()


    def go(self):
        self.root.mainloop()


addition = Addition()
multiplication = Multiplier()

addition.go()
multiplication.go()
