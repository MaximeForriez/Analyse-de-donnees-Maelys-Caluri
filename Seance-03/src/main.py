#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023


# DEFINITION DES FONCTIONS LOCALES

def dresserListeTypeColonnes(table):  # Nous l'avions codée durant la séance 2
    types_colonnes = [] #On crée une liste vide (on l'initialise)
    #Pour chaque colonne, 
    for nom_colonne in table.columns : 
        element = table[nom_colonne][0]    # On extrait le premier élément
        if type(element) == np.float64 :    # Si il est de type "np.float"
            types_colonnes.append(float)     # Notre liste enregiste "float"

        elif type(element) == str :        # Idem avec les autre types
            types_colonnes.append(str)

        elif type(element) == np.int64 :
            types_colonnes.append(int)

        elif type(element) == bool :
            types_colonnes.append(bool)

        else :
            types_colonnes.append(None)
    return types_colonnes





print("\033[92m\n ## SEANCE 3 ##\n")

## Question 1
# création de src/data/
# on introduit le ficher "resultats-elections[...].csv"



## Question 2
# On introduit le fichier main.py



## Question 3
# Nous ouvrons le fichier main.py dans VS Code



## Question 4
print("\033[93m\n ## QUESTION 4 ##\n")

# Ouverture du fichier et extraction des informations dans la variable table
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv", "r") as fichier :
    contenu = pd.read_csv(fichier)

table = pd.DataFrame(contenu)

print("Voici la table extraite, identique à celle de la séance 2:")
print(table) 



## Question 5
# on dresse la liste des types des colonnes
types_colonnes = dresserListeTypeColonnes(table) # précédemment codé dans la séance 2

colonnes = table.columns 

# on initialise les listes
liste_titres_colonnes_quanti = []
moyennes = []
medianes = []
modes = []
ecarts_types = []
ecarts_absolus = []
etendues = []

for i in range(len(colonnes)):            # Pour chaque colonne :
    if types_colonnes[i] in [float, int]:   # si la colonne est quantitative :
        liste_titres_colonnes_quanti.append(colonnes[i])   # On enregistre le titre de la colonne traitée
        new_col = table[colonnes[i]]                       # On isole la colonne traitée

        # On calcule et stocke la moyenne des valeurs de la colonne
        moy = new_col.mean()
        moyennes.append(round(float(moy), 2))

        # On calcule et stocke la médiane des valeurs de la colonne
        med = new_col.median()
        medianes.append(round(float(med), 2))

        # On calcule et stocke le mode des valeurs de la colonne
        mod = new_col.mode()
        modes.append(round(mod, 2))

        # On calcule et stocke l'ecart-type des valeurs de la colonne
        eca_typ = new_col.std()
        ecarts_types.append(round(float(eca_typ), 2))

        # On calcule et stocke l'écart absolu à la moyenne, des valeurs de la colonne
        #   La méthode mad() n'existe plus, on calcule donc manuellement :
        #   "la moyenne des [ecarts-absolus à la moyenne]"
        somme_eca_abs = 0
        for j in range(len(new_col)):
            somme_eca_abs += np.abs(moy - new_col[j])
        eca_abs = somme_eca_abs / len(new_col)
        ecarts_absolus.append(round(float(eca_abs), 2))

        # On calcule et stocke l'étendue des valeurs de la colonne
        eten = np.abs(new_col.max() - new_col.min())
        etendues.append(round(float(eten), 2))



## Question 6
print("\033[94m\n ## QUESTION 6 ##\n")

print("Voici les différentes listes obtenues:")
print("\033[95m liste des colonnes quantitatives =", liste_titres_colonnes_quanti)
print("\033[94m moyennes =", moyennes)
print("\033[95m medianes =", medianes)
print("\033[95m modes =")
#print("modes =", modes)
print("\033[94m ecarts_types =", ecarts_types)
print("\033[95m ecarts_absolus =", ecarts_absolus)
print("\033[94m etendues =", etendues)



