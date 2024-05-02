
from jeux import Jeu

class JeuxSociete(Jeu):
    def __init__(self, titre, annepublication, joueurs):
        super().__init__(titre)
        self.annepublication = annepublication
        self.joueurs = joueurs

    def affiche(self):
        super().affiche()
        print("Année de publication :", self.annepublication)
        print("Nombre de joueurs :", self.joueurs)