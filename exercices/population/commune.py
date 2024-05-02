from monde import Monde

class Commune:
    def __init__(self, nom, codepostal, population):
        self.nom = nom
        self.codepostal = codepostal
        self.__population = population
        Monde.populationTotale += self.__population

    def afficher(self):
        print(f" • le nom '{self.nom}': le code postal est : {self.codepostal}, le nombre de la population est : {self.__population}")

    def changer_population(self, nouvelle_valeur):
        self.__population = nouvelle_valeur
        print(f"Population mise à jour : {self.__population}")

#lorsaue une instance de commune est creé .sa population s'ajoute a la populationtotale de monde

#si la methode changerpopulation() est appelée, 
#les changement se reflétront correctement dans la population total 
#monde.population-=nouvelleValeur
#Monde.population+=self.  population
    def changer_population(self, nouvelle_valeur):
        self.monde.populationTotale += self.population
        self.population = nouvelle_valeur
        self.monde.ajouter__population(nouvelle_valeur)
        print("Populaion tolal:", self.monde.populationTotale) 