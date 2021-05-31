from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

choix = Tk ()

choix.title ("Le meilleur jeu au monde")
choix.geometry ("1280x720")
choix.minsize (1280 ,720)
choix.maxsize (1280, 720)
choix.iconbitmap("logo.ico")
choix.config(background='red')

#---------Frame---------
frame1 = Frame(choix)
frame2 = Frame(choix)

titre = Label(choix, text="Chapitre 1", font=("Courrier.tff", 40), fg='#000000', relief="flat")
titre.pack()

#---------Question a poser---------
question = Label(frame1, text="Question :")
question.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, orient=VERTICAL)

nom = Text(frame1)
nom.config(height=5, width=50)
nom.focus_set()
nom.pack()

button = Button(frame1, text="Valider")
button.pack()


#---------Choix 1 et 2 a faire---------
question = Label(frame2, text="Choix 1 :")
question.pack()

nom1 = Entry(frame2, width=50)
nom1.focus_set()
nom1.pack()

button = Button(frame2, text="Valider")
button.pack()


question = Label(frame2, text="Choix 2 :")
question.pack()

nom2 = Entry(frame2, width=50)
nom2.focus_set()
nom2.pack()

button = Button(frame2, text="Valider")
button.pack()


#---------Mainloop---------
frame1.pack(side=LEFT)
frame2.pack()
choix.mainloop()