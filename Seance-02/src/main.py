#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

print("\033[92m\n ## SEANCE 2 ##\n")
## Question 1 ##
# Dans le dossier "src", nous avons créé le dossier "data" et y avons introduit le fichier "resultats-elections-presidentielles-2022-1er-tour.csv"



## Question 2 ##
# Dans le dossier "src", nous avons introduit le fichier "main.py"



## Question 3 ##
# Nous travaillons dans l'éditeur de code 'VS Code'



## Question 4 ##
# Ouverture du fichier "resultats-elections-presidentielles-2022-1er-tour.csv",
# puis lecture de son contenu
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier) #'pd.read_csv()' est la méthode "read_csv()" de la bibliothèque "Pandas",
                                   # celle-ci permet de lire les fichiers au format C.S.V.



## Question 5 ##
print("\033[94m\n ## QUESTION 5 ##\n")
# On affiche la variable "contenu" sous forme d'une table
table = pd.DataFrame(contenu) #'pd.DataFrame()' est la méthode "DataFrame()" de la bibliothèque "Pandas",
                              # celle-ci permet de structurer l'affichage des données (Data) - de façon bien rangée, comme un tableau (Frame)

print("Voici la table extraite :")
print(table)



## Question 6 ##
print("\033[93m\n ## QUESTION 6 ##\n")
# Mesure du nombre de lignes et de colonnes par la fonction native "len()"
nb_lignes =   len(table)
nb_colonnes = len(table.columns) #'table.columns' est la liste des titres des colonnes
#print("table.columns =", table.columns) #OPTIONNEL: pour voir de quoi on parle

# Affichage du résultat
reponse = "Le tableau de données contient {} lignes et {} colonnes."
print(reponse.format(nb_lignes, nb_colonnes)) # la méthode "format()" va injecter les variables dans la chaîne de caractère,
                                              # respectivement aux endroits indiqués par '{}'




## Question 7 ##
print("\033[94m\n ## QUESTION 7 ##\n")
# PRINCIPE :
# "Pour chaque colonne :
#   On extrait le premier élément
#   On regarde son type
#   On rajoute ce type à la liste."

# On dresse une liste qui renseigne le type de chaque colonne
liste_types = [] #On crée une liste vide (on l'initialise)

for nom_colonne in table.columns : # Pour chaque colonne:
    element = table[nom_colonne][0] # On extrait le premier élément
    if type(element) == np.float64 : # Si il est de type "np.float"
        liste_types.append(float)     # Notre liste enregiste "float"

    elif type(element) == str :      # Idem avec les autre types
        liste_types.append(str)

    elif type(element) == np.int64 :
        liste_types.append(int)

    elif type(element) == bool :
        liste_types.append(bool)

    else :
        liste_types.append(None)    # Dans le cas d'un type non connu, on enregistre "None"

    print("Le 1er élément de la colonne '{}' = {} --> est de type : {}".format(nom_colonne, element, liste_types[-1]))

# Affichage de la liste des types obtenue
print("\n Voici un aperçu de la liste des types obtenue :")
print(liste_types)



## Question 8 ##
print("\033[93m\n ## QUESTION 8 ##\n")
# Affichage du nom des colonnes avec la méthode "head()"
print("Voici la liste des noms des colonnes, avec la méthode 'head()' :")
print(table.head(0)) # notons qu'elle s'utilise ainsi : [pd.DataFrame].head(n)
                     # (avec n le nombre de lignes à afficher, en partant d'en haut)



## Question 9 ##
print("\033[94m\n ## QUESTION 9 ##\n")
# On isole la colonne qui renseigne le nombre des inscrits
inscrits = table["Inscrits"] 
print("Voici la colonne du nombre des inscrits:")
print(inscrits) # Affichage



## Question 10 ## 
print("\033[93m\n ## QUESTION 10 ##\n")
# PRINCIPE :
# "Pour chaque colonne :
#   On isole la colonne,
#   On somme cette liste grâce à la méthode sum()."

colonnes = table.columns 
liste_sommes = [] # Initialisation de la liste des sommes
for i in range(len(colonnes)) : # Pour chaque colonne:  
    nouvelle_colonne = table[colonnes[i]] # On isole la colonne

    if liste_types[i] == int :            # On en vérifie le type en se référant à la liste des types à la position correspondante
        somme = nouvelle_colonne.sum()        # Si le type est un entier, on peut sommer la colonne 
        liste_sommes.append(int(somme))       # et la caster en entier (int) avant de l'enreistrer dans la liste des sommes

    elif liste_types[i] == float :        # Idem dans le seul autre cas d'un type "float".
        somme = nouvelle_colonne.sum() 
        liste_sommes.append(float(somme))

print("Voici la liste des sommes de chaque colonne:")
print(liste_sommes) # Une fois que toute la liste est rédigée, on l'affiche



## Question 11 ##
print("\033[94m\n ## QUESTION 11 ##\n")

# On isole les colonnes nécessaires
idx = table["Code du département"]
X = table["Inscrits"]
Y = table["Votants"]

print("Génération de diagrammes en barres...")
for i in range(len(idx)):

    plt.bar(["Inscrits", "Votants"], [X[i], Y[i]])

    #Ajout des titres et de la grille
    plt.title("Comparaison des Inscrits et des Votants dans le {}".format(idx[i])) #Titre principal
    plt.ylabel("Nombre")        #Titre de l'axe vertical
    plt.grid(True)              #Ajout de la grille

    #Sauvegarde du résultat 
    plt.savefig("./output/images_Q11/ins_vs_vot_dep_{}.png".format(idx[i])) 
    plt.close()  #Fermeture 'propre' du graphe  

print("-> Voir dossier ./output/images_Q11")



## Question 12 
print("\033[93m\n ## QUESTION 12 ##\n")

# On isole les colonnes nécessaires
idx = table ["Code du département"]
Blan = table ["Blancs"]
Nuls = table ["Nuls"]
Expr = table ["Exprimés"]
Abst = table ["Abstentions"]

print("Génération de diagrammes circulaires...")
for i in range(len(idx)):

    quad_val = [Blan[i], Nuls[i], Expr[i], Abst[i]]
    quad_lab = ["Blancs", "Nuls", "Exprimés", "Abstentions"]

    plt.pie(quad_val, labels= quad_lab, autopct="%1.1f%%")

    #Ajout des titres et de la grille
    plt.title("Répartition des votes dans le {}".format(idx[i])) #Titre principal

    #Sauvegarde du résultat 
    plt.savefig("./output/images_Q12/diag_circ_repart_vot_dep_{}.png".format(idx[i])) 
    plt.close() #Fermeture 'propre' du graphe
print("-> Voir dossier ./output/images_Q12")   



## Question 13
print("\033[94m\n ## QUESTION 13 ##\n")

# Tracé de l'histogramme normalisé (aire = 1)
print("Génération d'un histogramme...")

plt.hist(inscrits, bins = 20, density=True)  # density=True => aire totale = 1
plt.xlabel('Nombre d\'inscrits')
plt.ylabel('Densité')
plt.grid(True)
plt.title('Histogramme - distribution des inscrits (aire = 1)')

plt.savefig('./output/images_Q13/histogramme_inscrits.png')
plt.show()

print("-> Voir dossier ./output/images_Q13") 

print("\033[0m\n")
