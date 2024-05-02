#creé un dictionnaire contenant les utulisateur

utilisateurs = {
    "sondes": "motdepasse123",
    "toto": "secret456",
    "titi": "qwerty789"
}
#demandez a l'utulisateur de saisir son username et mot de passe
nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
mot_de_passe = input("Entrez votre mot de passe pour logez : ")

#Vérifie si le nom d'utilisateur existe dans le dictionnaire
if nom_utilisateur in utilisateurs:
    # Vérifie si le mot de passe saisi est correcte ou non
    if utilisateurs[nom_utilisateur] == mot_de_passe:
        print("Bienvenue dans votre espace")
    else:

        print("Mot de passe incorrect. Veuillez réessayer.")

#

      







































