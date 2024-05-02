from jeux import Jeu

class JeuxVideo(Jeu):
    def __init__(self, titre, editeur):
        super().__init__(titre)
        self.editeur = editeur

    def affiche(self):
        super().affiche()
        print("Éditeur :", self.editeur)

    def lancer(self):
        print("Le jeu est lancé !")