from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
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
    frame8 = Frame(jeu, bg='#98A4FF')

    for frame in (frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8):
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


    frame_1.pack(expand=YES)


    #----------------------------------------FRAME 2----------------------------------------#

    frame_2 =  Frame(frame2, bg='#98A4FF')

    #--------------------CHAPITRE 1--------------------#

    label_subtitle = Label (frame_2, text="Chapitre 1", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack (side=TOP)

    def chapitre1_1():
        lambda: showframe(frame3)

    def chapitre1_2():
        lambda: showframe(frame7)

    #------Question------#
    frameq = Frame(frame_2, bg='#98A4FF')

    file = open("Histoire1/chapitre1.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(frameq, text=texte2[0], font=("Courrier.tff", 20))
    label.pack(pady=10)

    frameq.pack(expand=YES)

    #------Choix1------#
    framec1 = Frame(frame_2, bg='#98A4FF')

    file = open("Histoire1/chapitre1.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(framec1, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(framec1, text="Choix 1", font=("Courrier.tff", 15), command=lambda:showframe(frame3))
    c.pack(ipadx=35)

    framec1.pack(expand=YES, side=LEFT, padx=20)

    #------Choix2------#
    framec2 = Frame(frame_2, bg='#98A4FF')

    file = open("Histoire1/chapitre1.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(framec2, text=texte2[2], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(framec2, text="Choix 2", font=("Courrier.tff", 15), command=lambda:showframe(frame7))
    c.pack( ipadx=35)

    framec2.pack(expand=YES, side=RIGHT, padx=20)


    frame_2.pack(expand=YES)



    # ----------------------------------------FRAME 3----------------------------------------#

    frame_3 = Frame(frame3, bg='#98A4FF')

    # --------------------CHAPITRE 2--------------------#

    label_subtitle = Label(frame_3, text="Chapitre 2", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)

    #Question:

    file = open("Histoire1/chapitre2.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(frame_3, text=texte2[0], font=("Courrier.tff", 20))
    label.pack(pady=10)

    #Choix1:

    file = open("Histoire1/chapitre2.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_3, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_3, text="Choix 1", font=("Courrier.tff", 15), command=lambda:showframe(frame4))
    c.pack(side=BOTTOM, ipadx=35)

    #Choix2:

    file = open("Histoire1/chapitre2.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_3, text=texte2[2], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_3, text="Choix 2", font=("Courrier.tff", 15), command=lambda:showframe(frame7))
    c.pack(side=BOTTOM, ipadx=35)

    frame_3.pack(expand=YES)



    # ----------------------------------------FRAME 4----------------------------------------#

    frame_4 = Frame(frame4, bg='#98A4FF')

    # --------------------CHAPITRE 2--------------------#

    label_subtitle = Label(frame_4, text="Chapitre 3", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)

    #Question:

    file = open("Histoire1/chapitre3.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(frame_4, text=texte2[0], font=("Courrier.tff", 20))
    label.pack(pady=10)

    #Choix1:

    file = open("Histoire1/chapitre3.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_4, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_4, text="Choix 1", font=("Courrier.tff", 15), command=lambda:showframe(frame5))
    c.pack(side=BOTTOM, ipadx=35)

    #Choix2:

    file = open("Histoire1/chapitre3.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_4, text=texte2[2], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_4, text="Choix 2", font=("Courrier.tff", 15), command=lambda:showframe(frame7))
    c.pack(side=BOTTOM, ipadx=35)

    frame_4.pack(expand=YES)



    # ----------------------------------------FRAME 5----------------------------------------#

    frame_5 = Frame(frame5, bg='#98A4FF')

    # --------------------CHAPITRE 2--------------------#

    label_subtitle = Label(frame_5, text="Chapitre 4", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)

    #Question:

    file = open("Histoire1/chapitre4.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(frame_5, text=texte2[0], font=("Courrier.tff", 20))
    label.pack(pady=10)

    #Choix1:

    file = open("Histoire1/chapitre4.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_5, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_5, text="Choix 1", font=("Courrier.tff", 15), command=lambda:showframe(frame6))
    c.pack(side=BOTTOM, ipadx=35)

    #Choix2:

    file = open("Histoire1/chapitre4.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_5, text=texte2[2], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_5, text="Choix 2", font=("Courrier.tff", 15), command=lambda:showframe(frame7))
    c.pack(side=BOTTOM, ipadx=35)

    frame_5.pack(expand=YES)


    # ----------------------------------------FRAME 6----------------------------------------#

    frame_6 = Frame(frame6, bg='#98A4FF')

    # --------------------CHAPITRE 2--------------------#

    label_subtitle = Label(frame_6, text="Chapitre 5", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)

    #Question:

    file = open("Histoire1/chapitre5.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(frame_6, text=texte2[0], font=("Courrier.tff", 20))
    label.pack(pady=10)

    #Choix1:

    file = open("Histoire1/chapitre5.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_6, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_6, text="Choix 1", font=("Courrier.tff", 15), command=lambda:showframe(frame8))
    c.pack(side=BOTTOM, ipadx=35)

    #Choix2:

    file = open("Histoire1/chapitre5.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_6, text=texte2[2], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_6, text="Choix 2", font=("Courrier.tff", 15), command=lambda:showframe(frame7))
    c.pack(side=BOTTOM, ipadx=35)

    frame_6.pack(expand=YES)



    #----------------------------------------FRAME 7----------------------------------------#

    frame_7 =  Frame(frame7, bg='#98A4FF')

    label_subtitle = Label (frame_7, text="Ce n'était pas le bon choix ...", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack (side=TOP)

    file = open("Histoire1/message.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_7, text=texte2[0], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_7, text="Quitter le jeu", font=("Courrier.tff", 15), command=alex.destroy)
    c.pack(side=BOTTOM, ipadx=35)

    frame_7.pack(expand=YES)


    #----------------------------------------FRAME 8----------------------------------------#

    frame_8 =  Frame(frame8, bg='#98A4FF')

    label_subtitle = Label (frame_8, text="Fin de jeu", font=("Courrier.tff", 30), fg='#000000', relief="flat")
    label_subtitle.pack (side=TOP, pady=20)

    file = open("Histoire1/message.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label1= Label(frame_8, text=texte2[1], font=("Courrier.tff", 20))
    label1.pack(pady=10)

    c = Button(frame_8, text="Quitter le jeu", font=("Courrier.tff", 15), command=alex.quitter)
    c.pack(side=BOTTOM, ipadx=35)

    frame_8.pack(expand=YES)


    showframe(frame1)


    jeu.mainloop()