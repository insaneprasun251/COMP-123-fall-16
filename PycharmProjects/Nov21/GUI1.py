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

        self.quitButton = Button(self.root, text="Quit", command=self.quit)
        self.quitButton.grid(row=1, column=2)

    def doAddition(self):
        #get the value from entry A
        aVal = self.aEntry.get()
        aVal= int(aVal)
        #get the value from entry B
        bVal= self.bEntry.get()
        bVal = int(bVal)
        #add the values together
        abVal= aVal + bVal
        #write that value A+B out to the label
        self.resultLabel.config(text=abVal)

    def quit(self):
        self.root.destroy()

    def go(self):
        self.root.mainloop()


window = Addition()
window.go()