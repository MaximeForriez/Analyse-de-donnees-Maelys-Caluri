#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

# Fonctions locales
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def calculerMoyenneDeListe(liste):
    # cette fonction calcule la moyenne d'une liste
    somme = 0
    for i in range(len(liste)): # d'abord on somme tous les éléments de la liste
        somme += liste[i]
    moyenne = somme / len(liste) # puis on divise la somme par le nombre d'éléments
    return moyenne

def testerHypothesesFormuleIntervalleFluctuation(n, p):
    # cette fonction vérifie si les paramètres n et p remplissent les trois conditions nécessaires 
    # pour que l'on puisse appliquer la formule de l'intervalle de fluctuation.
    if n >= 30:
        if n*p >= 5:
            if n*(1-p) >= 5:
                return True
    else:
        return False
    
def calculerIntervalleFluctuation(n, p, z_c):
    intervalle = [p - z_c*((math.sqrt(p*(1-p))) / (math.sqrt(n))),  p + z_c*((math.sqrt(p*(1-p))) / (math.sqrt(n)))]
    return intervalle

def calculerIntervalleConfiance(n, f, z_c):
    intervalle = [f - z_c*((math.sqrt(f*(1-f))) / (math.sqrt(n))),  f + z_c*((math.sqrt(f*(1-f))) / (math.sqrt(n)))]
    return intervalle

# 1 - Théorie de l'échantillonnage (intervalles de fluctuation)
# L'échantillonnage se base sur la répétitivité.
print("Résultat sur le calcul d'un intervalle de fluctuation")

donnees = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv"))

# 1.1 Calcul des moyennes
liste_pour = donnees["Pour"]
liste_cont = donnees["Contre"]
liste_sans = donnees["Sans opinion"]

moy_pour = round(calculerMoyenneDeListe(liste_pour))
moy_cont = round(calculerMoyenneDeListe(liste_cont))
moy_sans = round(calculerMoyenneDeListe(liste_sans))

print("moy_pour = ", moy_pour)
print("moy_cont = ", moy_cont)
print("moy_sans = ", moy_sans)



# 1.2 Calcul des fréquences
# Pour les moyennes obtenues
somme_moyennes_obtenues = moy_pour + moy_cont + moy_sans

freq_pour = round(moy_pour / somme_moyennes_obtenues, 3)
freq_cont = round(moy_cont / somme_moyennes_obtenues, 3)
freq_sans = round(moy_sans / somme_moyennes_obtenues, 3)

print("freq_pour = ", freq_pour)
print("freq_cont = ", freq_cont)
print("freq_sans = ", freq_sans)

# Pour la population mère
somme_moyennes_mere = 852 + 911 + 422

freq_pour_mere = round(852 / somme_moyennes_mere, 3)
freq_cont_mere = round(911 / somme_moyennes_mere, 3)
freq_sans_mere = round(422 / somme_moyennes_mere, 3)

print("freq_pour_mere = ", freq_pour_mere)
print("freq_cont_mere = ", freq_cont_mere)
print("freq_sans_mere = ", freq_sans_mere)



# 1.3 Calcul de l'intervalle de fluctuation 
n = 100
z_c = 1.96
# Pour la catégorie "Pour"
p_pour = 852 / 2185
if testerHypothesesFormuleIntervalleFluctuation(n, p_pour):
    inter_fluc_pour = calculerIntervalleFluctuation(n, p_pour, z_c)

print("inter_fluc_pour = ", inter_fluc_pour)

# Pour la catégorie "Contre"
p_cont = 911 / 2185
if testerHypothesesFormuleIntervalleFluctuation(n, p_cont):
    inter_fluc_cont = calculerIntervalleFluctuation(n, p_cont, z_c)

print("inter_fluc_cont = ", inter_fluc_cont)

# Pour la catégorie "Sans opinion"
p_sans = 422 / 2185
if testerHypothesesFormuleIntervalleFluctuation(n, p_sans):
    inter_fluc_sans = calculerIntervalleFluctuation(n, p_sans, z_c)

print("inter_fluc_sans = ", inter_fluc_sans)

# 1.4 Explication lien
# Lien entre ...



# On en conclut que
# Comme les 3 valeurs de fréquences sont comprises dans les intervalles de fluctuation, alors
# avec 95% de chances d'avoir raison, on peut affirmer que l'échantillon est représentatif de la population totale.




# 2 - Théorie de l'estimation (intervalles de confiance)
# L'estimation se base sur l'effectif.
print("Résultat sur le calcul d'un intervalle de confiance")

# 2.1 Extraire le premier échantillon
echant_un = list(donnees.iloc[0])
print("echant_un =", echant_un)

# 2.2 Calcul des fréquences de l'échantillon isolé
effectif_tot = sum(echant_un)

freq_pour_isole = echant_un[0]/effectif_tot
freq_cont_isole = echant_un[1]/effectif_tot
freq_sans_isole = echant_un[2]/effectif_tot

print("freq_pour_isole = ", freq_pour_isole)
print("freq_cont_isole = ", freq_cont_isole)
print("freq_sans_isole = ", freq_sans_isole)

# 2.3 Calcul des intervalles de confiance
inter_conf_pour = calculerIntervalleConfiance(effectif_tot, freq_pour_isole, z_c)
inter_conf_cont = calculerIntervalleConfiance(effectif_tot, freq_cont_isole, z_c)
inter_conf_sans = calculerIntervalleConfiance(effectif_tot, freq_sans_isole, z_c)

print("inter_conf_pour = ", inter_conf_pour)
print("inter_conf_cont = ", inter_conf_cont)
print("inter_conf_sans = ", inter_conf_sans)


# 3 - Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
print("Théorie de la décision")