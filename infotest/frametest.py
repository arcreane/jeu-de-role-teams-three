from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

def alert():
    showinfo("A Changer", "L'alerte askip")

def quitter():
    quit()

def fichiers():
    fiches = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
    photo = PhotoImage(file=filepath)

def showframe(frame):
    frame.tkraise()

choix = Tk()
choix.geometry ("1280x720")
choix.minsize (1280 ,720)
choix.maxsize (1280, 720)

choix.rowconfigure(0, weight=1)
choix.columnconfigure(0, weight=1)


#--------------------MENU HAUT--------------------#

menu = Menu(choix)

#Menu1
menu1 = Menu(menu, tearoff=0)
menu1.add_command(label="Nouveau", command=alert)
menu1.add_command(label="Ouvrir", command=fichiers)
menu1.add_command(label="Modifier", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=quitter)

menu.add_cascade(label="Fichier", menu=menu1)

#Menu2.1
menu4 = Menu(menu, tearoff=0)
menu4.add_command(label="Général", command=alert)
menu4.add_separator()
menu4.add_command(label="Interface", command=fichiers)
menu4.add_command(label="Performances", command=alert)
menu4.add_command(label="Disques de Travail", command=alert)

#Menu2
menu2 = Menu(menu, tearoff=0)
menu2.add_command(label="Annuler", command=alert)
menu2.add_command(label="Rétablir", command=alert)
menu2.add_separator()
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menu2.add_separator()
menu2.add_command(label="Rechercher", command=alert)
menu2.add_cascade(label="Préferences", menu=menu4)
menu2.add_command(label="Formes", command=alert)

menu.add_cascade(label="Edition", menu=menu2)

#Menu3
menu3 = Menu(menu, tearoff=0)
menu3.add_command(label="Nous Contacter", command=alert)
menu3.add_separator()
menu3.add_command(label="A propos", command=alert)

menu.add_cascade(label="Aide", menu=menu3)

choix.config(menu=menu)

#Les Frames

frame1 = Frame(choix, bg='#98A4FF')
frame2 = Frame(choix, bg='#98A4FF')
frame3 = Frame(choix, bg='#98A4FF')

for frame in (frame1,frame2,frame3):
    frame.grid(row=0, column=0, sticky='nsew')


#--------------------FRAME 1--------------------#

#Ma Frame
frame_1 =  Frame(frame1, bg='#98A4FF')

#texte1
titre = Label(frame_1, text="Bienvenue sur notre application !", font=("Arial.tff", 60), fg='#000000', relief="flat")
titre.pack()

#texte2
titre2 = Label(frame_1, text="Crée ta propre Histoire", font=("Courrier.tff", 40), fg='#000000', relief="flat")
titre2.pack()

#Boutton Commencer
c = Button(frame_1, text="Commencer", command=lambda:showframe(frame2), font=("Courrier.tff", 20))
c.pack(pady=10, ipadx=20)

#Boutton Ouvrir un Projet
c2 = Button(frame_1, text="Ouvrir un Projet", command=fichiers, font=("Courrier.tff", 20))
c2.pack()

#Boutton Quitter
quitter = Button(frame1, text="Quitter", font=("Courrier.tff", 10), command=quitter, relief="flat")
quitter.pack(side=BOTTOM, ipadx=35)

frame_1.pack(expand=YES)

#--------------------FRAME 2--------------------#

frame_2 =  Frame(frame2, bg='#98A4FF')

#texte Crée perso
label_subtitle = Label (frame_2, text="Crée ta propre Histoire", font=("Courrier.tff", 40), fg='#000000', relief="flat")
label_subtitle.pack (side=TOP)

#Zone de text
etiquette = Label(frame_2, text='Nom du personnage :')
etiquette.pack(padx=5, pady=5, side=TOP)

entree = Entry(frame_2, width=50, show="*")
entree.pack(padx=5, pady=5)
entree.focus_force()

#Boutton radio
etiquette = Label(frame_2, text='Homme ou Femme :')
etiquette.pack(padx=5, pady=5)

br = Radiobutton(frame_2, text="Homme", value=1, font=("Courrier.tff", 20))
br2 = Radiobutton(frame_2, text="Femme", value=2, font=("Courrier.tff", 20))
br.pack()
br2.pack()

#bouttonValider
c = Button(frame_2, text="Valider", font=("Courrier.tff", 30), bg='#FFFFFF', fg='#000000', command=lambda:showframe(frame3))
c.pack ()

#Exit

c = Button(frame2, text="Quitter", font=("Courrier.tff", 10), command=quitter, relief="flat")
c.pack(side=BOTTOM, ipadx=35)

frame_2.pack(expand=YES)

showframe(frame1)


choix.mainloop()