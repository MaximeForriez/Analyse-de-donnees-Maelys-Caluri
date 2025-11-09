#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Mettre dans un commentaire le numéro de la question

## Question 1
# Fait

## Question 2
# Fait

## Question 3
# Notre éditeur est VS_Code



## Question 4
# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)



## Question 5
table = pd.DataFrame(contenu)
print(table)



## Question 6
nb_ligne   = len(table)
nb_colonne = len(table.columns)

reponse = "Le tableau contient {} lignes et {} colonnes."
print(reponse.format(nb_ligne, nb_colonne))



## Question 7
# Pour chaque colonne :
#   On extrait le premier élément
#   On regarde son type
#   On le rajoute à la liste
liste_types = []
for nom_colonne in table.columns :
    element = table[nom_colonne][0]
    #print(element, " --- ", type(element))
    if type(element) == str :
        liste_types.append(str)

    elif type(element) == np.float64 :
        liste_types.append(float)

    elif type(element) == np.int64 :
        liste_types.append(int)

    elif type(element) == bool :
        liste_types.append(bool)

    else :
        liste_types.append(None)

print(liste_types)  



## Question 8
print(table.head(0))



## Question 9
inscrits = table["Inscrits"]
print(inscrits)



## Question 10
colonnes = table.columns 
liste_sommes = []
for i in range(len(table.columns)) :  
    nouvelle_colonne = table[colonnes[i]]

    if liste_types[i] == int :
        notre_somme = nouvelle_colonne.sum() 
        liste_sommes.append(notre_somme)

    elif liste_types[i] == float :
        notre_somme = nouvelle_colonne.sum() 
        liste_sommes.append(notre_somme)

print(liste_sommes) #On print en dehors de la boucle, une fois que toute la boucle est rédigée


## Question 11
idx = table["Code du département"]
X = table["Inscrits"]
Y = table["Abstentions"]
for i in range(len(idx)):

    plt.bar(["Inscrits", "Votants"], [X[i], Y[i]])
    #Ajout des titres et de la grille
    plt.title("Inscrits VS Votants dans le {}".format(idx[i])) #Titre principal
    plt.ylabel("Nombre") #Titre de l'axe vertical (Y)
    plt.grid(True)              #Ajout de la grille

    #Sauvegarde du résultat 
    plt.savefig("./output/images_Q11/ins_vs_vot_dep_{}.png".format(idx[i])) 
    plt.close() #Fermeture 'propre' du graphe  




## Question 12 
idx = table ["Code du département"]
Blan = table ["Blancs"]
Nuls = table ["Nuls"]
Expr = table ["Exprimés"]
Abst = table ["Abstentions"]
for i in range(len(idx)):

    quad_val = [Blan[i], Nuls[i], Expr[i], Abst[i]]
    quad_lab = ["Blancs", "Nuls", "Exprimés", "Abstentions"]

    plt.pie(quad_val, labels= quad_lab, autopct="%1.1f%%")

    #Ajout des titres et de la grille
    plt.title("Répartition des votes dans le {}".format(idx[i])) #Titre principal

    #Sauvegarde du résultat 
    plt.savefig("./output/images_Q12/diag_circ_repart_vot_dep_{}.png".format(idx[i])) 
    plt.close() #Fermeture 'propre' du graphe   


## Question 13
# Tracé de l'histogramme normalisé (aire = 1)
plt.hist(inscrits, bins = 20, density=True)  # density=True => aire totale = 1
plt.xlabel('Nombre d\'inscrits')
plt.ylabel('Densité')
plt.grid(True)
plt.title('Histogramme - distribution des inscrits (aire = 1)')

plt.savefig('./output/images_Q13/histogramme_inscrits.png')
plt.show()