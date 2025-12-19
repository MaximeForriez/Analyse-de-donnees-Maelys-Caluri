#coding:utf8

import pandas as pd
import math
import scipy
import matplotlib.pyplot as plt
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
print("\033[94m\n 1 - Théorie de l'échantillonnage")
print(" Résultat sur le calcul d'un intervalle de fluctuation")

donnees = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv"))

# 1.1 Calcul des moyennes
liste_pour = donnees["Pour"]
liste_cont = donnees["Contre"]
liste_sans = donnees["Sans opinion"]

moy_pour = round(calculerMoyenneDeListe(liste_pour))
moy_cont = round(calculerMoyenneDeListe(liste_cont))
moy_sans = round(calculerMoyenneDeListe(liste_sans))

print("\nVoici les 3 moyennes obtenues")
print("Moyenne de Pour = ", moy_pour)
print("Moyenne de Contre = ", moy_cont)
print("Moyenne de Sans opinion = ", moy_sans)



# 1.2 Calcul des fréquences
# Pour les moyennes obtenues
somme_moyennes_obtenues = moy_pour + moy_cont + moy_sans

freq_pour = round(moy_pour / somme_moyennes_obtenues, 3)
freq_cont = round(moy_cont / somme_moyennes_obtenues, 3)
freq_sans = round(moy_sans / somme_moyennes_obtenues, 3)

print("\n Voici les 3 fréquences obtenues")
print("Fréquence de Pour = ", freq_pour)
print("Fréquence de Contre = ", freq_cont)
print("Fréquence de Sans opinion = ", freq_sans)

# Pour la population mère
somme_moyennes_mere = 852 + 911 + 422

freq_pour_mere = round(852 / somme_moyennes_mere, 3)
freq_cont_mere = round(911 / somme_moyennes_mere, 3)
freq_sans_mere = round(422 / somme_moyennes_mere, 3)

print("\n Voici les 3 fréquences de la population mère")
print("Freq_mere Pour = ", freq_pour_mere)
print("Freq_mere Contre= ", freq_cont_mere)
print("Freq_mere Sans Opinion= ", freq_sans_mere)



# 1.3 Calcul de l'intervalle de fluctuation 
print("\n Voici les 3 intervalles de fluctuation")
n = 100
z_c = 1.96
# Pour la catégorie "Pour"
p_pour = 852 / 2185
if testerHypothesesFormuleIntervalleFluctuation(n, p_pour):
    inter_fluc_pour = calculerIntervalleFluctuation(n, p_pour, z_c)

print("Inter_fluc Pour = ", inter_fluc_pour)

# Pour la catégorie "Contre"
p_cont = 911 / 2185
if testerHypothesesFormuleIntervalleFluctuation(n, p_cont):
    inter_fluc_cont = calculerIntervalleFluctuation(n, p_cont, z_c)

print("Inter_fluc Contre = ", inter_fluc_cont)

# Pour la catégorie "Sans opinion"
p_sans = 422 / 2185
if testerHypothesesFormuleIntervalleFluctuation(n, p_sans):
    inter_fluc_sans = calculerIntervalleFluctuation(n, p_sans, z_c)

print("Inter_fluc Sans Opinion= ", inter_fluc_sans)

# 1.4 Explication lien
# Lien entre ...



# On en conclut que
# Comme les 3 valeurs de fréquences sont comprises dans les intervalles de fluctuation, alors
# avec 95% de chances d'avoir raison, on peut affirmer que l'échantillon est représentatif de la population totale.




# 2 - Théorie de l'estimation (intervalles de confiance)
# L'estimation se base sur l'effectif.
print("\033[93m\n 2 - Théorie de l'estimation")
print("Résultat sur le calcul d'un intervalle de confiance")

# 2.1 Extraire le premier échantillon
echant_un = list(donnees.iloc[0])
print("\n Voici le 1er échantillon")
print("Echantillon 1 =", echant_un)

# 2.2 Calcul des fréquences de l'échantillon isolé
effectif_tot = sum(echant_un)

freq_pour_isole = echant_un[0]/effectif_tot
freq_cont_isole = echant_un[1]/effectif_tot
freq_sans_isole = echant_un[2]/effectif_tot

print("\n Voici les 3 fréquences de l'échantillon isolé")
print("Freq_isole Pour= ", freq_pour_isole)
print("Freq_isole Contre= ", freq_cont_isole)
print("Freq_isole Sans opinion= ", freq_sans_isole)

# 2.3 Calcul des intervalles de confiance
inter_conf_pour = calculerIntervalleConfiance(effectif_tot, freq_pour_isole, z_c)
inter_conf_cont = calculerIntervalleConfiance(effectif_tot, freq_cont_isole, z_c)
inter_conf_sans = calculerIntervalleConfiance(effectif_tot, freq_sans_isole, z_c)

print("\n Voici les 3 intervalles de confiance")
print("Inter_conf Pour = ", inter_conf_pour)
print("Inter_conf Cont = ", inter_conf_cont)
print("Inter_conf Sans = ", inter_conf_sans)

# 2.4 Interprétation
# L'intervalle de confiance est plus mince, donc plus retreint, que l'intervalle de fluctuation



# 3 - Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
print("\033[94m\n 3 - Théorie de la décision")
print("Théorie de la décision")

donnees_1 = pd.DataFrame(ouvrirUnFichier("./data/Loi-normale-Test-1.csv"))
donnees_2 = pd.DataFrame(ouvrirUnFichier("./data/Loi-normale-Test-2.csv"))

test_1 = list(donnees_1["Test"])
test_2 = list(donnees_2["Test"])

stat_1, p_value_1 = scipy.stats.shapiro(test_1)
stat_2, p_value_2 = scipy.stats.shapiro(test_2)

print("\n Voici les résultats du test de Shapiro")
print("Test 1 : stat_1 = ", stat_1, ",  p_value_1 = ", p_value_1)
print("Test 2 : stat_2 = ", stat_2, ",  p_value_2 = ", p_value_2)

print("\033[0m\n")

# Bonus
# On génère les graphes pour appuyer notre décision
borne_inf = min(test_1)
borne_sup = max(test_1)
X = []
Y = []
for i in range(borne_inf, borne_sup+1):
    X.append(i)
    Y.append(0)

for j in range(len(test_1)):
    Y[test_1[j]-borne_inf] += 1

plt.stem(X, Y)
plt.title("Test 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/test_1.png")
plt.close()


borne_inf = min(test_2)
borne_sup = max(test_2)
X = []
Y = []
for i in range(borne_inf, borne_sup+1):
    X.append(i)
    Y.append(0)

for j in range(len(test_2)):
    Y[test_2[j]-borne_inf] += 1

plt.stem(X, Y)
plt.title("Test 2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/test_2.png")
plt.close()
