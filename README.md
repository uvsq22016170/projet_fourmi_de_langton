Groupe MI TD4
Alexandre CHOLLET
Adam HARBANE
Bryan LE BLANC
Kais CHEBOUB
https://github.com/uvsq22016170/projet_fourmi_de_langton

Règles du jeu :
- Si la fourmi est sur une case noire, elle tourne de 90° vers la gauche, change
la couleur de la case en blanc et avance d’une case.
- Si la fourmi est sur une case blanche, elle tourne de 90° vers la droite,
change la couleur de la case en noir et avance d’une case.

Utilisation du programme :
Au lancement du programme une fenêtre s'ouvre. En cliquant dans le cadre de droite une fourmi est positionnée à l'endroit du clic. 
Les différentes fonctions possibles sont déclenchées par les boutons à gauche :
    - Play : Déclanche le déplacement de la fourmi. Ce bouton se transforme en pause quand la fourmi est lancée.
    - Pause : Arrête le déplacement de la fourmi. Ce bouton se transforme en play quand la fourmi est stoppée.
    - Next : Déplace la fourmi d'une case.
    - Retourner plusieurs fois en arrière : Permet de saisir le nombre de retours arrières de la fourmi et fait revenir la fourmi an arrière de ce nombre.
    - Retourner en arrière : Fait revenir la fourmi une fois en arrière.
    - Changer le délai : Permet de saisir le délai en millisecondes entre chaque déplacement de la fourmi. Par défaut le délai est 0.
    - Changer la taille : Permet de saisir la taille de la grille ou peut se déplacer la fourmi . Par défaut le taille est 100.
    - Configuration noir : Initialise la grille avec des cases noires.
    - Configuration blanc : Initialise la grille avec des cases blanches.
    - Sauvegarder : Sauvegarde les information suivantes dans un fichier nommé "sauvegarde" : taille de la grille, etat de la grille, position de la fourmi, nombre de déplacements de la fourmi, délai entre chaque déplacement de la fourmi.
    - Charger : Lit le fichier nommé "sauvegarde" et initialise la grille avec ces informations.