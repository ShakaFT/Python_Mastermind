import random

def mastermind(symboles = "ABCDEF", longueur_code = 4)->None:
    code = generer_code(symboles, longueur_code)
    #print(f"le code est {code}")
    liste_proposition = []
    while True:
        proposition = saisir_proposition(symboles, longueur_code)
        if proposition == code:
            print(f"Félicitations vous avez trouvé en {len(liste_proposition)+1} essais !")
            return
        liste_proposition.append(proposition)
        afficher(liste_proposition, code)

def generer_code(symboles:str, longueur_code:int)->str:
    return "".join(random.sample(symboles,4))


def saisir_proposition(symboles:str, longueur_code:int)->str:
    while True:
        proposition = input("Saisir une tentative : ").upper()
        if len(proposition) != longueur_code:
            print("ERREUR : la proposition doit contenir 4 caractères !")
            continue
        for c in proposition:
            if c not in symboles:
                print("Le code entré n'est pas valide !")
                break
        else:
            return proposition

def obtenir_bien_mal_place(proposition:str, code:str)->tuple:
    bien_place = 0
    mal_place = 0
    for c_prop, c_code in zip(proposition, code):
        if c_prop == c_code:
            bien_place += 1
        elif c_code in proposition:
            mal_place += 1
    return bien_place, mal_place

def afficher(liste_proposition:list, code)->None:
    for i, prop in enumerate(liste_proposition):
        bien_place, mal_place = obtenir_bien_mal_place(prop, code)
        print(f"Essai n°{i + 1} : {prop} : bien placé = {bien_place}, mal placé = {mal_place}")

mastermind()