## Question 7
print("\033[93m\n ## QUESTION 7 ##\n")
distances_interquart = []
distances_interdec   = []
for nom_colonne in liste_titres_colonnes_quanti:
    new_col = table[nom_colonne]

    quart_25 = new_col.quantile(0.25)
    quart_75 = new_col.quantile(0.75)
    deci_10  = new_col.quantile(0.1)
    deci_90  = new_col.quantile(0.9)

    distances_interquart.append(round(float(quart_75 - quart_25),2))
    distances_interdec.append(round(float(deci_90 - deci_10), 2))

print("Voici les distances interquatiles et interdéciles obtenues pour chaque colonne:")
print("distances_interquart =" ,distances_interquart)
print("distances_interdec =", distances_interdec)


## Question 8
print("\033[94m\n ## QUESTION 8 ##\n")

print("Génération de boîtes à moustaches...")
for nom_colonne in liste_titres_colonnes_quanti:
    plt.boxplot(table[nom_colonne])
    
    plt.title("Boîte à moustaches pour la colonne {}".format(nom_colonne)) #Titre principal
    plt.xlabel(nom_colonne) #Titre de l'axe vertical (X)
    plt.ylabel("Effectif")  #Titre de l'axe vertical (Y)

    plt.grid(True)              #Ajout de la grille

    #Sauvegarde du résultat 
    plt.savefig("./output/img/boite_moustache_pour_{}.png".format(nom_colonne))
    plt.close() #Fermeture 'propre' du graphe

print("-> Voir dossier ./output/img")


## Question 9 
# C'est fait, on a bien le deuxième fichier .csv dans le dossier data


## Question 10
print("\033[93m\n ## QUESTION 10 ##\n")

with open("./data/island-index.csv", "r") as fichier_2 :
    contenu_2 = pd.read_csv(fichier_2, low_memory=False)

iles = pd.DataFrame(contenu_2)

surfaces = list(iles["Surface (km²)"]) # On isole la colonne "Surface (km²)" puis on la cast en liste

print("Voici la liste des surfaces (30 premières valeurs):")
print("surfaces[:30] = ", surfaces[:30])

# Oranigramme :
# La surface est-elle inférieure à 10 ?
#   |
#   --OUI: On enregistre dans ]0,10]
#   |
#   --NON: La surface est-elle inférieure à 25 ?
#       |
#       --OUI: On enregistre dans ]10,25]
#       |
#       --NON: La surface est-elle inféreieure à 50 ?
#           |
#           --OUI: On enregistre dans ]25,50]
#           |
#           --NON: La surface est-elle inféreieure à 100 ?
#               |
#               etc...

compte_0_10       = 0
compte_10_25      = 0
compte_25_50      = 0
compte_50_100     = 0
compte_100_2500   = 0
compte_2500_5000  = 0
compte_5000_10000 = 0
compte_10000_INF  = 0

for surface in surfaces: # Pour chaque surface :
    if surface <= 10.0:      # si la surface est inférieure à 10
        compte_0_10 += 1        # alors je la comptablise dans l'intervalle ]0, 10]
    elif surface <= 25.0:    # SINON, si la surface est inférieure à 25
        compte_10_25 += 1       # alors je la comptabilse dans l'intervalle ]10, 25]
    elif surface <= 50.0:    # SINON, si ...
        compte_25_50 += 1       # alors ...
    elif surface <= 100.0:
        compte_50_100 += 1
    elif surface <= 2500.0:
        compte_100_2500 += 1
    elif surface <= 5000.0:
        compte_2500_5000 += 1
    elif surface <= 10000.0:
        compte_5000_10000 += 1
    else :
        compte_10000_INF += 1

print("\nVoici les résultats de la catégorisation:")
print("Entre 0 et 10km², on dénombre {} îles."      .format(compte_0_10))
print("Entre 10 et 25km², on dénombre {} îles."       .format(compte_10_25))
print("Entre 25 et 50km², on dénombre {} îles."       .format(compte_25_50))
print("Entre 50 et 100km², on dénombre {} îles."      .format(compte_50_100))
print("Entre 100 et 2 500km², on dénombre {} îles."   .format(compte_100_2500))
print("Entre 2 500 et 5 000km², on dénombre {} îles." .format(compte_2500_5000))
print("Entre 5 000 et 10 000km², on dénombre {} îles.".format(compte_5000_10000))
print("Au delà de 10 000km², on dénombre {} îles."    .format(compte_10000_INF))

print("\033[0m\n")





