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
        for element1 in range(0, len(ordre2)):
            for element2 in range(0, len(ordre1)):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1)):
            for element2 in range(0, len(ordre2)):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element1][1]])
    return classement

#Partie sur les îles

## Question 2 ##
#Ouverture du fichier "island-index.csv"
iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv")) 
#print(iles) #OPTIONNEL: aperçu du tableau entier

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().



## Question 3 ##
#On isole la colonne "Surface (km²)" en la castant en list()
surfaces = list(iles["Surface (km²)"])
#print(surfaces) #OPTIONNEL: aperçu de la liste créée /!\ Affichage terminal volumineux

#Ajout des valeurs de surface des continents
surfaces.append(float(85545323)) #Asie / Afrique / Europe
surfaces.append(float(37856841)) #Amérique
surfaces.append(float( 7768030)) #Antarctique
surfaces.append(float( 7605049)) #Australie
#print(surfaces) #OPTIONNEL: aperçu de la liste complétée /!\ Affichage terminal volumineux



## Question 4 ##
#On ordonne la liste "surfaces" (de façon décroissante) 
surfaces_decroissant = ordreDecroissant(surfaces)
#print(surfaces_decroissant) #OPTIONNEL: aperçu de la liste complétée et triée /!\ Affichage terminal volumineux



## Question 5 ##
#On crée la liste des rangs (qui seront les abscisses du graphe)
rangs = list(range(1, len(surfaces_decroissant)+1)) #On a: rangs = [1, 2, 3, ... , 84223]

#Génération du graphe
plt.plot(rangs, surfaces_decroissant, "o-") #Génération du graphe

#Ajout des titres et de la grille
plt.title("Q5 - Loi rang-taille des terres émergées") #Titre principal
plt.xlabel("Rang")          #Titre de l'axe horizontal (X)
plt.ylabel("Surface (km²)") #Titre de l'axe vertical (Y)
plt.grid(True)              #Ajout de la grille

#Sauvegarde du résultat 
plt.savefig("./output/Q5-loi_rang-taille_terres.png") #sous le nom "Q5-loi_rang-taille_terres.png"
plt.close() #Fermeture 'propre' du graphe



## Question 6 ##
#Passage des valeurs au logarithme
surf_decr_log = conversionLog(surfaces_decroissant) #Pour les surfaces (axe Y)
rangs_log = conversionLog(rangs)                    #Pour les rangs (axe X)

#Génération du graphe corrigé
plt.plot(rangs_log, surf_decr_log, "o-")

#Ajout des titres et de la grille
plt.title("Q6 - Loi rang-taille (log-log) des terres émergées") #Titre principal
plt.xlabel("log(Rang)")    #Titre de l'axe horizontal (X)
plt.ylabel("log(Surface)") #Titre de l'axe vertical (Y)
plt.grid(True)             #Ajout de la grille

#Sauvegarde du résultat 
plt.savefig("./output/Q6-loi_rang-taille_log-log_terres.png") #sous le nom "Q6-loi_rang-taille_log-log_terres.png"
plt.close() #Fermeture 'propre' du graphe



## Question 7 ##
# Non, on ne peut pas faire un test (statistique) sur les rangs. 
# Les rangs ne sont pas issus d'un échantillon aléatoire, mais ils sont générés par
# une simple numérotation ordonnée (1er, 2e, 3e, ...). 
# En effet, nous avons créé la liste des rangs après avoir trié la liste des surfaces. 
# La corrélation entre le rang et la taille est donc évidente, car forcée "par construction".
# Le rang et la taille ne sont donc pas des variables indépendantes issues de mesures distinctes.
# Cela implique qu'on ne peut pas appliquer un test de corrélation (au sens statistique) entre le rang et la taille. 





#Partie sur les populations des États du monde

## Question 9 ##
#Ouverture du fichier "Le-Monde-HS-Etats-du-monde-2007-2025.csv"
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))
#print(monde) #OPTIONNEL: aperçu du tableau entier

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().



## Question 10 ##
#On isole les cinq colonnes demandées en les castant en list()
etats =       list(monde["État"]) 
pop2007 =     list(monde["Pop 2007"])
pop2025 =     list(monde["Pop 2025"])
densite2007 = list(monde["Densité 2007"])
densite2025 = list(monde["Densité 2025"])

