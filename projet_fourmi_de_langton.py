###########################################################
# Groupe MI4
# Alexandre CHOLLET
# Adam HARBANE
# Bryan LE BLANC
# Kais CHEBOUB
# https://github.com/uvsq22016170/projet_fourmi_de_langton
###########################################################

###############################################################################################################################################
#Importation des modules
import tkinter as tk
import random as rd
import tkinter.messagebox as mb

import numpy as np
import itertools
from matplotlib import pyplot as plt
from matplotlib import animation, colors

###############################################################################################################################################
#Constantes
#taille de base de la grille
taille = 100

#délai entre chaque étape
delai = 0

###############################################################################################################################################
#Variables globales
coul = ["black", "white"]
stop = False
fourmi_placee = False
execution = False


###############################################################################################################################################
#Fonctions

def calc_coeff ():
    global coeff
    coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille

def init ():
    global config, L_obj
    config = [[0] * taille for i in range(taille)]
    L_obj = [[canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = coul[config[i][j]], outline = coul[config[i][j]]) for i in range (taille)] for j in range(taille)]

def init_fourmi (event):
    global fourmi_placee, fourmi, mem
    if fourmi_placee == False:
        fourmi = [int(event.y/coeff), int(event.x/coeff), 0]
        canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = "red", outline = "red")
        fourmi_placee = True
        mem = ["pas de fourmi"]
    else :
        mb.showerror("Erreur", "Une fourmi a déja été placée")

def reconfiguration (val):
    global fourmi_placee
    if execution == False:
        fourmi_placee = False
        for i in range (taille) :
            for j in range (taille) :
                if val == "r":
                    config[i][j] = rd.randint(0,1)
                else :
                    config[i][j] = val
                canvas.itemconfigure(L_obj[i][j], fill = coul[config[i][j]], outline = coul[config[i][j]])
    else:
        mb.showerror("Erreur", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def noir ():
    reconfiguration(0)

def blanc ():
    reconfiguration(1)

def aleatoire ():
    reconfiguration("r")

def deplacement ():
    global mem, execution
    if fourmi_placee == True and execution == False:
        mem += [[fourmi.copy(), config[fourmi[0]][fourmi[1]]]]
        if len(mem) > 100:
            mem = mem[1:]
        fourmi[2] = (fourmi[2] + int(config[fourmi[0]][fourmi[1]] == 0) - int(config[fourmi[0]][fourmi[1]] == 1))%4
        config[fourmi[0]][fourmi[1]] = int(config[fourmi[0]][fourmi[1]] == 0)
        canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = coul[config[fourmi[0]][fourmi[1]]], outline = coul[config[fourmi[0]][fourmi[1]]])
        fourmi[0] = int(fourmi[0] - (fourmi[2] == 0))%taille
        fourmi[1] = int(fourmi[1] - (fourmi[2] == 1))%taille
        fourmi[0] = int(fourmi[0] + (fourmi[2] == 2))%taille
        fourmi[1] = int(fourmi[1] + (fourmi[2] == 3))%taille
        canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = "red", outline = "red")
    elif fourmi_placee == False and execution == False:
        mb.showerror("Erreur", "Il n'y pas de fourmi dans la grille")
    else :
        mb.showerror("Erreur", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def play ():
    global stop, execution
    if fourmi_placee == True:
        execution = True
        b_play_pause.config(text = "Pause", command = pause)
        while stop == False:
            execution = False
            deplacement()
            execution = True
            canvas.after(delai, racine.update())
        execution = False
        stop = False
        b_play_pause.config(text = "Play", command = play)
    else :
        mb.showerror("Erreur", "Il n'y pas de fourmi dans la grille")

def pause ():
    global stop
    stop = True

def retour ():
    global fourmi, mem, fourmi_placee
    if fourmi_placee == True and execution == False:
        if mem != [] :
            canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = coul[config[fourmi[0]][fourmi[1]]], outline = coul[config[fourmi[0]][fourmi[1]]])
            if mem != ["pas de fourmi"]:
                config[mem[-1][0][0]][mem[-1][0][1]] = mem[-1][1]
                fourmi = mem[-1][0]
                canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = "red", outline = "red")
            else :
                fourmi_placee = False
            mem = mem[:-1]
        else :
            mb.showerror("Erreur", "Plus de retour possible : mémoire vide")
    elif fourmi_placee == False and execution == False:
        mb.showerror("Erreur", "Il n'y pas de fourmi dans la grille")
    else :
        mb.showerror("Erreur", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

###############################################################################################################################################
#Partie principale

#Création de la fenêtre
racine = tk.Tk()
racine.title("Projet fourmi de langton")

#Calcul du coefficient en fonction de la taille de l'écran actuel
calc_coeff ()

#Creation des widgets
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)
b_play_pause = tk.Button(racine, text = "Play", command = play)
b_next = tk.Button(racine, text = "Faire une étape", command = deplacement)
b_retour = tk.Button(racine, text = "Retourner en arrière", command = retour)
b_noir = tk.Button(racine, text = "Configuration noir", command = noir)
b_blanc = tk.Button(racine, text = "Configuration blanc", command = blanc)
b_aleatoire = tk.Button(racine, text = "Configuration aléatoire", command = aleatoire)

#Placement des widgets
canvas.pack(side = "right")
b_play_pause.pack(side = "top", fill = "x")
b_next.pack(side = "top", fill = "x")
b_retour.pack(side = "top", fill = "x")
b_aleatoire.pack(side = "bottom", fill = "x")
b_blanc.pack(side = "bottom", fill = "x")
b_noir.pack(side = "bottom", fill = "x")

#Lien
canvas.bind("<Button-1>", init_fourmi)

#Initialisation
init()

#Boucle principale
racine.mainloop()