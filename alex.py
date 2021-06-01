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