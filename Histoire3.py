from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os
import alex



def play():

    def showframe(frame):
        frame.tkraise()

    jeu = Tk()
    jeu.geometry ("1280x720")
    jeu.minsize (1280, 720)
    jeu.maxsize (1280, 720)
    jeu.rowconfigure(0, weight=1)
    jeu.columnconfigure(0, weight=1)



    def showframe(frame):
        frame.tkraise()

    #Les Frames

    frame1 = Frame(jeu, bg='#98A4FF')
    frame2 = Frame(jeu, bg='#98A4FF')
    frame3 = Frame(jeu, bg='#98A4FF')
    frame4 = Frame(jeu, bg='#98A4FF')
    frame5 = Frame(jeu, bg='#98A4FF')
    frame6 = Frame(jeu, bg='#98A4FF')
    frame7 = Frame(jeu, bg='#98A4FF')

    for frame in (frame1,frame2,frame3,frame4,frame5,frame6,frame7):
        frame.grid(row=0, column=0, sticky='nsew')




    #----------------------------------------FRAME 1----------------------------------------#

    frame_1 =  Frame(frame1, bg='#98A4FF')

    label_subtitle = Label (frame_1, text="Bonjour :", font=("Courrier.tff", 20), fg='#000000', relief="flat")
    label_subtitle.pack (side=TOP)


    file = open("Histoire1/nom.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(frame_1, text=texte2[0], font=("Courrier.tff", 20))
    #remplace le 0 par 1 ou 2 pour avoir les mots apres les #
    label.pack()

    label_subtitle = Label (frame_1, text="Es-tu pret a vivre cette aventure ?", font=("Courrier.tff", 20), fg='#000000', relief="flat")
    label_subtitle.pack (pady=10, side=TOP)

    label_subtitle = Label (frame_1, text="(Ps: N'oublie pas que tu peux perir a chaque instant !)", font=("Courrier.tff", 15), fg='#000000', relief="flat")
    label_subtitle.pack (pady=10, side=TOP)

    #Bouton Valider
    c = Button(frame_1, text="Prêt", font=("Courrier.tff", 30), bg='#FFFFFF', fg='#000000', command=lambda:showframe(frame2))
    c.pack ()

    #Bouton Supprimer Histoire
    c = Button(frame1, text="Supprimer l'Histoire", font=("Courrier.tff", 10), bg='#FFFFFF', fg='#000000', command=alex.effacer1)
    c.pack (side=BOTTOM)


    frame_1.pack(expand=YES)


    #----------------------------------------FRAME 2----------------------------------------#

    frame_2 =  Frame(frame2, bg='#98A4FF')

    #--------------------CHAPITRE 1--------------------#

    label_subtitle = Label (frame_2, text="Chapitre 1", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack (side=TOP)

    #Question:

    file = open("Histoire1/chapitre1.txt", "r")
    text1 = file.read()
    texte2 = text1.split("##")
    label= Label(frame_2, text=texte2[0], font=("Courrier.tff", 20))
    label.pack(pady=10)

    #Choix1:

    file = open("Histoire1/chapitre1.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_2, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_2, text="Choix 1", font=("Courrier.tff", 15), command=lambda:showframe(frame3))
    c.pack(side=BOTTOM, ipadx=35)

    #Choix2:

    file = open("Histoire1/chapitre1.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_2, text=texte2[2], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_2, text="Choix 2", font=("Courrier.tff", 15), command=lambda:showframe(frame7))
    c.pack(side=BOTTOM, ipadx=35)

    frame_2.pack(expand=YES)



    # ----------------------------------------FRAME 3----------------------------------------#

    frame_3 = Frame(frame3, bg='#98A4FF')

    # --------------------CHAPITRE 2--------------------#

    label_subtitle = Label(frame_3, text="Chapitre 2", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)

    # Question:

    file = open("Histoire1/chapitre2.txt", "r")
    text1 = file.read()
    texte2 = text1.split("##")
    label = Label(frame_3, text=texte2[0], font=("Courrier.tff", 20))
    label.pack()

    # Choix1:

    file = open("Histoire1/chapitre2.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1 = Label(frame_3, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_3, text="Choix 1", font=("Courrier.tff", 15), command=lambda: showframe(frame3))
    c.pack(side=BOTTOM, ipadx=35)

    # Choix2:

    file = open("Histoire1/chapitre2.txt", "r")
    text3 = file.read()
    texte4 = text3.split("#")
    label2 = Label(frame_3, text=texte4[2], font=("Courrier.tff", 20))
    label2.pack(pady=10)

    c = Button(frame_3, text="Choix 2", font=("Courrier.tff", 15), command=lambda: showframe(frame7))
    c.pack(side=BOTTOM, ipadx=35)

    frame_2.pack(expand=YES)




    #----------------------------------------FRAME 7----------------------------------------#

    frame_7 =  Frame(frame7, bg='#98A4FF')

    label_subtitle = Label (frame_7, text="Ce n'était pas le bon choix ...", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack (side=TOP)

    frame_7.pack(expand=YES)


    showframe(frame1)


    jeu.mainloop()