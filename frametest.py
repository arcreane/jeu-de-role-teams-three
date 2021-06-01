from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import alex


projet = Tk()
projet.geometry ("1280x720")
projet.minsize (1280, 720)
projet.maxsize (1280, 720)

bg = PhotoImage(file="fond.png")
label1 = Label(projet, image=bg)
label1.place(x=-2, y=-2)

projet.rowconfigure(0, weight=1)
projet.columnconfigure(0, weight=1)


#----------------------------------------MENU HAUT----------------------------------------#

menu = Menu(projet)

#Menu1
menu1 = Menu(menu, tearoff=0)
menu1.add_command(label="Ouvrir", command=alex.fichiers)
menu1.add_command(label="Enregistrer Sous", command=alex.alert)
menu1.add_command(label="Modifier", command=alex.alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=alex.quitter)

menu.add_cascade(label="Fichier", menu=menu1)

# Menu édition de blocs
menuedit = Menu(menu, tearoff=0)
menuedit.add_command(label="Ajouter un choix", command=alex.alert)
menuedit.add_command(label="Supprimer un choix", command=alex.alert)

#Menu2.1
menu4 = Menu(menu, tearoff=0)
menu4.add_command(label="Général", command=alex.alert)
menu4.add_separator()
menu4.add_command(label="Interface", command=alex.fichiers)
menu4.add_command(label="Performances", command=alex.alert)
menu4.add_command(label="Disques de Travail", command=alex.alert)

#Menu2
menu2 = Menu(menu, tearoff=0)
menu2.add_command(label="Ajouter un bloc", command=alex.alert)
menu2.add_cascade(label="Editer un bloc", menu=menuedit)
menu2.add_command(label="Supprimer un bloc", command=alex.alert)
menu2.add_separator()
menu2.add_command(label="Rechercher", command=alex.alert)
menu2.add_cascade(label="Préferences", menu=menu4)
menu2.add_command(label="Formes", command=alex.alert)
menu.add_cascade(label="Edition", menu=menu2)

#Menu3
menu3 = Menu(menu, tearoff=0)
menu3.add_command(label="Nous Contacter", command=alex.alert)
menu3.add_separator()
menu3.add_command(label="A propos", command=alex.alert)

menu.add_cascade(label="Aide", menu=menu3)

projet.config(menu=menu)

#Les Frames

frame1 = Frame(projet, bg='#98A4FF')
frame2 = Frame(projet, bg='#98A4FF')
frame3 = Frame(projet, bg='#98A4FF')
frame4 = Frame(projet, bg='#98A4FF')
frame5 = Frame(projet, bg='#98A4FF')
frame6 = Frame(projet, bg='#98A4FF')
frame7 = Frame(projet, bg='#98A4FF')

for frame in (frame1,frame2,frame3,frame4,frame5,frame6,frame7):
    frame.grid(row=0, column=0, sticky='nsew')




#----------------------------------------FRAME 1----------------------------------------#

#Ma Frame
frame_1 =  Frame(frame1, bg='#98A4FF')

#texte1
titre = Label(frame_1, text="Bienvenue sur notre application !", font=("Arial.tff", 60), fg='#000000', relief="flat")
titre.pack()

#texte2
titre2 = Label(frame_1, text="Crée ta propre Histoire", font=("Courrier.tff", 40), fg='#000000', relief="flat")
titre2.pack()

#Boutton Commencer
c = Button(frame_1, text="Commencer", command=lambda:alex.showframe(frame2), font=("Courrier.tff", 20))
c.pack(pady=10, ipadx=20)

#Boutton Ouvrir un Projet
c2 = Button(frame_1, text="Ouvrir un Projet", command=alex.fichiers, font=("Courrier.tff", 20))
c2.pack()

#Boutton Quitter
quitter = Button(frame1, text="Quitter", font=("Courrier.tff", 10), command=alex.quitter, relief="flat")
quitter.pack(side=BOTTOM, ipadx=35)

frame_1.pack(expand=YES)




#----------------------------------------FRAME 2----------------------------------------#

frame_2 =  Frame(frame2, bg='#98A4FF')

#Texte Crée perso
label_subtitle = Label (frame_2, text="Crée ta propre Histoire", font=("Courrier.tff", 40), fg='#000000', relief="flat")
label_subtitle.pack (side=TOP)

#--------------------Zone de text--------------------#
etiquette = Label(frame_2, text='Nom du personnage :')
etiquette.pack(padx=5, pady=5, side=TOP)

def perso():
    nom = nom_perso.get()
    file = open("nom.txt", "a")
    file.write(f"{nom}#")
    file.close()

