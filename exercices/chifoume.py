import random  # Importation du module random pour générer des nombres aléatoires

def jouerchifoumi():
    choix = ["pierre", "papier", "ciseaux"]  # Liste des choix possibles dans le jeu
    ordinateur = random.choice(choix)  # Choix aléatoire de l'ordinateur parmi la liste des choix

    # Demande au joueur de choisir et stocke le choix dans la variable 'joueur'
    joueur = input("Choisissez pierre, papier ou ciseaux: ").lower()

#Vérifie si le choix du joueur est valide
    if joueur not in choix:
        print("Choix invalide. Veuillez choisir entre pierre, papier ou ciseaux.")
        return

    # Affiche les choix de l'ordinateur et du joueur
    print("L'ordinateur a choisi:", ordinateur)
    print("Le joueur a choisi:", joueur)

    # Comparaison des choix pour déterminer le résultat
    if joueur == ordinateur:
        print("Égalité !")
    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "papier" and ordinateur == "pierre") or \
         (joueur == "ciseaux" and ordinateur == "papier"):
        print("Le joueur gagne !")
    else:
        print("L'ordinateur gagne !")

