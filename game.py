from tkinter import*
import tkinter as tk
from tkinter import messagebox
import random
import pygame


root=tk.Tk()
root.title("Typing Master")      
root.geometry("600x400+400-200")
root.configure(bg="#001D3D")
root.iconbitmap("typing.ico")
root.maxsize(600, 400)
root.minsize(600, 400)


words=['apple','pear','pair','mango','car','bike','cat','dog','horse','fan','air','blue','red','black','grey',
       'hair','sudden','karachi','for','today','that','yesterday','fork','door','color','floor','flour','grape',
       'duck','horn','crown','fish','fly','plain']

pygame.mixer.init()       #initializing the mixer for sound

def time():
    global timeleft,matched
    if(timeleft>0):
        timeleft-=1                   #it will run the time counter and -1 from its value after each sec
        timercount.configure(text=timeleft)     #it will display the change in counter value after each sec
        timercount.after(1000,time)          #1000ms = 1 sec
        if (timeleft<11):
            timercount.configure(fg="red")
            timer.configure(fg="red")
        if timeleft==10:
            pygame.mixer.music.load("countdown1.mp3")     #countdown sound
            pygame.mixer.music.play(loops=0)
    else:
        scorecount.configure(text=matched)                #change in score count and show after time is up
        scorelabel.configure(text="You enter\tWPM")
        if matched>=35 and matched<=40:
            feedback.configure(text="Your typing speed is average")            #feedback on last
        elif matched>=65:
            feedback.configure(text="Your typing speed is above average")
        else:
            feedback.configure(text="Your typing speed is below average")
            
        retry=messagebox.askretrycancel('Notification','Do you want to retry?')
        
        if retry==True:
            timeleft=60                                                    #RETRY BOX coding
            matched=0
            feedback.configure(text='')
            scorecount.configure(text='')
            scorelabel.configure(text='')
            timercount.configure(text=timeleft,fg="yellow")
            timer.configure(fg="yellow")
            wordentry.delete(0,END)



def startGame(event):

    global matched,not_matched

    if timeleft==60:        #it will call the func time
        time()
        
    if(wordentry.get() == word["text"]):
        matched+=1            #if you enter correct word then it will be count otherwise else loop will run
    elif(wordentry.get() != word["text"]):
        not_matched+=1
        pygame.mixer.music.load("buzzer1.mp3")     
        pygame.mixer.music.play(loops=0)           #it will play sound when you enter wrong word

    random.shuffle(words)              #it will shuffle words in a list
    word.configure(text=words[0])        #it will print those shuffled words one by one
    wordentry.delete(0,END)         #after user typed the word and pressed enter key then entry box will automatically cleared 
    label.configure(text="")         #After starting game instruction below entry will remove
         
    
h1=Label(root, text="Typing Master", bg="#001D3D", fg="#FFC300" ,font="comicsanms 24 bold", anchor="center")
h1.pack(pady=10)             #first heading

word=Label(root, text=words[0], font="comicsanms 20 bold", fg="#FFD60A", bg="#001D3D",width=15,anchor="center")
word.place(y=150,x=40)            #words that we have to enter

wordentry=Entry(root,font="comicsanms 18 bold",fg="grey",bg="#001D3D", justify="center",bd=4)
wordentry.place(x=40,y=200)#entry box where we will enter words


timer=Label(root, text="Timer:",fg="green", bg="#001D3D", font="comicsanms 18 bold")
timer.place(x=470, y=100)         #timer heading

timercount=Label(root, text="60",fg="green", bg="#001D3D", font="comicsanms 16 bold")
timercount.place(x=495, y=140)         #timer count below its heading

label=Label(root, text="Type word and Hit enter to start the game", bg="#001D3D", fg="grey", font="comicsanms 10 italic")
label.place(x=68,y=250) #instruction 1 for user below entry label at starting of game



matched=0             #variables used in this program
not_matched=0
timeleft=60

scorelabel=Label(root, text="", bg="#001D3D", fg="#FFC300", font="comicsanms 17 bold")
scorelabel.place(x=50,y=310)                   #text which will appear after time is up

scorecount=Label(root, text="", bg="#001D3D", fg="#FFC300", font="comicsanms 17 bold")
scorecount.place(x=190,y=310)                #number of wpm score which will in between the text of scorelabel

feedback=Label(root, text="",bg="#001D3D",fg="#FFC300",font="comicsanms 12 bold")
feedback.place(x=53,y=350)        #it will display the text which will tell your typing speed is average or not 



root.bind('<Return>', startGame)
root.mainloop()