nom_perso = StringVar()

entree = Entry(frame_2, width=50, textvariable=nom_perso)
entree.focus_force()
entree.pack(padx=5, pady=5)


#--------------------Boutton radio--------------------#
etiquette = Label(frame_2, text='Homme ou Femme :')
etiquette.pack(padx=5, pady=5)

def genre():
    genre = genre_perso.get()
    file = open("genre.txt", "a")
    file.write(f"{genre}#")
    file.close()

genre_perso = StringVar()

br = Radiobutton(frame_2, text="Homme", value=1, font=("Courrier.tff", 20), variable=genre_perso) #1 pour Homme
br2 = Radiobutton(frame_2, text="Femme", value=2, font=("Courrier.tff", 20), variable=genre_perso) #2 pour Femme
br.pack()
br2.pack()

#Bouton Valider
c = Button(frame_2, text="Valider", font=("Courrier.tff", 30), bg='#FFFFFF', fg='#000000', command=lambda:[perso(), genre(), alex.showframe(frame3)])
c.pack ()

#Quitter
c = Button(frame2, text="Quitter", font=("Courrier.tff", 10), command=alex.quitter, relief="flat")
c.pack(side=BOTTOM, ipadx=35)

frame_2.pack(expand=YES)




#----------------------------------------FRAME 3----------------------------------------#

#--------------------Question--------------------#
frame_q =  Frame(frame3, bg='#98A4FF')

question = Label(frame_q, text="Chapitre 1 :")
question.pack()

texteframe = Frame(frame_q)
scroll = Scrollbar(texteframe)
scroll.pack(side=RIGHT, fill=Y)

def chap1():
    question1 = text.get("1.0", "end")
    choix1 = choix1_1.get()
    choix2 = choix1_2.get()
    file = open("chapitre1.txt", "a")
    file.write(f"{question1}##{choix1}#{choix2}#")
    file.close()

text = Text(texteframe, width=50, height=10, yscrollcommand=scroll.set)
text.focus_set()
text.pack()
scroll.config(command=text.yview)
texteframe.pack()

frame_q.pack()

#--------------------Choix 1/2--------------------#

#Choix 1
frame_c =  Frame(frame3, bg='#98A4FF')

question = Label(frame_c, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
question.pack()

choix1_1 = StringVar()

nom1 = Entry(frame_c, width=50, textvariable=choix1_1)
nom1.focus_set()
nom1.pack()

#Choix 2

question = Label(frame_c, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
question.pack()

choix1_2 = StringVar()

nom1 = Entry(frame_c, width=50, textvariable=choix1_2)
nom1.focus_set()
nom1.pack()

frame_c.pack()

button = Button(frame3, text="Valider", font=("Courrier.tff", 15), command=lambda:[chap1(), alex.showframe(frame4)])
button.pack()




#----------------------------------------FRAME 4----------------------------------------#

#--------------------Question--------------------#
frame_q2 =  Frame(frame4, bg='#98A4FF')

question_2 = Label(frame_q2, text="Chapitre 2 :")
question_2.pack()

texteframe = Frame(frame_q2)
scroll = Scrollbar(texteframe)
scroll.pack(side=RIGHT, fill=Y)

def chap2():
    question2 = text.get("1.0", "end")
    choix3 = choix1_3.get()
    choix4 = choix1_4.get()
    file = open("chapitre2.txt", "a")
    file.write(f"{question2}##{choix3}#{choix4}#")
    file.close()

text = Text(texteframe, width=50, height=10, yscrollcommand=scroll.set)
text.focus_set()
text.pack()
scroll.config(command=text.yview)
texteframe.pack()

frame_q2.pack()

#--------------------Choix 1/2--------------------#

#Choix 1
frame_c2 =  Frame(frame4, bg='#98A4FF')

question_3 = Label(frame_c2, text="Choix De Fin :", font=("Arial.tff", 15), fg='#000000', relief="flat")
question_3.pack()

choix1_3 = StringVar()

nom3 = Entry(frame_c2, width=50, textvariable=choix1_3)
nom3.focus_set()
nom3.pack()

#Choix 2

question_4 = Label(frame_c2, text="Choix De Poursuite :", font=("Arial.tff", 15), fg='#000000', relief="flat")
question_4.pack()

choix1_4 = StringVar()

nom4 = Entry(frame_c2, width=50, textvariable=choix1_4)
nom4.focus_set()
nom4.pack()

frame_c2.pack()

button = Button(frame4, text="Valider", font=("Courrier.tff", 15), command=lambda:[chap2(), alex.showframe(frame5)])
button.pack()


alex.showframe(frame1)


projet.mainloop()