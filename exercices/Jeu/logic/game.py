#faire l'import
import random
#choix de l'utulisateur
def DemanderChoix():
    choix = input("Choisissez pierre, feuille ou ciseaux : ")
    return choix.lower()  
#choix d'ordinateur
def Generer_choix_ordinateur():
    choix_ordinateur = random.choice(["pierre", "feuille", "ciseaux"])
    return choix_ordinateur
#Resultat de choix
def DeterminerResultat(choix_joueur, choix_ordinateur):
    if choix_joueur == choix_ordinateur:
        return "Égalité"
    elif (choix_joueur == "pierre" and choix_ordinateur == "ciseaux") or \
         (choix_joueur == "feuille" and choix_ordinateur == "pierre") or \
         (choix_joueur == "ciseaux" and choix_ordinateur == "feuille"):
        return "Vous avez gagné !"
    else:
        return "L'ordinateur a gagné !" 
