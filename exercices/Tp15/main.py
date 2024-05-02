#Cree main.py jeux.py jeux_video.py et jeux_societe.py donnez l'attribut titre 
#a la classe jeu et la methode affichez (self) qui affichera le titre dujeux
#Fait l'heritage la classe jeuxsociete et jeu et ajoutez les attribut annepublication 
#et joueurs puis surchargez la methode affichez()
#Faire heritez la classe jeux video de jeu et ajoutz y 
#l'attributs editeur puis surchargez la methode affichee() pour l'affichez
#Ajoutez la methode lancer (self) sur la classe jeuxvideo qui affichera comme quoi le jeux est lance lorsqu'elle est applée


from jeux import Jeu
from jeux_societe import JeuxSociete
from jeux_video import JeuxVideo

# Création d'un jeu de société
jeu_societe = JeuxSociete("Monopoly", 1935, 2)
jeu_societe.affiche()

# Création d'un jeu vidéo
jeu_video = JeuxVideo("The Legend of Zelda: Breath of the Wild", "Nintendo")
jeu_video.affiche()




