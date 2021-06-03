from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *



def showframe(frame):
    frame.tkraise()

choix = Tk ()

choix.title ("Le meilleur jeu au monde")
choix.geometry ("1280x720")
choix.minsize (1280 ,720)
choix.maxsize (1280, 720)
choix.iconbitmap("logo.ico")
choix.config(background='#98A4FF')

#Les Frames

framechoix1 = Frame(choix, bg='#98A4FF')
framechoix2 = Frame(choix, bg='#98A4FF')
framechoix3 = Frame(choix, bg='#98A4FF')
framechoix4 = Frame(choix, bg='#98A4FF')
framechoix5 = Frame(choix, bg='#98A4FF')

for frame in (framechoix1,framechoix2,framechoix3):
    frame.grid(row=0, column=0, sticky='nsew')

#--------------------QUESTION--------------------#

frame_q =  Frame(framechoix1, bg='#98A4FF')

question = Label(frame_q, text="Question :")
question.pack()

texteframe = Frame(frame_q)
scroll = Scrollbar(texteframe)
scroll.pack(side=RIGHT, fill=Y)

text = Text(texteframe, width=40, height=5, yscrollcommand=scroll.set)
text.focus_set()
text.pack()
scroll.config(command=text.yview)
texteframe.pack()

button = Button(frame_q, text="Valider")
button.pack()

frame_q.pack()

#--------------------CHOIX 1/2--------------------#

#Choix 1
frame_c =  Frame(framechoix1, bg='#98A4FF')

question = Label(frame_c, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
question.pack()

nom1 = Entry(frame_c, width=40)
nom1.focus_set()
nom1.pack()

#Choix 2

question = Label(frame_c, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
question.pack()

nom1 = Entry(frame_c, width=40)
nom1.focus_set()
nom1.pack()

frame_c.pack()

button = Button(framechoix1, text="Valider", font=("Courrier.tff", 15))
button.pack()



showframe(framechoix1)

choix.mainloop()