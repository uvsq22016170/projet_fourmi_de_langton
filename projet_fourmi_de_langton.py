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

###############################################################################################################################################
#Constantes
#taille de base de la grille
taille = 9

###############################################################################################################################################
#Variables globales
Coul = ["black", "white"]
fourmi_placee = False

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

#Calcul du coefficient en fonction de la taille de l'écran actuel
calc_coeff ()

#Creation des widgets
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)
b_play_pause = tk.Button(racine, text = "Play")
b_next = tk.Button(racine, text = "Faire une étape")

#Placement des widgets
canvas.pack(side = "right")
b_play_pause.pack(side = "top", fill = "x")
b_next.pack(side = "top", fill = "x")

#Lien
canvas.bind("<Button-1>", init_fourmi)

#Initialisation
init()

#Boucle principale
racine.mainloop()