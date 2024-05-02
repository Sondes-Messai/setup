#l'import des fichiers
from logic.game import DemanderChoix, Generer_choix_ordinateur, DeterminerResultat
#les choix des joueurs
if __name__ == "__main__":
    choix_joueur = DemanderChoix()
    choix_ordinateur = Generer_choix_ordinateur()
    resultat = DeterminerResultat(choix_joueur, choix_ordinateur)
    print(resultat)
    