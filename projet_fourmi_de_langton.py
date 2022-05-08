###########################################################
# Groupe MI TD4
# Alexandre CHOLLET
# Adam HARBANE
# Bryan LE BLANC
# Kais CHEBOUB
# https://github.com/uvsq22016170/projet_fourmi_de_langton
###########################################################

###############################################################################################################################################
#Importation des modules
import tkinter as tk
import tkinter.messagebox as mb
import pickle

###############################################################################################################################################
#Constantes
#taille de base de la grille
taille = 100

#délai de base entre chaque étape
delai = 0

###############################################################################################################################################
#Variables globales
coul = ["black", "white"]
stop = False
fourmi_placee = False
execution = False
nbr_depl = 0

###############################################################################################################################################
#Fonctions

def calc_coeff ():
    """
    Calcul un coefficient en fonction de la taille de l'écran, ce coefficient est la taille des côtés des
    cases de la grille et permet que la fenêtre ne dépasse pas la taille de l'écran.
    """
    global coeff
    coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille

def init ():
    """
    Créé les variables globales config (liste de listes des valeurs associés à chaque case)
    et L_obj (liste de liste des identifiants des cases) ayant la bonne taille.
    """
    global config, L_obj
    config = [[0] * taille for i in range(taille)]
    L_obj = [[canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = coul[config[i][j]], outline = coul[config[i][j]]) for i in range (taille)] for j in range(taille)]

def init_fourmi (event):
    """
    Si il n'y a pas de fourmi dans la grille : place la fourmi à l'endroit du clic,
    créé la variable globale fourmi contenant [ligne de la fourmi, colonne de la fourmi, orientation de la fourmi].
    Sinon : message d'erreur.
    """
    global fourmi_placee, fourmi
    if fourmi_placee == False:
        fourmi = [int(event.y/coeff), int(event.x/coeff), 0]
        canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = "red", outline = "red")
        fourmi_placee = True
    else :
        mb.showwarning("Attention", "Une fourmi a déja été placée")

