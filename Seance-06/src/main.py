#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

#Fonction pour ouvrir les fichiers
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Fonction pour convertir les données en données logarithmiques
def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

#Fonction pour trier par ordre décroissant les listes (îles et populations)
def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

#Fonction pour obtenir le classement des listes spécifiques aux populations
def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

#Fonction pour obtenir l'ordre défini entre deux classements (listes spécifiques aux populations)
def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

#Partie sur les îles:
## Question 2
iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv"))
#print(iles)


## Question 3
surface = list(iles["Surface (km²)"])
#print("surface =", surface)

#Ajout de la valeur Asie / Afrique / Europe = ...
surface.append(float(85545323))
surface.append(float(37856841))
surface.append(float(7768030))
surface.append(float(7605049))
#print("surface =", surface)


## Question 4
surface_dec = ordreDecroissant(surface)
#print("20 prem. val. de surface_dec =", surface_dec[0:20])


## Question 5
rangs = list(range(1, len(surface_dec) +1)) #Liste pour l'axe des abscisses, on a rangs = [1,2,3, ... , 84223]
plt.plot(rangs, surface_dec, "o-") #Génération du graphe

plt.title("Q5 - Loi rang-taille des iles") #Ajout du titre
plt.xlabel("Rang")          #Ajout du titre de l'axe X
plt.ylabel("Surface (km²)") #Ajout du titre de l'axe Y
plt.grid(True)              #Ajout de la grille

plt.savefig("./output/Q5_loi_rang_taille_iles.png") #Sauvegarde du résultat sous le nom "Q5_loi_rang_taille_iles.png"
plt.close() #Fermeture propre du graphe


## Question 6
#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().
surface_dec_log = conversionLog(surface_dec)
rangs_log = conversionLog(rangs)

plt.plot(rangs_log, surface_dec_log, "o-") #Génération du graphe

plt.title("Q6 - Loi rang-taille (log-log) des iles") #Ajout du titre
plt.xlabel("log(Rang)")          #Ajout du titre de l'axe X
plt.ylabel("log(Surface)") #Ajout du titre de l'axe Y
plt.grid(True)              #Ajout de la grille

plt.savefig("./output/Q6_loi_rang_taille_log_log_iles.png") #Sauvegarde du résultat sous le nom 
plt.close() #Fermeture propre du graphe


## Question 7
# Non, on ne peut pas faire un test (statistique) sur les rangs. 
# Les rangs ne sont pas issus d'un échantillon aléatoire, mais ils sont générés par
# une simple numérotation ordonnée (1er, 2e, 3e, ...). 
# En effet, nous avons créé la liste des rangs après avoir trié la liste des surfaces. 
# La corrélation entre le rang et la taille est donc évidente, car forcée "par construction".
# Le rang et la taille ne sont donc pas des variables indépendantes issues de mesures distinctes.
# Cela implique qu'on ne peut pas appliquer un test de corrélation (au sens statistique) entre le rang et la taille. 





#Partie sur les populations des États du monde

## Question 9
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))
#print(monde)

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().

## Question 10
etats = list(monde["État"])
pop_2007 = list(monde["Pop 2007"])
pop_2025 = list(monde["Pop 2025"])
densite_2007 = list(monde["Densité 2007"])
densite_2025 = list(monde["Densité 2007"])

#print("etats =", etats)
#print("\033[91m pop_2007 = ", pop_2007)
#print("\033[92m pop_2025 =", pop_2025)
#print("\033[93m densite_2007 =", densite_2007)
#print("\033[94m densite_2025 =", densite_2025)
#print("\033[0m")

## Question 11
ord_pop_2007 = ordrePopulation(pop_2007, etats)
ord_pop_2025 = ordrePopulation(pop_2025, etats)
ord_densite_2007 = ordrePopulation(densite_2007, etats)
ord_densite_2025 = ordrePopulation(densite_2025, etats)

print("\033[91m ord_pop_2007 =", ord_pop_2007)
print("\033[92m ord_pop_2025 =", ord_pop_2025)
print("\033[93m ord_densite_2007 =", ord_densite_2007)
print("\033[94m ord_densite_2025 =", ord_densite_2025)
print("\033[0m")

