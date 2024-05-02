# l'operation d'addition
def addition(x, y):
    return x + y

# l'operation soustraction
def soustraire(x, y):
    return x - y
# l'operation multiplier
def multiplier(x, y):
    return x * y
# l'operation diviser
def diviser(x, y):
    return x / y

#l'affichage du choix de l'utilisateur

print("Sélectionnez une opération :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
#choix de l'utulisateur
choix = input("Entrez votre choix (1/2/3/4) : ")

# Boucle 
if choix in ('1', '2', '3', '4'):
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    if choix == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    elif choix == '2':
        print(num1, "-", num2, "=", soustraire(num1, num2))
    elif choix == '3':
        print(num1, "*", num2, "=", multiplier(num1, num2))
    elif choix == '4':
        print(num1, "/", num2, "=", diviser(num1, num2))
else:
    print("Entrée invalide")
    
# Message du FINAL
print("Merci d'avoir utilisé ma calculatrice  !")
