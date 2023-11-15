questions = [
    "Combien de fois la France a-t-elle remporté la Coupe du monde de football ?",
    "Quand Apple a-t-elle été fondée ?",
    "Qui a fondé SpaceX ?"
]
reponses = [
    "2",
    "1976",
    "Elon Musk"
]


def poser_question(question, reponse, chances_restantes = 3):
    while chances_restantes > 0:
        reponse_utilisateur = input(question)
        if reponse_utilisateur.lower() == reponse.lower():
            print("Bonne réponse !")
            return chances_restantes
        else:
            chances_restantes -= 1
            print(f"Mauvaise réponse ! Il vous reste {chances_restantes} chances.")
    return chances_restantes 

def executer_quiz():
    chances_restantes = 3
    for i in range(len(questions)):
        chances_restantes = poser_question(questions[i], reponses[i], chances_restantes)


executer_quiz()
