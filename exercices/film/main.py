#Faire l'import de film
from film import Film
from bibliotheque import Bibliotheque
# Create the library
biblio = Bibliotheque()
biblio.film(Film(titre="Inception", realisateur="Christopher Nolan", annee=2011))
biblio.film(Film(titre="Titanic", realisateur="Quentin Tarantino", annee=1994))
biblio.film(Film(titre="The Matrix", realisateur="Lana Wachowski", annee=1999))

# Get user input for the desired year
anneeCherchee = int(input("Quelle année recherchez-vous?: "))
resultats = biblio.annee(anneeCherchee)

if len(resultats) < 1:
    print("Nous n'avons aucun film sorti en", anneeCherchee, "dans notre bibliothèque.")
else:
    for film in resultats:
         print(str(film.titre) + " est sorti en " + str(film.annee) + ".")
