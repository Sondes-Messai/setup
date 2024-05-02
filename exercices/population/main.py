
#l'import 
from commune import Commune

paris = Commune("paris","75000",620000)
paris.afficher()

# Création d'autres communes
marseille = Commune("Marseille", "13000", 850000)
lyon = Commune("Lyon", "69000", 520000)

# Modification de la population de Paris
paris._Commune__population = 700000

# Affichage des autres communes
marseille.afficher()
lyon.afficher()

# Vérification de la population totale
population_totale = paris._Commune__population + marseille._Commune__population + lyon._Commune__population
print(f"Population totale : {population_totale}")