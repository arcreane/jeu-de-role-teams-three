from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

def alert():
    showinfo("Alerte", "Tu ne peux pas faire ceci.")

def alertv2():
    showinfo("Alerte", "Vous pouvez nous contacter via Teams.")

def alertv3():
    showinfo("Alerte", "L'équipe se compose de:\n\n- Vacheron Matthieu,\n- Antoine Alexandre,\n- Beliouz Nacim,\n- Salin Annabelle,\n- Thayaparan Sangar")

def quitter():
    quit()

def destroy():
    jeu.destroy()

def effacer1():
    file = open('Histoire1/chapitre1.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire1/message.txt', 'w')
    file.write('')
    file.close


    file = open('Histoire1/genre.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire1/nom.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire1/chapitre2.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire1/chapitre3.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire1/chapitre4.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire1/chapitre5.txt', 'w')
    file.write('')
    file.close


def effacer2():
    file = open('Histoire2/chapitre1.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire2/message.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire2/genre.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire2/nom.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire2/chapitre2.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire2/chapitre3.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire2/chapitre4.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire2/chapitre5.txt', 'w')
    file.write('')
    file.close


def effacer3():
    file = open('Histoire3/chapitre1.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire3/message.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire3/genre.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire3/nom.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire3/chapitre2.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire3/chapitre3.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire3/chapitre4.txt', 'w')
    file.write('')
    file.close

    file = open('Histoire3/chapitre5.txt', 'w')
    file.write('')
    file.close