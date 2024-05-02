#ecrivez une fonction demamdezNombre() qui demande un entier a l'utulisateur
def demandezNombre ()
	
    while True:
        try:
            # Demande à l'utilisateur de saisir un nombre entier
            nombre = int(input("Veuillez saisir un nombre entier : "))
            # Si la saisie est correcte, retourne le nombre
            return nombre
        except ValueError:
            # Si la saisie n'est pas un nombre entier, affiche un message d'erreur
            print("Ce n'est pas un nombre entier valide. Veuillez réessayer.")
# Utilisation de la fonction




















# Utilisation de la fonction
nombre_utilisateur = demandezNombre()
print(f"Le nombre entier saisi est {nombre_utilisateur}.")
