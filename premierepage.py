from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

#Fenetre
f = Tk ()

f.title ("Le meilleur jeu au monde")
f.geometry ("1280x720")
f.minsize (1280 ,720)
f.maxsize (1280, 720)
f.iconbitmap("logo.ico")
f.config(background='#084B8A')

#BackGround
bg = PhotoImage(file="fond.png")
label1 = Label(f, image=bg)
label1.place(x=-2, y=-2)

#Menu en Haut
def fichiers():
    fiches = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
    photo = PhotoImage(file=filepath)

def quitter():
    quit()
    pass

def commencer():
    showinfo("Message d'Alerte", "Est-tu vraiment prêt?")

def alert():
    showinfo("Un truc comme ca", "Bravo tu a cliqué")

menu = Menu(f)

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

f.config(menu=menu)


#Ma Frame
frame =  Frame(f)

#texte1

titre = Label(frame, text="Bienvenue sur notre application !", font=("Arial.tff", 60), fg='#000000', relief="flat")
titre.pack()

#texte2
titre2 = Label(frame , text="Crée ta propre Histoire", font=("Courrier.tff", 40), fg='#000000', relief="flat")
titre2.pack()

#Boutton Commencer
c = Button(frame, text="Commencer", command=commencer, font=("Courrier.tff", 20))
c.pack(pady=10, ipadx=20)

#Boutton Ouvrir un Projet
c2 = Button(frame, text="Ouvrir un Projet", command=fichiers, font=("Courrier.tff", 20))
c2.pack()

#Boutton Quitter
quitter = Button(f, text="Quitter", command=quitter, font=("Courrier.tff", 20))
quitter.pack(side=BOTTOM)

#Fin de Frame
frame.pack(expand=YES)


f.mainloop ()