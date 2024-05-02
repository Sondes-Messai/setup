#Relisez et inspirez-vous de l’algorithme 
#du jeu du pendu que vous avez rédigé au TP1
#Utilisez les différents éléments vus précédemment 
#(variables, conditions, listes, boucles, etc.) 
#pour implémenter l’algorithme​


#l'import pour que le jeux fonctionne
import random

# Liste des mots possibles pour le jeu
choix = ["Casserole", "Cuillere", "Patate", "Souris","Tetine","Balon","Fourchet"]

# Sélection aléatoire d'un mot de la liste
solution = random.choice(choix)

# Initialisation du nombre de tentatives
tentatives = 7

# Initialisation de l'affichage du mot à deviner
affichage = ""

# Initialisation de la chaîne contenant les lettres trouvées
lettres_trouvees = ""

# Création de l'affichage initial avec des underscores
for l in solution:
  affichage = affichage + "_ "

# Message de bienvenue
print(">> Bienvenue dans le pendu <<")

# Boucle de jeu principale
while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  
  # Demande une lettre au joueur 
  #lower()méthode renvoie une chaîne où tous les caractères sont en minuscules.
  proposition = input("proposez une lettre : ")[0:1].lower()

  # Vérifie si la lettre proposée est dans le mot
  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print("-> Nope\n")
    
    # Affichage du pendu en fonction du nombre de tentatives restantes
    if tentatives==0:
        print(" ==========+= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|\ ")
    if tentatives<=4:
        print(" ||       /|  ")
    if tentatives<=5:                    
        print("/||           ")
    if tentatives<=6:
        print("==============\n")

  # Mise à jour de l'affichage du mot à deviner
  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  # Vérifie si toutes les lettres ont été trouvées
  if "_" not in affichage:
      print(">>> le pendu est sauvé de la mort ! <<<")
      break

# Fin de la partie
print("\n    * Fin de l'exection *    ")
