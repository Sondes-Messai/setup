#comparez 3-4 questions d'une enquete aupres de l'utulisateur

# affichez les questions une a une  en demande la repeonse

# stockez la reponse en variable


print("Enquete aupres de l'utilisateur")
print(end="\n\n")
prenom = input("Entrez votre prenom: ")
print(end="\n\n")
nom = input("Entrez votre nom: ")
print(end="\n\n")
sex = input("Entrez votre sex: ")
print(end="\n\n")
postal = input("Entrez votre code postal: ")
print(end="\n\n")
ibn = input("Entrez votre ibn: ")
print(end="\n\n")



annee = 2024
anneeNaissance = int(input("Entrez votre année de naissance: "))
ageApproximatif = annee - anneeNaissance

print("Bonjour " + prenom)
print(end="\n\n")
print("Votre nom est :" + nom)
print(end="\n\n")
print("Votre sex est : " + sex)
print(end="\n\n")
print("Votre code postal est : " + postal)
print(end="\n\n")
print("Votre ibn est :" + ibn)
print(end="\n\n")
print("Vous avez environ :" + str(ageApproximatif) + " ans")
print(end="\n\n")
print("Merci de votre inscription a notre site a bientot")