def reconfiguration (val):
    """
    Si la fontion play ne s'execute pas : réinitialisation de la grille à la valeur "val".
    Sinon : message d'erreur.
    """
    global fourmi_placee, nbr_depl
    if execution == False:
        fourmi_placee = False
        nbr_depl = 0
        for i in range (taille) :
            for j in range (taille) :
                config[i][j] = val
                canvas.itemconfigure(L_obj[i][j], fill = coul[config[i][j]], outline = coul[config[i][j]])
    else:
        mb.showwarning("Attention", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def noir ():
    reconfiguration(0)

def blanc ():
    reconfiguration(1)

def deplacement ():
    """
    Si la fourmi est sur la grille et si la fonction play ne s'execute pas : Tourne la fourmi, 
    change la valeur de la case sur laquelle elle se trouve et déplace la fourmi d'une case vers l'avant.
    Sinon : message d'erreur.
    """
    global nbr_depl
    if fourmi_placee == True and execution == False:
        nbr_depl += 1
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
        mb.showwarning("Attention", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def play ():
    """
    Si la fourmi est sur la grille : execute deplacement tant que l'utilisateur n'a pas cliqué sur le bouton stop.
    Sinon : message d'erreur.
    """
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
    """
    Fonction exécutée quand le bouton pause est activé.
    """
    global stop
    stop = True

def fen_dialog (titre, txt_label, fonction):
    """
    Créé une sous fenêtre de la fenêtre principale avec un label, une entry et un bouton.
    """
    global fen, entree
    fen = tk.Toplevel()
    fen.title(titre)
    entree = tk.Entry(fen, width = 100)
    label = tk.Label(fen, text = txt_label, width = 100)
    bouton = tk.Button(fen, text = "Ok", command = fonction)
    label.pack(side = "top", fill = "x")
    entree.pack(side = "top", fill ="x")
    bouton.pack(side = "top")

def recupere (txt_var, var):
    """
    Récupère ce qu'il y a dans l'entry de la sous-fenêtre créée avec la fonction ci-dessus
    et vérifie que ce qu'il y a dans l'entry est un entier (sinon message d'erreur,
    suppression de la saisie de l'entry et sortie de la fonction) puis l'affecte à la variable "var".
    Ferme la sous-fenêtre créée avec la fonction ci-dessus.
    """
    global taille, delai
    e = entree.get()
    if e.isnumeric() == False:
        entree.delete(0, tk.END)
        mb.showerror("Erreur", "Seuls les entier sont acceptés pour " + txt_var + " " + var)
        return False
    else :
        if var == "délai":
            delai = int(e)
        elif var == "taille":
            taille = int(e)
        elif var == "retours":
            retours(int(e))
        fen.destroy()

def retour ():
    """
    Si la fourmi est sur la grille et si la fonction play ne s'execute pas : Fait reculer
    la fourmi d'une case ou supprime la fourmi si elle est à sa position initiale.
    Sinon : message d'erreur.
    """
    global nbr_depl, fourmi_placee
    if fourmi_placee == True and execution == False:
        if nbr_depl != 0:
            nbr_depl -= 1
            canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = coul[config[fourmi[0]][fourmi[1]]], outline = coul[config[fourmi[0]][fourmi[1]]])
            fourmi[0] = int(fourmi[0] + (fourmi[2] == 0))%taille
            fourmi[1] = int(fourmi[1] + (fourmi[2] == 1))%taille
            fourmi[0] = int(fourmi[0] - (fourmi[2] == 2))%taille
            fourmi[1] = int(fourmi[1] - (fourmi[2] == 3))%taille
            fourmi[2] = (fourmi[2] + int(config[fourmi[0]][fourmi[1]] == 0) - int(config[fourmi[0]][fourmi[1]] == 1))%4
            config[fourmi[0]][fourmi[1]] = int(config[fourmi[0]][fourmi[1]] == 0)
            canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = coul[config[fourmi[0]][fourmi[1]]], outline = coul[config[fourmi[0]][fourmi[1]]])
            canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = "red", outline = "red")
        else : 
            canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = coul[config[fourmi[0]][fourmi[1]]], outline = coul[config[fourmi[0]][fourmi[1]]])
            mb.showerror("Erreur", "Plus de retour possible")
            fourmi_placee = False
    elif fourmi_placee == False and execution == False:
        mb.showerror("Erreur", "Il n'y pas de fourmi dans la grille")
    else :
        mb.showwarning("Attention", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def retours (nbr):
    """
    Execute la fonction retour "nbr" fois. Si la fourmi est à sa position initiale : Execute la fonction retour et sort de la fonction.
    """
    for i in range (nbr):
        if nbr_depl == 0:
            retour()
            return
        retour ()

def fen_retours ():
    """
    Si la fourmi est dans la grille et que la fonction play ne s'execute pas : execute la focntion fen_dialog.
    Sinon : message d'erreur.
    """
    if fourmi_placee == True and execution == False:
        fen_dialog("Fenêtre de choix du nombre de retours", "Veuillez saisir combien de fois vous voulez revenir en arrière (attention, seuls les entiers sont accéptés).", change_retours)
    elif fourmi_placee == False and execution == False:
        mb.showerror("Erreur", "Il n'y pas de fourmi dans la grille")
    else :
        mb.showwarning("Attention", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def change_retours ():
    recupere("le nombre de", "retours")

def sauvegarder ():
    """
    Si la fonction play ne s'execute pas : sauvegarede les variables taille, délai, nbr_depl, fourmi et 
    config dans le fichier "sauvegarde".
    Sinon : message d'erreur.
    """
    if execution == False :
        file = open("sauvegarde", "wb")
        pickle.dump(taille, file)
        pickle.dump(delai, file)
        pickle.dump(nbr_depl, file)
        pickle.dump(fourmi, file)
        pickle.dump(config, file)
        file.close()
    else :
        mb.showwarning("Attention", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def charger ():
    """
    Si la fonction play ne s'execute pas : récupère les variables taille, délai, nbr_depl, fourmi et 
    config du fichier "sauvegarde" et reconfigure la grille à partir de ces données.
    Sinon : message d'erreur.
    """
    global taille, delai, nbr_depl, fourmi, config, L_obj, fourmi_placee
    if execution == False :
        file = open("sauvegarde","rb")
        taille = pickle.load(file)
        delai = pickle.load(file)
        nbr_depl = pickle.load(file)
        fourmi = pickle.load(file)
        config = pickle.load(file)
        file.close()
        calc_coeff()
        L_obj = [[canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = coul[config[j][i]], outline = coul[config[j][i]]) for i in range (taille)] for j in range(taille)]
        fourmi_placee = True
        canvas.itemconfigure(L_obj[fourmi[0]][fourmi[1]], fill = "red", outline = "red")
    else :
        mb.showwarning("Attention", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def fen_delai ():
    fen_dialog("Fenêtre de changement de délai", "Veuillez saisir le nouveau délai (attention, seuls les entiers sont accéptés).", change_delai)

def fen_taille ():
    """
    Si la fonction play ne s'execute pas : execute la fonction fen_dialog.
    Sinon : message d'erreur.
    """
    if execution == False:
        fen_dialog("Fenêtre de changement de taille", "Veuillez saisir la nouvelle taille (attention, seuls les entiers sont accéptés).", change_taille)
    else :
        mb.showwarning("Attention", "La fourmi avance, veuillez mettre en pause pour effectuer cette action")

def change_delai():
    recupere("changer le", "délai")

def change_taille():
    global fourmi_placee
    if recupere("changer la", "taille") != False:
        calc_coeff()
        init()
        fourmi_placee = False

###############################################################################################################################################
#Partie principale

#Création de la fenêtre
racine = tk.Tk()
racine.title("Projet fourmi de langton")

#Calcul du coefficient en fonction de la taille de l'écran actuel
calc_coeff ()

#Creation des widgets
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)

l_deplace = tk.Label(racine, text = "Déplacement de la fourmi")
b_play_pause = tk.Button(racine, text = "Play", command = play)
b_next = tk.Button(racine, text = "Next", command = deplacement)
b_retours = tk.Button(racine, text = "Retourner plusieurs fois en arrière", command = fen_retours)
b_retour = tk.Button(racine, text = "Retourner en arrière", command = retour)

l_separe1 = tk.Label(racine)
l_separe2 = tk.Label(racine)

l_change_val = tk.Label(racine, text = "Changement de valeurs")
b_delai = tk.Button(racine, text = "Changer le delai", command = fen_delai)
b_taille = tk.Button(racine, text = "Changer la taille", command = fen_taille)

l_separe3 = tk.Label(racine)
l_separe4 = tk.Label(racine)

l_change_config = tk.Label(racine, text = "Changement de configuration")
b_noir = tk.Button(racine, text = "Configuration noir", command = noir)
b_blanc = tk.Button(racine, text = "Configuration blanc", command = blanc)

l_separe5 = tk.Label(racine)
l_separe6 = tk.Label(racine)

l_sauv_charge = tk.Label(racine, text = "Sauvegarde et chargement")
b_sauvegarde = tk.Button(racine, text = "Sauvegarder", command = sauvegarder)
b_charge = tk.Button(racine, text = "Charger", command = charger)

#Placement des widgets
canvas.pack(side = "right")

l_deplace.pack(side = "top", fill = "x")
b_play_pause.pack(side = "top", fill = "x")
b_next.pack(side = "top", fill = "x")
b_retours.pack(side = "top", fill = "x")
b_retour.pack(side = "top", fill = "x")

l_separe1.pack(side = "top")
l_separe2.pack(side = "top")

l_change_val.pack(side = "top", fill = "x")
b_delai.pack(side = "top", fill = "x")
b_taille.pack(side = "top", fill = "x")

l_separe3.pack(side = "top")
l_separe4.pack(side = "top")

l_change_config.pack(side = "top")
b_noir.pack(side = "top", fill = "x")
b_blanc.pack(side = "top", fill = "x")

l_separe5.pack(side = "top")
l_separe6.pack(side = "top")

l_sauv_charge.pack(side = "top", fill = "x")
b_sauvegarde.pack(side = "top", fill = "x")
b_charge.pack(side = "top", fill = "x")

#Lien entre le canvas et le clic du bouton gauche de la souris
canvas.bind("<Button-1>", init_fourmi)

#Initialisation
init()

#Boucle principale
racine.mainloop()