#OPTIONNEL: aperçu des listes créées
#print("etats =", etats)           #État
#print("pop2007 =", pop2007)       #Pop 2007
#print("pop2025 =", pop2025)       #Pop 2025
#print("densite2007 =", densite2007) #Densité 2007
#print("densite2025 =", densite2025) #Densité 2025



## Question 11 ##
#On ordonne les listes de manière décroissante
ord_pop2007 = ordrePopulation(pop2007, etats)         #Pop 2007 ordonnée
ord_pop2025 = ordrePopulation(pop2025, etats)         #Pop 2025 ordonnée
ord_densite2007 = ordrePopulation(densite2007, etats) #Densité 2007 ordonnée
ord_densite2025 = ordrePopulation(densite2025, etats) #Densité 2025 ordonnée

#OPTIONNEL: aperçu des listes triées
#print("ord_pop2007 =", ord_pop2007)         #Pop 2007 ordonnée
#print("ord_pop2025 =", ord_pop2025)         #Pop 2025 ordonnée
#print("ord_densite2007 =", ord_densite2007) #Densité 2007 ordonnée
#print("ord_densite2025 =", ord_densite2025) #Densité 2025 ordonnée



## Question 12 ##
#Comparaison entre le classement des États selon leurs populations de 2007
#               et le classement des États selon leurs densités de 2007
compar_pop_dens_2007 = classementPays(ord_pop2007,ord_densite2007)

#Comparaison entre le classement des États selon leurs populations de 2025
#               et le classement des États selon leurs densités de 2025
compar_pop_dens_2025 = classementPays(ord_pop2025,ord_densite2025)

#OPTIONNEL: aperçu des comparatifs obtenus
#print("compar_pop_dens_2007 =", compar_pop_dens_2007) #pour l'année 2007
#print("compar_pop_dens_2025 =", compar_pop_dens_2025) #pour l'année 2025


#Le comparatif obtenu pour 2007 est ordonné par rapport à "ord_pop2007"
# (c.à.d par rapport au classement des États selon leurs populations)
compar_pop_dens_2007.sort()

#Le comparatif obtenu pour 2025 est ordonné par rapport à "ord_pop2025"
# (c.à.d par rapport au classement des États selon leurs populations)
compar_pop_dens_2025.sort()

#OPTIONNEL: aperçu des comparatifs - ordonnés par rapport à "ord_pop20XX"
# (c.à.d par rapport au classement des États selon leurs populations)
#print("compar_pop_dens_2007 =", compar_pop_dens_2007) #pour l'année 2007
#print("compar_pop_dens_2025 =", compar_pop_dens_2025) #pour l'année 2025



## Question 13 ##
#Pour l'année 2007
#On isole les deux premières colonnes relatives aux rangs
# (premièrement les rangs selon la population
#          puis les rangs selon la densité    )
rangs_pop_2007 = []     #Initialisation de la liste "rangs_pop_2007"
rangs_densite_2007 = [] #Initialisation de la liste "rangs_densite_2007"
#Boucle : on parcourt tout le classement "compar_pop_dens_2007" - composé de triplets
for triplet in compar_pop_dens_2007 :    #Pour chaque triplet,   
    rangs_pop_2007.append(triplet[0])        #Écriture du premier  élément dans "rang_pop_2007"
    rangs_densite_2007.append(triplet[1])    #Écriture du deuxième élément dans "rang_densite_2007"

#OPTIONNEL: aperçu des listes obtenues
#print("rangs_pop_2007 =", rangs_pop_2007)         #rangs selon la population en 2007
#print("rangs_densite_2007 =", rangs_densite_2007) #rangs selon la densitée en 2007


#Pour l'année 2025
#On isole les deux premières colonnes relatives aux rangs
# (premièrement les rangs selon la population
#          puis les rangs selon la densité    )
rangs_pop_2025 = []     #Initialisation de la liste "rangs_pop_2025"
rangs_densite_2025 = [] #Initialisation de la liste "rangs_densite_2025"
#Boucle : on parcourt tout le classement "compar_pop_dens_2025" - composé de triplets
for triplet in compar_pop_dens_2025 :    #Pour chaque triplet,   
    rangs_pop_2025.append(triplet[0])        #Écriture du premier  élément dans "rang_pop_2025"
    rangs_densite_2025.append(triplet[1])    #Écriture du deuxième élément dans "rang_densite_2025"

