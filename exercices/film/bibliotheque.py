# Create the Bibliotheque class
class Bibliotheque:
    def __init__(self):
        self.films = []
        self.taille = 0

    def film(self, film):
        self.films.append(film)
        self.taille += 1

    def annee(self, annee):
        resultats = []
        for f in self.films:
            if f.annee == annee:
                resultats.append(f)
        return resultats

    def afficher(self):
        for film in self.films:
               print(" - " + str(film.annee) + " : "  + film.titre + ", " + film.realisateur)
        print()