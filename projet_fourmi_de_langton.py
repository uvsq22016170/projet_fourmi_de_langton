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

###############################################################################################################################################
#Constantes
#taille de base de la grille
taille = 9

###############################################################################################################################################
#Variables globales
Coul = ["black", "white"]

###############################################################################################################################################
#Fonctions

def init ():
    """
    Initialise la grille
    """
    global config, L_obj, coeff, fourmi
    coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille
    config = [[0] * taille for i in range(taille)]
    L_obj = [[] * taille for i in range(taille)]
    fourmi = [taille/2, taille/2, "N"]

def noir ():
    for i in range (taille) :
        for j in range (taille) :
            L_obj[i] += [canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = Coul[0], outline = Coul[0])]

def blanc ():
    for i in range (taille) :
        for j in range (taille) :
            L_obj[i] += [canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = Coul[1], outline = Coul[1])]

def random ():
    for i in range (taille):
        for j in range (taille):
            config[i][j] = rd.randint(0, 1)
            canvas.itemconfigure(L_obj[i][j], fill = Coul[config[i][j]], outline = Coul[config[i][j]])

###############################################################################################################################################
#Partie principale

#Création de la fenêtre
racine = tk.Tk()
racine.title("Projet fourmi de langton")

#Initialisation
init()

#Creation des widgets
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)
b_play_pause = tk.Button(racine, text = "Play")
b_next = tk.Button(racine, text = "Faire une étape")

#Placement des widgets
canvas.pack(side = "right")
b_play_pause.pack(side = "top", fill = "x")
b_next.pack(side = "top", fill = "x")

#Boucle principale
racine.mainloop()