#OPTIONNEL: aperçu des listes obtenues
#print("rangs_pop_2025 =", rangs_pop_2025)         #rangs selon la population en 2025
#print("rangs_densite_2025 =", rangs_densite_2025) #rangs selon la densité en 2025



## Question 14 ##
#Pour l'année 2007

# 1-Corrélation
#Calcul du coefficient de corrélation rho entre les rangs selon la population en 2007
#                                            et les rangs selon la densité en 2007
rho_2007, p_value_spearman_2007 = scipy.stats.spearmanr(rangs_pop_2007,rangs_densite_2007)
#La fonction spearmanr() renseigne deux valeurs:
#     rho : mesure la corrélation entre les deux classements.
#              - si rho proche de +1 : les classements sont très similaires
#              - si rho proche de -1 : les classements sont inversés
#              - si rho proche de  0 : les classements ne corrèlent pas
#
#     p-value : c'est la probabilité qu'il n'y ait aucune corrélation entre les classements.
#               (On note H0 l'hypothèse "nulle": H0 = "il n'y a aucune corrélation entre les classements")
#
#              - si p-value  < 0.05 (soit  < 5%): --> on rejette l'hypothèse H0 
#                                                     (avec un risque de se tromper < 5%)
#                                                 --> la corrélation observée est donc très probablement réelle 
#                                                     (corrélation sûre à plus de 95%) 
#
#              - si p-value >= 0.05 (soit >= 5%): --> on ne peut pas rejeter l'hypothèse H0
#                                                     (car on aurait un risque de se tromper >= 5%)
#                                                 --> aucune corrélation n'est donc prouvée. Ainsi, si rho montre une corrélation, celle-ci est peut-être dûe au hasard
#                                                     (corrélation sûre à moins de 95%)

print("rho_2007 =", rho_2007)
print("p_value_spearman_2007 =", p_value_spearman_2007)

# 2-Concordance
#Calcul du coefficient de concordance tau entre les rangs selon la population en 2007
#                                            et les rangs selon la densité en 2007
tau_2007, p_value_kendall_2007 = scipy.stats.kendalltau(rangs_pop_2007,rangs_densite_2007)
#La fonction kendalltau() renseigne deux valeurs:
#     tau : mesure la concordance entre les deux classements.
#              - si tau proche de +1 : les classements concordent fortement
#              - si tau proche de -1 : les classements discordent fortement
#              - si tau proche de  0 : les classements n'ont pas de lien
#
#     p-value : c'est la probabilité qu'il n'y ait aucune concordance entre les classements.
#               (On note H0 l'hypothèse "nulle": H0 = "il n'y a aucune concordance entre les classements")
#
#              - si p-value  < 0.05 (soit  < 5%): --> on rejette l'hypothèse H0 
#                                                     (avec un risque de se tromper < 5%)
#                                                 --> la concordance observée est donc très probablement réelle 
#                                                     (concordance sûre à plus de 95%) 
#
#              - si p-value >= 0.05 (soit >= 5%): --> on ne peut pas rejeter l'hypothèse H0
#                                                     (car on aurait un risque de se tromper >= 5%)
#                                                 --> aucune concordance n'est donc prouvée. Ainsi, si tau montre une concordance, celle-ci est peut-être dûe au hasard
#                                                     (concordance sûre à moins de 95%)

print("tau_2007 =", tau_2007)
print("p_value_kendall_2007 =", p_value_kendall_2007)

#Interprétation
# Pour l'année 2007, on obtient rho = 0.093 et tau = 0.067. Ces valeurs sont proches de 0, ce qui
# signifie qu'il n'y a ni corrélation ni concordance entre les classements selon la population et selon la densité.
# 
# De plus, les 'p-value' des tests de Spearman et de Kendall sont respectivement de 0.224 et 0.192, ce qui 
# est bien supérieur à 0.050 (5%). On ne peut donc pas rejeter l'hypothèse "nulle", selon laquelle "il n'y a pas de relation entre les classements".
#
# Conclusion : D'après les données de 2007, il n'y a donc pas de corrélation - statistiquement significative - entre 
# la population d'un État et sa densité de population : ce sont deux grandeurs variant indépendamment.



#Pour l'année 2025

# 1-Corrélation
#Calcul du coefficient de corrélation rho entre les rangs selon la population en 2025
#                                            et les rangs selon la densité en 2025
rho_2025, p_value_spearman_2025 = scipy.stats.spearmanr(rangs_pop_2025,rangs_densite_2025)

