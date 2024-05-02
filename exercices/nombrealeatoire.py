import random

# Le programme choisit un nombre aléatoire entre 0 et 100
nombre_secret = random.randint(0, 100)
# Nombre maximum d'essais autorisés
nombre_essais_max = 10
# Compteur d'essais
nombre_essais = 0

print("Devinez le nombre que j'ai choisi entre 0 et 100.")

# Boucle de jeu
while nombre_essais < nombre_essais_max:
    # L'utilisateur essaie de deviner le nombre
    essai = int(input("Entrez votre essai : "))
    nombre_essais += 1  # Incrémentation du compteur d'essais
    
    # Le programme indique si l'essai est plus grand ou plus petit que le nombre secret
    if essai < nombre_secret:
        print("C'est plus grand.")
    elif essai > nombre_secret:
        print("C'est plus petit.")
    else:
        print("Bravo ! Vous avez trouvé le nombre secret.")
        break  # Fin de la boucle si le nombre est correct

# Si le nombre d'essais atteint le maximum sans trouver le nombre secret
if nombre_essais == nombre_essais_max:

    print(f"Vous avez atteint le nombre maximum d'essais. Le nombre secret était {nombre_secret}.")

