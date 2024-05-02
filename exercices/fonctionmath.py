#ecrire la fonction pythagore(a,b) qui calculera l'hypotenuse a partir des cote de aet b
#ecrire la fonction distance (xA,yA,xb,yB) qui calcule la distance entre A t B
#ecrivez la fonction moyenne (liste) qui apartir d'une liste de nombre calcule sa moyenne
#ecrivez les fonction min(liste)et max(list) qui nous retourne
# l'element le plus petit et l'element le plus grand de la liste
#import math
#math.sqrt()
#theoreme de pythagore:
import math 
 #Pythagore
def pythagore (a,b):
    return math.sqrt(a*a+b*b)

print(pythagore(23,14))
print(pythagore(3,4))
print(pythagore(316,40))
#Distance
def distance(xA, yA, xB, yB):
    return math.sqrt((xB - xA)**2 + (yB - yA)**2)
print (distance(3,3,3,9))
#Moyenne
def moyenne(liste):
    return sum(liste) / len(liste) 
#Min 
def min_liste(liste):
    return min(liste) 
#Max
def max_liste(liste):
    return max(liste) 


    


  
  


