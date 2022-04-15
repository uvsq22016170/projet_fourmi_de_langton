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

###############################################################################################################################################
#Constantes
#taille de base de la grille
taille = 9

###############################################################################################################################################
#Variables globales

###############################################################################################################################################
#Fonctions
    
###############################################################################################################################################
#Partie principale

#Création de la fenêtre
racine = tk.Tk()
racine.title("Projet fourmi de langton")

#Calcul du coefficient en fonction de la taille de l'écran actuel
coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille

#Creation des widgets
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)

#Placement des widgets
canvas.pack(side = "right")

#Boucle principale
racine.mainloop()