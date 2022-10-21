from random import random, randint


def deviner_nombre():
    # on etablit nos bornes
    borne_minimale = 0
    borne_maximale = 100
    nb_essais = 0
    # On genere un numero entre borne_minimale et borne_maximale
    mystere = randint(borne_minimale, borne_maximale)
    # print("Numero mystere est: " + str(mystere))
    print("J'ai choisi un nombre entre {0} et {1}".format(borne_minimale, borne_maximale))
    print("Ä vous de le deviner...")
    # Dans ce variable on garde
    essai = -1
    # une boucle dans laquelle on imprime une ligne
    while mystere != essai:
        valeur = input("Entrez votre essai :")
        essai = int(valeur)
        nb_essais = nb_essais + 1
        if essai > mystere:
            print("Mauvais choix, le nombre est plus petit que {0}".format(essai))
        if essai < mystere:
            print("Mauvaise réponse, le nombre est plus grand que {0}".format(essai))

    print("Bravo! Bonne réponse")
    print("Vous avez réussi en : {0} essai(s)".format(nb_essais))


if __name__ == '__main__':
    question = "o"
    while question == "o":
        deviner_nombre()
        question = input("Voulez-vous faire une autre partie (o/n)?")
    print("Merci et au revoir")
