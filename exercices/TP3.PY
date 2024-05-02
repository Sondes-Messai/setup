#cree une liste des articles a achetez
#demandez l'utulisateur a ajoutez des article
#demandez lui egalement a suprimez un article
# listez les article achetez
#comptez et affichez les article
articles_a_acheter = []

def ajouter_article():
    article = input("Entrez l'article à ajouter à la liste : ")
    articles_a_acheter.append(article)
    print(f"L'article '{article}' a été ajouté à la liste.")

def supprimer_article():
    article = input("Entrez l'article à supprimer de la liste : ")
    if article in articles_a_acheter:
        articles_a_acheter.remove(article)
        print(f"L'article '{article}' a été supprimé de la liste.")
    else:
        print(f"L'article '{article}' n'est pas dans la liste.")

def afficher_articles():
    print("Articles à acheter :")
    for article in articles_a_acheter:
        print("- " + article)

def compter_articles():
    count = len(articles_a_acheter)
    if count == 0:
        print("Aucun article dans la liste.")
    elif count == 1:
        print("Il y a 1 article dans la liste.")
    else:
        print(f"Il y a {count} articles dans la liste.")

# Ajout d'un article
ajouter_article()

# Suppression d'un article
supprimer_article()

# Affichage de la liste
afficher_articles()

# Comptage des articles
compter_articles()
