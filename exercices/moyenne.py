# les mots clé
#list.append(nombre)
# Calculez la moyenne = sommme de nbr de la liste/len(liste) en utulient len et sum


# Création d'une liste vide:
liste_nombres = []

# Demande de cinq nombres à l'utilisateur:
for i in range(5):
    nombre = int(input("Entrez le nombre {}: ".format(i+1)))
    liste_nombres.append(nombre)

# Affichage de la liste:
print("La liste des nombres est :", liste_nombres)

# Calcul et affichage de la moyenne:
moyenne = sum(liste_nombres) / len(liste_nombres)
print("La moyenne des nombres est :", moyenne)
