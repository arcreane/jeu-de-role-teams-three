from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

def Story2():

    def stop():
        editor2.destroy()

    editor2 = Tk()
    editor2.geometry("1280x720")
    editor2.minsize(1280, 720)
    editor2.maxsize(1280, 720)

    editor2.rowconfigure(0, weight=1)
    editor2.columnconfigure(0, weight=1)

    def showframe(frame):
        frame.tkraise()

    # Les Frames
    frame1 = Frame(editor2, bg='#98A4FF')
    frame2 = Frame(editor2, bg='#98A4FF')
    frame3 = Frame(editor2, bg='#98A4FF')
    frame4 = Frame(editor2, bg='#98A4FF')
    frame5 = Frame(editor2, bg='#98A4FF')
    frame6 = Frame(editor2, bg='#98A4FF')
    frame8 = Frame(editor2, bg='#98A4FF')
    frame11 = Frame(editor2, bg='#98A4FF')



    for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame8, frame11):
        frame.grid(row=0, column=0, sticky='nsew')


    # ----------------------------------------------------------------------------EDITOR 2----------------------------------------------------------------------------#


    # ----------------------------------------FRAME 1----------------------------------------#

    frame_1 = Frame(frame1, bg='#98A4FF')

    # Texte Crée perso
    label_subtitle = Label (frame_1, text="Crée ta propre Histoire", font=("Courrier.tff", 40), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)

    # --------------------Zone de text--------------------#
    etiquette = Label(frame_1, text='Nom du personnage :')
    etiquette.pack(padx=5, pady=5, side=TOP)

    def perso():
        nom = nom_perso.get()
        file = open("Histoire2/nom.txt", "a")
        file.write(f"{nom}#")
        file.close()

    nom_perso = StringVar()


    entree = Entry(frame_1, width=50, textvariable=nom_perso)
    entree.focus_force()
    entree.pack(padx=5, pady=5)

    # --------------------Boutton radio--------------------#
    etiquette = Label(frame_1, text='Homme ou Femme :')
    etiquette.pack(padx=5, pady=5)

    def genre():
        genre = genre_perso.get()
        file = open("Histoire2/genre.txt", "a")
        file.write(f"{genre}#")
        file.close()

    genre_perso = StringVar()

    br = Radiobutton(frame_1, text="Homme", value=1, font=("Courrier.tff", 20), variable=genre_perso)  # 1 pour Homme
    br2 = Radiobutton(frame_1, text="Femme", value=2, font=("Courrier.tff", 20), variable=genre_perso)  # 2 pour Femme
    br.pack()
    br2.pack()



    # Bouton Valider
    c = Button(frame_1, text="Valider", font=("Courrier.tff", 20), bg='#FFFFFF', fg='#000000', command=lambda:[perso(), genre(), showframe(frame11)])
    c.pack(pady=20, expand=YES)

    # Quitter
    c = Button(frame1, text="Menu Principal", font=("Courrier.tff", 12), bg='#FFFFFF', fg='#000000', command=stop)
    c.pack(side=BOTTOM)

    frame_1.pack(expand=YES)


    # ----------------------------------------FRAME 2----------------------------------------#

    frame_2 = Frame(frame2, bg='#98A4FF')

    # --------------------Question--------------------#
    frame_q = Frame(frame_2, bg='#98A4FF')

    question = Label(frame_q, text="Chapitre 1 :")
    question.pack()

    texteframe = Frame(frame_q)
    scroll = Scrollbar(texteframe)
    scroll.pack(side=RIGHT, fill=Y)

    def chap1():
        question1 = text.get("1.0", "end")
        choix1 = choix1_1.get()
        choix2 = choix1_2.get()
        file = open("Histoire2/chapitre1.txt", "a")
        file.write(f"{question1}#{choix1}#{choix2}#")
        file.close()

    text = Text(texteframe, width=50, height=10, yscrollcommand=scroll.set)
    text.focus_set()
    text.pack()
    scroll.config(command=text.yview)
    texteframe.pack()

    frame_q.pack()

    # --------------------Choix 1/2--------------------#

    # Choix 1
    frame_c = Frame(frame_2, bg='#98A4FF')

    question = Label(frame_c, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question.pack()

    choix1_1 = StringVar()

    nom1 = Entry(frame_c, width=50, textvariable=choix1_1)
    nom1.focus_set()
    nom1.pack()

    # Choix 2

    question = Label(frame_c, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question.pack()

    choix1_2 = StringVar()

    nom1 = Entry(frame_c, width=50, textvariable=choix1_2)
    nom1.focus_set()
    nom1.pack()

    frame_c.pack()

    button = Button(frame_2, text="Valider", font=("Courrier.tff", 15), command=lambda: [chap1(), showframe(frame3)])
    button.pack()

    # Quitter
    c = Button(frame2, text="Menu Principal", font=("Courrier.tff", 12), bg='#FFFFFF', fg='#000000', command=stop)
    c.pack(side=BOTTOM)

    frame_2.pack(expand=YES)

    # ----------------------------------------FRAME 3----------------------------------------#

    frame_3 = Frame(frame3, bg='#98A4FF')

    # --------------------Question--------------------#
    frame_q2 = Frame(frame_3, bg='#98A4FF')

    question_2 = Label(frame_q2, text="Chapitre 2 :")
    question_2.pack()

    texteframe2 = Frame(frame_q2)
    scroll = Scrollbar(texteframe2)
    scroll.pack(side=RIGHT, fill=Y)

    def chap2():
        question2 = text.get("1.0", "end")
        choix_3 = choix1_3.get()
        choix_4 = choix1_4.get()
        file = open("Histoire2/chapitre2.txt", "a")
        file.write(f"{question2}#{choix_3}#{choix_4}#")
        file.close()

    text2 = Text(texteframe2, width=50, height=10, yscrollcommand=scroll.set)
    text2.focus_set()
    text2.pack()
    scroll.config(command=text.yview)
    texteframe2.pack()

    frame_q2.pack()

    # --------------------Choix 1/2--------------------#

    # Choix 1
    frame_c2 = Frame(frame_3, bg='#98A4FF')

    question_3 = Label(frame_c2, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_3.pack()

    choix1_3 = StringVar()

    nom3 = Entry(frame_c2, width=50, textvariable=choix1_3)
    nom3.focus_set()
    nom3.pack()

    # Choix 2

    question_4 = Label(frame_c2, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_4.pack()

    choix1_4 = StringVar()

    nom4 = Entry(frame_c2, width=50, textvariable=choix1_4)
    nom4.focus_set()
    nom4.pack()

    frame_c2.pack()

    button = Button(frame_3, text="Valider", font=("Courrier.tff", 15), command=lambda: [chap2(), showframe(frame4)])
    button.pack()

    # Quitter
    c = Button(frame3, text="Menu Principal", font=("Courrier.tff", 12), bg='#FFFFFF', fg='#000000',
               command=stop)
    c.pack(side=BOTTOM)

    frame_3.pack(expand=YES)

    # ----------------------------------------FRAME 4----------------------------------------#

    frame_4 = Frame(frame4, bg='#98A4FF')

    # --------------------Question--------------------#
    frame_q3 = Frame(frame_4, bg='#98A4FF')

    question_3 = Label(frame_q3, text="Chapitre 3 :")
    question_3.pack()

    texteframe3 = Frame(frame_q3)
    scroll = Scrollbar(texteframe3)
    scroll.pack(side=RIGHT, fill=Y)

    def chap3():
        question3 = text.get("1.0", "end")
        choix_5 = choix1_5.get()
        choix_6 = choix1_6.get()
        file = open("Histoire2/chapitre3.txt", "a")
        file.write(f"{question3}#{choix_5}#{choix_6}#")
        file.close()

    text3 = Text(texteframe3, width=50, height=10, yscrollcommand=scroll.set)
    text3.focus_set()
    text3.pack()
    scroll.config(command=text.yview)
    texteframe3.pack()

    frame_q3.pack()

    # --------------------Choix 1/2--------------------#

    # Choix 1
    frame_c3 = Frame(frame_4, bg='#98A4FF')

    question_5 = Label(frame_c3, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_5.pack()

    choix1_5 = StringVar()

    nom5 = Entry(frame_c3, width=50, textvariable=choix1_5)
    nom5.focus_set()
    nom5.pack()

    # Choix 2

    question_6 = Label(frame_c3, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_6.pack()

    choix1_6 = StringVar()

    nom6 = Entry(frame_c3, width=50, textvariable=choix1_6)
    nom6.focus_set()
    nom6.pack()

    frame_c3.pack()

    button = Button(frame_4, text="Valider", font=("Courrier.tff", 15), command=lambda: [chap3(), showframe(frame5)])
    button.pack()

    # Quitter
    c = Button(frame4, text="Menu Principal", font=("Courrier.tff", 12), bg='#FFFFFF', fg='#000000', command=stop)
    c.pack(side=BOTTOM)

    frame_4.pack(expand=YES)

    # ----------------------------------------FRAME 5----------------------------------------#

    frame_5 = Frame(frame5, bg='#98A4FF')

    # --------------------Question--------------------#
    
    frame_q4 = Frame(frame_5, bg='#98A4FF')

    question_4 = Label(frame_q4, text="Chapitre 4 :")
    question_4.pack()

    texteframe4 = Frame(frame_q4)
    scroll = Scrollbar(texteframe4)
    scroll.pack(side=RIGHT, fill=Y)

    def chap4():
        question4 = text.get("1.0", "end")
        choix_7 = choix1_7.get()
        choix_8 = choix1_8.get()
        file = open("Histoire2/chapitre4.txt", "a")
        file.write(f"{question4}#{choix_7}#{choix_8}#")
        file.close()

    text4 = Text(texteframe4, width=50, height=10, yscrollcommand=scroll.set)
    text4.focus_set()
    text4.pack()
    scroll.config(command=text.yview)
    texteframe4.pack()

    frame_q4.pack()

    # --------------------Choix 1/2--------------------#

    # Choix 1
    frame_c4 = Frame(frame_5, bg='#98A4FF')

    question_7 = Label(frame_c4, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_7.pack()

    choix1_7 = StringVar()

    nom7 = Entry(frame_c4, width=50, textvariable=choix1_7)
    nom7.focus_set()
    nom7.pack()

    # Choix 2

    question_8 = Label(frame_c4, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_8.pack()

    choix1_8 = StringVar()

    nom8 = Entry(frame_c4, width=50, textvariable=choix1_8)
    nom8.focus_set()
    nom8.pack()

    frame_c4.pack()

    button = Button(frame_5, text="Valider", font=("Courrier.tff", 15), command=lambda: [chap4(), showframe(frame6)])
    button.pack()

    # Quitter
    c = Button(frame5, text="Menu Principal", font=("Courrier.tff", 12), bg='#FFFFFF', fg='#000000', command=stop)
    c.pack(side=BOTTOM)

    frame_5.pack(expand=YES)

    # ----------------------------------------FRAME 6----------------------------------------#

    frame_6 = Frame(frame6, bg='#98A4FF')

    # --------------------Question--------------------#
    frame_q5 = Frame(frame_6, bg='#98A4FF')

    question_5 = Label(frame_q5, text="Chapitre 5 :")
    question_5.pack()

    texteframe5 = Frame(frame_q5)
    scroll = Scrollbar(texteframe5)
    scroll.pack(side=RIGHT, fill=Y)

    def chap5():
        question5 = text.get("1.0", "end")
        choix_9 = choix1_9.get()
        choix_10 = choix1_10.get()
        file = open("Histoire2/chapitre5.txt", "a")
        file.write(f"{question5}#{choix_9}#{choix_10}#")
        file.close()

    text5 = Text(texteframe5, width=50, height=10, yscrollcommand=scroll.set)
    text5.focus_set()
    text5.pack()
    scroll.config(command=text.yview)
    texteframe5.pack()

    frame_q5.pack()

    # --------------------Choix 1/2--------------------#

    # Choix 1
    frame_c5 = Frame(frame_6, bg='#98A4FF')

    question_9 = Label(frame_c5, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_9.pack()

    choix1_9 = StringVar()

    nom9 = Entry(frame_c5, width=50, textvariable=choix1_9)
    nom9.focus_set()
    nom9.pack()

    # Choix 2

    question_10 = Label(frame_c5, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
    question_10.pack()

    choix1_10 = StringVar()

    nom10 = Entry(frame_c5, width=50, textvariable=choix1_10)
    nom10.focus_set()
    nom10.pack()

    frame_c5.pack()

    button = Button(frame_6, text="Valider", font=("Courrier.tff", 15), command=lambda: [chap5(), showframe(frame8)])
    button.pack()

    # Quitter
    c = Button(frame6, text="Menu Principal", font=("Courrier.tff", 12), bg='#FFFFFF', fg='#000000', command=stop)
    c.pack(side=BOTTOM)

    frame_6.pack(expand=YES)



    # ----------------------------------------FRAME 8----------------------------------------#

    frame_8 = Frame(frame8, bg='#98A4FF')

    # --------------------Fin--------------------#
    label_subtitle = Label(frame_8, text="Bravo, tu as fini ton Histoire !", font=("Courrier.tff", 40), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)
    label_subtitle = Label(frame_8, text="Es-tu prêt à la tester ?", font=("Courrier.tff", 40), fg='#000000', relief="flat")
    label_subtitle.pack(side=TOP)

    c = Button(frame_8, text="Menu Principal", font=("Courrier.tff", 20), bg='#FFFFFF', fg='#000000', command=stop)
    c.pack(pady=25)

    frame_8.pack(expand=YES)



    # ----------------------------------------FRAME 11----------------------------------------#

    frame_11 = Frame(frame11, bg='#98A4FF')

    # --------------------Message Mort--------------------#

    frame_m = Frame(frame_11, bg='#98A4FF')

    mort = Label(frame_m, text="Message :", font=("Arial.tff", 20), fg='#000000', relief="flat")
    mort.pack()
    mort2 = Label(frame_m, text="Cette case vous permet d'afficher un message si le joueur fait le mauvais choix.")
    mort2.pack()

    texteframe = Frame(frame_m)
    scroll = Scrollbar(texteframe)
    scroll.pack(side=RIGHT, fill=Y)

    def mess():
        messagemort = textm.get("1.0", "end")
        messagefin = textf.get("1.0", "end")
        file = open("Histoire2/message.txt", "w")
        file.write(f"{messagemort}#{messagefin}#")
        file.close()

    textm = Text(texteframe, width=50, height=10, yscrollcommand=scroll.set)
    textm.focus_set()
    textm.pack()
    scroll.config(command=textm.yview)
    texteframe.pack(padx=40)

    frame_m.pack(expand=YES, side=RIGHT)

    # --------------------Message Fin--------------------#

    frame_f = Frame(frame_11, bg='#98A4FF')

    mort = Label(frame_f, text="Message :", font=("Arial.tff", 20), fg='#000000', relief="flat")
    mort.pack()
    mort2 = Label(frame_f, text="Cette case vous permet d'afficher un message à la fin de la partie.")
    mort2.pack()

    texteframe = Frame(frame_f)
    scroll = Scrollbar(texteframe)
    scroll.pack(side=RIGHT, fill=Y)

    textf = Text(texteframe, width=50, height=10, yscrollcommand=scroll.set)
    textf.focus_set()
    textf.pack()
    scroll.config(command=textf.yview)
    texteframe.pack(padx=40)

    frame_f.pack(expand=YES, side=LEFT)

    button = Button(frame_11, text="Valider", font=("Courrier.tff", 15), command=lambda: [mess(), showframe(frame2)])
    button.pack(side=BOTTOM)

    # Quitter
    c = Button(frame11, text="Menu Principal", font=("Courrier.tff", 12), bg='#FFFFFF', fg='#000000', command=stop)
    c.pack(side=BOTTOM)

    frame_11.pack(expand=YES)

    # ----------------------------------------------------------------------------FIN EDITOR 2----------------------------------------------------------------------------#

    showframe(frame1)

    editor2.mainloop()