#print("rho_2025 =", rho_2025)
#print("p_value_spearman_2025 =", p_value_spearman_2025)

# 2-Concordance
#Calcul du coefficient de concordance tau entre les rangs selon la population en 2025
#                                            et les rangs selon la densité en 2025
tau_2025, p_value_kendall_2025 = scipy.stats.kendalltau(rangs_pop_2025,rangs_densite_2025)

print("tau_2025 =", tau_2025)
print("p_value_kendall_2025 =", p_value_kendall_2025)

#Interprétation
# Pour l'année 2025, on obtient rho = -0.027 et tau = -0.007. Ces valeurs sont quasiment nulles, ce qui
# signifie qu'il n'y a ni corrélation ni concordance entre les classements selon la population et selon la densité.
# 
# De plus, les 'p-value' des tests de Spearman et de Kendall sont respectivement de 0.709 et 0.877, ce qui 
# est largement supérieur à 0.050 (5%). On accepte donc l'hypothèse "nulle", selon laquelle "il n'y a pas de relation entre les classements".
#
# Conclusion : D'après les données de 2025, il n'y a donc pas de corrélation - statistiquement significative - entre 
# la population d'un État et sa densité de population : ce sont deux grandeurs variant indépendamment.
#
# N.B.:L'analyse des données de 2007 et l'analyse des données de 2025 aboutissent à cette même conclusion.



## BONUS ##

## Algorithme pour les îles ##
#On propose l'algorithme suivant:
#   DESCRIPTION DE L'ALGO



# VERSION 1 = On ne modifie pas le fichier 'island.csv'
# DONC on génère nous meme la liste des identifiants.


# METHODE 1 : METHODE RUSSE = On lance le même programme : ARCHI CHRONOPHAGE
#                                                          Compléxité quadratique !
###Ouverture du fichier "island-index.csv"
##iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv")) 
###print(iles) #OPTIONNEL: aperçu du tableau entier
##
###On isole les colonnes "Surface" et "Trait de côte"
##surfaces = list(iles["Surface (km²)"])
##traits =   list(iles["Trait de côte (km)"])
##
##limite = 1000
##surfaces = surfaces[0:limite]
##traits = traits[0:limite]
###On crée la liste des identifiants (de même taille que les colonnes isolées)
##idents = list(range(1, len(surfaces)+1))
##
###OPTIONNEL: aperçu des 10 premières valeurs des listes obtenues
###print("surfaces[0:10] =", surfaces[0:10]) #10 premières valeurs de 'surfaces'
###print("traits[0:10]   =", traits[0:10])   #10 premières valeurs de 'traits'
###print("idents[0:10]   =", idents[0:10])   #10 premières valeurs de 'idents'
##
###On ordonne les listes de manière décroissante
##ord_surf =  ordrePopulation(surfaces, idents)
##ord_trait = ordrePopulation(traits,   idents)
##
##print("ord_surf  =",  ord_surf)
##print("ord_trait =", ord_trait)
##
##compar_surf_trait= classementPays(ord_surf, ord_trait)
##
##compar_surf_trait.sort()
##print("compar_surf_trait =", compar_surf_trait)
##
##rangs_surf = []  #Initialisation de la liste des rangs des surfaces
##rangs_trait = [] #Initialisation de la liste des rangs des traits
###Boucle : on parcourt tout le classement "compar_pop_dens_2007" - composé de triplets
##for triplet in compar_surf_trait :    #Pour chaque triplet,   
##    rangs_surf.append(triplet[0])        #Écriture du premier  élément dans "rang_pop_2007"
##    rangs_trait.append(triplet[1]) 
##
##rho_surf_trait, p_value_spearman_surf_trait = scipy.stats.spearmanr(rangs_surf,rangs_trait)
##
##tau_surf_trait, p_value_kendall_surf_trait = scipy.stats.kendalltau(rangs_surf,rangs_trait)
##
##print("rho_surf_trait =", rho_surf_trait)
##print("p_value_spearman_surf_trait =", p_value_spearman_surf_trait)
##
##print("tau_surf_trait =", tau_surf_trait)
##print("p_value_kendall_surf_trait =", p_value_kendall_surf_trait)

# RESULTATS DE LA METHODE RUSSE :
# rho_surf_trait = 0.9712866815534842
# p_value_spearman_surf_trait = 0.0
# tau_surf_trait = 0.8539337169239855
# p_value_kendall_surf_trait = 0.0
#
# TEMPS DE CALCUL : > 20 minutes

