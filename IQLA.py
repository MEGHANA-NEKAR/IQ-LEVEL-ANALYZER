# import the modules
from tkinter import *
import random
import pyttsx3
import tkinter.font as font


# list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# the game time left, initially 30 seconds.
timeleft = 30

randomvariable=10
speaker=pyttsx3.init()

# function that will start the game.
def startGame(event):
        if timeleft == 30:
        # start the countdown timer.
             countdown()

        # run the function to
        # choose the next colour.
        nextColour(5)


# Function to choose and
# display the next colour.
def nextColour(value):
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft
    global randomvariable

    # if a game is currently in play
    if timeleft > 0:


        # make the text entry box active.
        e.focus_set()

        if difficultmode == True and e.get().lower() == colours[0].lower():
            score += 1
            # clear the text entry box.
        e.delete(0, END)

        print("randomvariable**First", randomvariable)
        print("label.cget('fg')",label.cget('fg').lower())

        if easymode == True and randomvariable!=10:
            print("randomvariable**color", colours[randomvariable].lower())
            if str(colours[randomvariable]).lower() == label.cget('fg').lower() and value==1:
                score += 1
            if str(colours[randomvariable]).lower() != label.cget('fg').lower() and value==0:
                score += 1
            if str(colours[randomvariable]).lower() == label.cget('fg').lower() and value==0:
                score -= 1
            if str(colours[randomvariable]).lower() != label.cget('fg').lower() and value==1:
                score -= 1

        random.shuffle(colours)

        randomvariable = random.randint(0, 1)
        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        print("randomvariable***", randomvariable)
        label.config(fg=str(colours[0]), text=str(colours[randomvariable+3]))
        if easymode == True:
            colorlabel.config(fg=str(colours[randomvariable+2]), text=str(colours[randomvariable]))


        # update the score.
        scoreLabel.config(text="Score: " + str(score))
    else:
        print("score*****",score)
        if score>=30:
            IQLevellabel.config(text="You are highly advanced!!!")
            speaker.say("You are highly advanced!!!")
            speaker.runAndWait()
        elif score>=25 and score<30:
            IQLevellabel.config(text="You are superior!!")
            speaker.say("You are superior!!")
            speaker.runAndWait()
        elif score>=20 and score<25:
            IQLevellabel.config(text="You are above average")
            speaker.say("You are above average")
            speaker.runAndWait()
        elif score >= 11 and score < 20:
            IQLevellabel.config(text="You are average!!")
            speaker.say("You are average")
            speaker.runAndWait()
        elif score >= 10 and score < 11:
            IQLevellabel.config(text="You are below average")
            speaker.say("You are below average")
            speaker.runAndWait()
        elif score >= 5 and score < 10:
            IQLevellabel.config(text="You are Well below average")
            speaker.say("You are Well below average")
            speaker.runAndWait()
        else:
            IQLevellabel.config(text="Bad Score, Lower extreme")
            speaker.say("Bad Score, Lower extreme")
            speaker.runAndWait()
    # Countdown timer function


def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: "
                             + str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)

    # Driver Code


# create a GUI window
root = Tk()

# set the title
root.title("IQ Level Analyzer")

# set the size
root.geometry("600x600")

var= IntVar()

yesValue= IntVar()


def sel():
    global easymode
    global difficultmode

    selectionq.config(text="You selected the option " + str(var.get()))
    selectionq.pack()

    if var.get()==2:
        easymode=False
        difficultmode=True
        instructions.config(text="Type in the colour of the words, and not the word text!")
        instructions.pack()

        scoreLabel.config(text="Press enter to start")
        scoreLabel.pack()

        timeLabel.config(text="Time left: "
                              + str(timeleft))
        timeLabel.pack()

        label1.pack()
        label2.pack()
        e.pack()
        root.bind('<Return>', startGame)


        # set focus on the entry box
        e.focus_set()
        #abortButton.pack()
        #restartButton.pack()

        # add a label for displaying the IQ Level
        IQLevellabel.pack(padx=20, pady=20)
        root.mainloop()
    else:
        easymode = True
        difficultmode = False
        instructions.config(text="Press Yes If colour of the words are same as word text Otherwise Press No!")
        instructions.pack()

        scoreLabel.config(text="Press enter to start")
        scoreLabel.pack()

        timeLabel.config(text="Time left: "
                              + str(timeleft))
        timeLabel.pack()

        root.bind('<Return>', startGame)
        label.pack()
        colorlabel.pack()

        yesButton.pack(ipady = 5)
        noButton.pack(ipady = 5)
        #abortButton.pack()
        #restartButton.pack()

        # add a label for displaying the IQ Level
        IQLevellabel.pack(padx=20, pady=20)
        root.mainloop()

radbuttonFont = font.Font(family='Helvetica', size=10, weight='bold')
Label(root,
        text="""Select Difficulty Level:""",width='20',bd='5',fg='blue',bg='light green',font=('Helvetica', 30)).pack()
selectionq= Label(root,width='20',bd='5',fg='blue',bg='light blue')
Radiobutton(root,
               text="Easy",
                bd = '4',
               variable=var,
               value=1,command=sel,font=radbuttonFont).pack()

Radiobutton(root,
               text="Difficult",
                bd = '5',
               variable=var,
               value=2,command=sel,font=radbuttonFont).pack()

# add an instructions label
instructions = Label(root, font=('Helvetica', 12))
# add a score label
scoreLabel = Label(root, font=('Helvetica', 12))
# add a time left label
timeLabel = Label(root, font=('Helvetica', 12))
# add a label for displaying the colours
label = Label(root, font=('Helvetica', 60))
#label2 = Label(root, font=('Helvetica', 60))
colorlabel = Label(root, font=('Helvetica', 60))

# add a text entry box for
        # typing in colours
e = Entry(root)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

yesButton = Button(root, text = 'Yes !', bd = '5',width='20',fg='Blue',bg='light blue',font=buttonFont,command = lambda :nextColour(1))
noButton = Button(root, text = 'No !', bd = '5',width='20',fg='purple',bg='pink',font=buttonFont,command = lambda :nextColour(0))

IQLevellabel = Label(root, font=('Helvetica', 20))

# start the GUI
root.mainloop()









