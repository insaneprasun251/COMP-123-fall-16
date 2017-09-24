from tkinter import *
from PIL import Image, ImageTk

class CanvasExperiment:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.grid(row=0, column=0)
        self.circ = self.canvas.create_oval(100, 100, 300, 300, fill="blue")

    def go(self):
        self.root.mainloop()


# ce = CanvasExperiment()
# ce.go()

class Smiley:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.grid(row=0, column=0)
        self.circ = self.canvas.create_oval(10, 10, 390, 390, fill="yellow")
        self.lefteye = self.canvas.create_oval(200, 100, 250, 250, fill="black")
        self.righteye = self.canvas.create_oval(200, 200, 200, 200, fill="purple")
        self.smile = self.canvas.create_arc(20, 350, 350, 350, style="arc")

    def go(self):
        self.root.mainloop()

# smile = Smiley()
# smile.go()

class Photo:
    def __init__(self):
        self.image = Image.open("../Final Project/stan the stegosaurus.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.root = Tk()
        self.canvas = Canvas(self.root, width=640, height=481)
        self.canvas.grid(row=o, column=0)
        self.pic = Label(image=self.photo)

    def go(self):
        self.root.mainloop()

pic = Photo()
pic.go()
