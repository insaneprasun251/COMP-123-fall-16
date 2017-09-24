
import random as rd
from tkinter import *

# ---------------------------------------
# Question 1


class RandomColorGUI:
    
    def __init__(self):
        """Sets up the GUI window, and all the widgets in it"""
        self.mainWindow = Tk()
        self.colorbutton = Button(self.mainWindow, text="Change Color")
        self.colorbutton.grid(row=0, column=0, padx=50, pady=30)
        self.colorbutton.config(command=self.setcolors)

        self.quitbutton = Button(self.mainWindow, text="Quit", command=quit)
        self.quitbutton.grid(row=1, column=0, pady=50)

    def go(self):
        """Sets the GUI in motion; uses the default event loop belonging to the main window."""
        self.mainWindow.mainloop()

    def makeColorString(self, redVal, greenVal, blueVal):
        """Takes in three integers between 0 and 255, and it returns the color string needed
        by tkinter to specify colors based on RGB values.  If the input values are not between
        0 and 255, then a message is printed and black is returned"""
        if (0 <= redVal <= 255) and (0 <= greenVal <= 255) and (0 <= blueVal <= 255):
            return "#%02x%02x%02x" % (redVal, greenVal, blueVal)
        else:
            print("Error: invalid value for a color string:", (redVal, greenVal, blueVal))
            return '#000000'

    def setcolors(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        col = self.makeColorString(r, g, b)
        self.mainWindow["bg"] = col
        
    def quit(self):
        self.mainWindow.destroy()
    
# End of class definition

# Define a function to trigger the GUI.  This allows more than one GUI to be given in the same
# files without them all launching.


def goRandomColor():
    """Sets up and runs the RandomColor GUI program."""
    rcg = RandomColorGUI()
    rcg.go()

# ---------------------------------------
# Question 2


class GuessingGameGUI:
    
    def __init__(self):
        """Sets up the GUI window, and all the widgets in it"""

        self.mainWindow = Tk()

        # set up a label as a local variable (doesn't need to be accessed)
        titleLabel = Label(self.mainWindow, text="Guess My Number",
                           font="Helvetica 20 bold", relief=RAISED,
                           justify=CENTER, bd=5)
        titleLabel.grid(row=0, columnspan=3, pady=20)

        self.greeting = "I am thinking of a number between 1 and 10. Try to guess it!"
        self.messageText = StringVar()
        self.messageText.set(self.greeting)
        messageBox = Label(self.mainWindow, textvariable=self.messageText,
                           font='Helvetica 16')
        messageBox.grid(row=1, column=1, columnspan=3, pady=20)
        
        entryLabel = Label(self.mainWindow, text="Enter guess here:", font='Helvetica 16')
        entryLabel.grid(row=2, column=1)
        
        self.userText = StringVar()
        userBox = Entry(self.mainWindow, textvariable=self.userText, font='Helvetica 16 bold')
        userBox.grid(row=2, column=2)
        userBox.bind("<Return>", self.respond)
        userBox.bind('<Tab>', self.respond)

        self.countText = StringVar()
        countLabel = Label(self.mainWindow, textvariable=self.countText, font='Helvetica 16')
        countLabel.grid(row=2, column=3)
        
        # set up a button as a local variable (doesn't need to be accessed)
        quitButton = Button(self.mainWindow, text="Quit",
                            font="Helvetica 16", command=self.quit)
        quitButton.grid(row=4, column=3, padx=20, pady=10)
   
        resetButton = Button(self.mainWindow, text="Reset Game",
                             font="Helvetica 16", command=self.resetGame)
        resetButton.grid(row=4, column=1, padx=20, pady=10)
        
        # choose number
        self.myNumber = rd.randint(1, 10)
        self.count = 0
        self.gameWon = False

        # self.resetGame()

    def go(self):
        """Sets the GUI in motion; uses the default event loop belonging to the main window."""
        self.mainWindow.mainloop()

    def quit(self):
        """Stops the program and closes the main window"""
        self.mainWindow.destroy()

    def resetGame(self):
        """This callback function for the Reset button resets the game to its initial state, 
        choosing a new random number and displaying the initial message again, and resetting the
        guess count to zero"""
        self.quit()
        self.__init__()



    def respond(self, event):
        """This callback method takes an event as input, but doesn't need to use it.  It
        responds to the user's input.  If the game is over, then nothing happens except that 
        the user's input disappears.  Otherwise it checks for good input, updates the guess count
        and displays an appropriate message."""
        if self.gameWon:
            self.userText.set("")
        else:
            self.count = self.count + 1
            self.countText.set("Guesses = " + str(self.count))
    
            guessStr = self.userText.get()
            self.userText.set("")
            
            if not guessStr.isnumeric():
                self.messageText.set("Enter only an integer between 1 and 10")
            else:
                guess = int(guessStr)
                if guess < 1 or guess > 10:
                    self.messageText.set("Enter only an integer between 1 and 10")
                elif guess == self.myNumber:
                    self.messageText.set("You guessed it!    Click Reset to play again.")
                    self.gameWon = True
                else:
                    self.messageText.set("That wasn't it.  Try again!")
        

# End of class definiton

# Define a function to trigger the GUI.  This allows more than one GUI to be given in the same
# files without them all launching.
def guessingGame():
    """Sets up and runs the GuessingGame GUI program."""
    game = GuessingGameGUI()
    game.go()


# ---------------------------------------
# Question 3

# Put your answer to question three here
# A function is called independently of an object, although an object may be passed to it. Methods are linked to objects
# and called with the dot syntax, making them inseparable from the classes and instances they operate in.
