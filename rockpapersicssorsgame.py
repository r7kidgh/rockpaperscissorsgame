from tkinter import *
from tkinter import font
import random

gui = Tk()
gui.geometry("800x400")
gui.title("Rock Paper Scissors Game")
gui.config(background="gray94")
print(font.families())
plrscore = 0
compscore = 0

winner = " "

def game(player_choice):
    global plrscore, compscore, winner
    playerselected.config(text="Your Selection :  " + str(player_choice))
    option =["rock", "paper", "scissors"]
    computer_choice = random.choice(option)
    computerselected.config(text="Computer Selection : " + str(computer_choice))      
    if player_choice == "rock" and computer_choice == "scissors":
        plrscore= plrscore + 1
        compscore= compscore - 1
        winner = "You Win!"
        title2.config(text=winner)
    elif player_choice == "rock" and computer_choice == "paper":
        plrscore= plrscore - 1
        compscore= compscore + 1
        winner = "You Lost!"
        title2.config(text=winner)
    elif player_choice == "paper" and computer_choice == "rock":
        plrscore= plrscore + 1
        compscore= compscore - 1
        winner = "You Win!"
        title2.config(text=winner)
    elif player_choice == "paper" and computer_choice == "scissors":
        plrscore= plrscore - 1
        compscore= compscore + 1
        winner = "You Lost!"
        title2.config(text=winner)
    elif player_choice == "scissors" and computer_choice == "rock":
        plrscore= plrscore - 1
        compscore= compscore + 1
        winner = "You Lost!"
        title2.config(text=winner)
    elif player_choice == "scissors" and computer_choice == "paper":
        plrscore= plrscore + 1
        compscore= compscore - 1
        winner = "You Win!"
        title2.config(text=winner)
    elif player_choice == computer_choice:
        winner = "You Tied!"
        title2.config(text=winner)
    playerscore.config(text="Your Score: " + str(plrscore))
    computerscore.config(text="Computer Score: " + str(compscore))

title = Label(gui,text = "Rock Paper Scissors", bg = "gray94", fg = "gray54", font=("Arial",28))
title.place(x= 230, y=25)

title2 = Label(gui,text = "Lets Start The Game!", bg = "gray94", fg = "darkgreen", font=("Arial",18))
title2.place(x= 270, y=75)

title3 = Label(gui,text = "Score: ", bg = "gray94", fg = "gray54", font=("Arial",18))
title3.place(x= 100, y=230)

playerselected = Label(gui,text = "Your Selection : ", bg = "gray94", fg = "gray14", font=("Arial",16))
playerselected.place(x= 175, y=275)

playerscore = Label(gui,text = "Your Score : ", bg = "gray94", fg = "gray14", font=("Arial",16))
playerscore.place(x= 470, y=275)

computerselected = Label(gui,text = "Computer Selection : ", bg = "gray94", fg = "gray14", font=("Arial",16))
computerselected.place(x= 175, y=310)

computerscore = Label(gui,text = "Computer Score : ", bg = "gray94", fg = "gray14", font=("Arial",16))
computerscore.place(x= 470, y=310)

option = Label(gui,text = "Your Options : ", bg = "gray94", fg = "gray54", font=("Arial",16))
option.place(x= 100, y=135)

rock = Button(gui,highlightbackground="gray94",fg="gray0",text = "Rock",font=("Arial",18),width=10,command=lambda:game('rock'))
rock.place(x=165 ,y=170)

paper = Button(gui,highlightbackground="gray94",fg="gray0",text = "Paper",font=("Arial",18),width=10,command=lambda:game('paper'))
paper.place(x=350 ,y=170)

scissors = Button(gui,highlightbackground="gray94",fg="gray0",text = "Scissors",font=("Arial",18),width=10,command=lambda:game('scissors'))
scissors.place(x=535 ,y=170)

gui.mainloop()
