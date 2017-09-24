from tkinter import *

# In this question you will complete a tkinter interface.
# This interface is designed to help students understand
# even and odd numbers. The interface has one entery in
# which users will type an integer. (feel free to assume
# that the users will correctly type an integer, that is,
# it is OK for your code to crash if the user types
# something other than an integer into the entry). The
# interface also has a button and an output label. when
# the button is pressed the entry should be read and its
# value copied over to the output label, if the input
# number is even the output label's background should be
# green, if it is odd the output label should be odd. Your
# job is to complete this interface so that the button
# copies the value over and updates the color of the label.
# To make this problem easier the widget code is all
# provided, you may, however, want to modify it to add
# commands and/or stringvariables to allow you to complete
# your job. Note: this interface uses many labels to help
# instruct the user, most of these labels should be ignored.


class EvenOdd:
    def __init__(self):
        self.root = Tk()

        self.usertext = StringVar()
        self.usertext.set("")


        # labels
        self.intrLab1 = Label(self.root, text="1. type a number below.")
        self.intrLab1.grid(row=0, column=0)

        self.insrLab2 = Label(self.root, text="2. click this button.")
        self.insrLab2.grid(row=0, column=1)

        self.insrLab3 = Label(self.root, text="3. is the number even or odd?")
        self.insrLab3.grid(row=0, column=2)

        # buttons and labels for the actual interface
        # note - you may want to switch some of the text to textvariables
        self.inpt = Entry(self.root, textvariable=self.usertext)
        self.inpt.grid(row=1, column=0)

        self.btn = Button(self.root, text="Is It Even?", command=self.colors)
        self.btn.grid(row=1, column=1)

        # the background of this label should be green if the number
        # is even, odd otherwise.
        self.output = Label(self.root, textvariable=self.usertext, bg="green")
        self.output.grid(row=1, column=2)

    def colors(self):
        numstr = self.usertext.get()
        num = int(numstr)
        if num % 2 == 0:
            self.output.config(bg="green", text=num)
        else:
            self.output.config(bg="red", text=num)


    def go(self):
        self.root.mainloop()


eo = EvenOdd()
eo.go()
