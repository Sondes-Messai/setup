#qcm a 2 question 
#les question capital de france et presidant de france
#posez chaque question un a une
#saisie la reponse par l'utulisateur de chaque question
#verifier et affichez si la reponse  si la bonne ou pas 
# Définir les questions et les réponses correctes

# Définir les questions et les réponses correctes
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "reponses_possibles": ["Berlin", "Paris", "Madrid"],
        "bonne_reponse": "Paris"
    },
    {
        "question": "Qui est le président de la France ?",
        "reponses_possibles": ["Emmanuel Macron", "Nicolas Sarkozy","Jacques Chirac"],
        "bonne_reponse": "Emmanuel Macron"
    }
]

# Boucle pour poser chaque question
for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    print("Réponses possibles:", ", ".join(q["reponses_possibles"]))
    reponse_utilisateur = input("Votre réponse: ")

    # Vérifier si la réponse de l'utilisateur est correcte
    if reponse_utilisateur.capitalize() == q["bonne_reponse"]:
        print("Bonne réponse!\n")
    else:
        print(f"Faux. La réponse correcte était: {q['bonne_reponse']}\n")




