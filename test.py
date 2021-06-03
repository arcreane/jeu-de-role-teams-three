from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


projet = Tk()
projet.geometry ("1280x720")
projet.minsize (1280, 720)
projet.maxsize (1280, 720)

projet.rowconfigure(0, weight=1)
projet.columnconfigure(0, weight=1)


def bouton():
    text1=choix2_1.get()
    file = open("tah.txt", "a")
    file.write(f"{text1}#")
    file.close()

choix2_1=StringVar()

nom1 = Entry(projet, width=40, textvariable=choix2_1)
nom1.focus_set()
nom1.pack()


button = Button(projet, text="Valider", font=("Courrier.tff", 15), command=bouton)
button.pack()

def capte():
    file = open("tah.txt", "r")
    text1 = file.read()
    texte2 = text1.split("#")
    label= Label(projet, text=texte2[0])
    #remplace le 0 par 1 ou 2 pour avoir les mots apres les #
    label.pack()

button2 = Button(projet, text="Tascapté", font=("Courrier.tff", 15), command=capte)
button2.pack()


projet.mainloop()