# METHODE 2 : METHODE REFLECHIE
# On cherche coute que coute à ne pas faire de 'recherche carrée' càd :
# for i in range (84000) :
#     for j in range (84000) :
#         nombre de passage ici = 84 000 * 84 000 = 7 056 000 000

print ("\033[91m DEPART : METHODE REFLECHIE \033[0m")

import time

debut = time.time()
s = list(iles["Surface (km²)"])
t =   list(iles["Trait de côte (km)"])

couple_t_s = []
for i in range(0, len(s)):
    if (np.isnan(t[i]) == False) and (np.isnan(s[i]) == False):
        couple_t_s.append([t[i], s[i]])

couple_t_s.sort()
class_1 = []
for i in range(0,len(couple_t_s)):
    class_1.append([couple_t_s[i][1],couple_t_s[i][0],i+1])

class_1.sort()
rangs_s=[]
rangs_t=[]
for i in range(0, len(class_1)):
    rangs_s.append(i+1)
    rangs_t.append(class_1[i][2])

rho_s_t, p_value_spearman_s_t = scipy.stats.spearmanr(rangs_s,rangs_t)

tau_s_t, p_value_kendall_s_t = scipy.stats.kendalltau(rangs_s,rangs_t)



print("rho_s_t =", rho_s_t)
print("p_value_spearman_s_t =", p_value_spearman_s_t)

print("tau_s_t =", tau_s_t)
print("p_value_kendall_s_t =", p_value_kendall_s_t)

fin = time.time()
print("tps exec =", fin-debut)

# RESULTATS DE LA METHODE REFLECHIE :
# rho_s_t = 0.9712866815534842
# p_value_spearman_s_t = 0.0
# tau_s_t = 0.8539337169239855
# p_value_kendall_s_t = 0.0
#
# TEMPS DE CALCUL : 0.333 secondes

print ("\033[92m CALCUL TERMINÉ EN", str(((fin-debut)//0.001)/1000), "SECONDES ! \033[0m")







## Partie population Mondiale :

def calculCorrelationConcordance(chemin_fichier, nom_colonne_1, nom_colonne_2, nom_colonne_id):
    tableau = pd.DataFrame(ouvrirUnFichier(chemin_fichier))
    colonne_1 =  list(tableau[nom_colonne_1])
    colonne_2 =  list(tableau[nom_colonne_2])
    colonne_id = list(tableau[nom_colonne_id])

    #On ordonne les listes de manière décroissante
    ord_col1 = ordrePopulation(colonne_1, colonne_id)
    ord_col2 = ordrePopulation(colonne_2, colonne_id)

    #On compare
    compar_1_2 = classementPays(ord_col1,ord_col2)

    #On trie la comparaison
    compar_1_2.sort()

    rangs_col_1 = []  #Initialisation 
    rangs_col_2 = [] 
    #Boucle : 
    for triplet in compar_1_2 :    #Pour chaque triplet,   
        rangs_col_1.append(triplet[0])        #Écriture du premier  élément dans "rang_pop_2007"
        rangs_col_2.append(triplet[1])    

    coeff_correl_spearman, p_value_spearman = scipy.stats.spearmanr(rangs_col_1,rangs_col_2)
    coeff_concord_kendall, p_value_kendall = scipy.stats.kendalltau(rangs_col_1,rangs_col_2)
    return (coeff_correl_spearman, p_value_spearman, coeff_concord_kendall, p_value_kendall)


valeurs = []
for annee in range(2007, 2026):
    chemin_fichier = "./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"
    nom_col_1 = "Pop " + str(annee)
    nom_col_2 = "Densité " +str(annee)
    rho, p_value_spearman, tau, p_value_kendall = calculCorrelationConcordance(chemin_fichier, nom_col_1, nom_col_2, "État")
    valeurs.append([annee, rho, p_value_spearman, tau, p_value_kendall])

print("ANNÉE \t Coeff_Correl_Spearman \t p-value_Spearman \t Coeff_Concord_Kendall \t p-value_Kendall")
for ligne in range(0, len(valeurs)):
    print(str(valeurs[ligne][0]) + "\t " +
          str(valeurs[ligne][1]) + "\t " +
          str(valeurs[ligne][2]) + "\t " +
          str(valeurs[ligne][3]) + "\t " +
          str(valeurs[ligne][4]))