#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt
import math

#https://docs.scipy.org/doc/scipy/reference/stats.html


dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']


## 1 - VISUALISER DES DISTRIBUTIONS
## 1.A - Distributions statistiques de Variables DISCRETES

## Question 1.A.1 - Loi de Dirac
# Dirac = "Une seule issue est probable à 100%."
def distrib_dirac_discret(a, x_min, x_max):
    X = []
    P = []
    for i in range(x_min, x_max+1):
        X.append(i)
        if i == a:
            P.append(1.0)
        else :
            P.append(0.0)

    return X, P

# Paramètrage
a = 5
x_min = 1
x_max = 6

# On génère la distribution
X, P = distrib_dirac_discret(a, x_min, x_max)

# On visualise la distribution
plt.stem(X, P)
plt.title("Loi de Dirac centrée en a = {}".format(a))
plt.xlabel("x")
plt.xticks(X)
plt.ylabel("Pr(X = x)")
plt.ylim(0, 1.1)
plt.grid(True)
plt.savefig("./output/1_A_Distrib_Discretes/1_Dirac_discret.png")
plt.close()



## Question 1.A.2 - Loi Uniforme Discrète
# Uniforme : "Toutes les issues sont équiprobables."
def distrib_uniforme_discret(x_min, x_max):
    X = []
    P = []

    n = (x_max - x_min) + 1   # n = nombre de valeurs possibles
    for i in range(x_min, x_max+1):
        X.append(i)
        P.append(1/n)         # 1/n = probabilité pour chacune

    return X, P

# Paramètrage
x_min = 1
x_max = 20

# On génère la distribution
X, P = distrib_uniforme_discret(x_min, x_max)

# On visualise la distribution
plt.stem(X, P)
plt.title("Loi uniforme discrète sur l'intervalle [[{} ; {}]]".format(x_min, x_max))
plt.xlabel("x")
plt.xticks(X)
plt.ylabel("Pr(X = x)")
plt.ylim(0, 2*max(P))
plt.grid(True)
plt.savefig("./output/1_A_Distrib_Discretes/2_Uniforme_discret.png")
plt.close()





## Question 1.A.3 - Loi Binomiale
# Binomiale : "Je joue à pile ou face 57 fois, 
#              combien j'ai de chance de remporter au total:
#              0 manche? 1 manche? 2 manches? ... 57 manches?"
def distrib_binomiale_discret(n, p):
    K = []
    for k in range(0, n+1):
        K.append(k)

    P = scipy.stats.binom.pmf(K, n, p)

    return K, P

# Paramètrage
n = 20    # Nombre d'épreuves
p = 0.5   # Probabilité de succès à chacune (exemples = 1/6 pour qu'un dé fasse 1 ;
          #                                           = 1/2 pour gagner à pile ou face )

# On génère la distribution
K, P = distrib_binomiale_discret(n, p)

# On visualise la distribution
plt.stem(K, P)
plt.title("Loi binomiale (n = {}, p = {})".format(n, p))
plt.xlabel("k")
plt.xticks(K)
plt.ylabel("Pr(X = k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_A_Distrib_Discretes/3_Binomiale_discret.png")
plt.close()



## Question 1.A.4 - Loi de Poisson
# Poisson : "Même philosophie que Binomiale, mais quand événement rare."
#           Exemple : Hypothèse = il y a en moyenne 2 etoiles filantes chaque 5 min.
#                                                   |Donc lambda = 2.
#                     Maintenant on choisit dans la soirée une tranche de 5 min :
#                        Alors Poisson donne la probabilité qu'il y passe :
#                        0 comète / 1 comète / 2 comètes / ... / 14 980 comètes / ...
def distrib_poisson_discret(lam, n_max):
    K = []
    for k in range(0, n_max +1):
        K.append(k)

    P = scipy.stats.poisson.pmf(K, lam)

    return K, P

# Paramètrage
lam = 5     # Paramètre lambda
n_max = 20  # Valeur maximale

# On génère la distribution
K, P = distrib_poisson_discret(lam, n_max)

# On visualise la distribution
plt.stem(K, P)
plt.title("Loi de Poisson de paramètre lambda = {}.".format(lam))
plt.xlabel("k")
plt.xticks(K[::5])
plt.ylabel("Pr(X = k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_A_Distrib_Discretes/4_Poisson_discret.png")
plt.close()





## Question 1.A.5 - Loi de Zipf-Mandelbrot
# Zipf : "Dans un livre, si le mot le plus fréquent apparait 1000 fois,
#                alors le 2ème mot                  apparait 1000 / 2 fois,
#                   et le 3ème mot                  apparait 1000 / 3 fois,
#                              etc ...
#  
# Zipf-Mandelbrot : Généralisation en apportant des paramètres correctifs:
#                      s > 1  : exposant
#                      q >= 0 : décalage de Mandelbrot
#                      N      : taille maximale du support 
#                   De ces trois valeurs découle la costante de normalisation H qui vaut:
#                              1             1                       1
#                      H = ---------  +  ---------  +  (...)  +  ---------
#                          (1 + q)^s     (2 + q)^s               (N + q)^s
# 
# N.B.: Zipf-Mandelbrot se retrouve souvent en géographie !
#       Exemple : classement des populations des villes.
def distrib_zipf_mandelbrot(s, q, N):
    X = []
    P = []
    # Calcul de la constante de normalisation H
    H = 0
    for i in range(0, N+1):
        H += 1.0 / ((i + q)**s)
    # Fin du calcul de H

    for i in range(0, N+1):
        X.append(i)
        P.append(1.0 / (H * ((i + q)**s)))

    return X, P

# Paramètrage
s = 1.5  # Exposant (doit être > 1)
q = 2    # Décalage de Mandelbrot (doit être >= 0)
N = 50   # Taille maximale du support

# On génère la distribution
X, P = distrib_zipf_mandelbrot(s, q, N)

# On visualise la distribution
plt.stem(X, P)
plt.title("Loi de Zipf-Mandelbrot avec (s = {}; q = {}; N = {})".format(s,q,N))
plt.xlabel("x")
plt.ylabel("P(X = x)")
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.savefig("./output/1_A_Distrib_Discretes/5_Zipf_Mandelbrot_discret.png")
plt.close()





## 1.B - Distributions statistiques de Variables CONTINUES
## Question 1.B.1 - Loi de Poisson
def distrib_poisson_continu(mu, n_max, finesse):
    K_cont = np.linspace(0, n_max, finesse)
    P_cont = []
    for i in range(0, len(K_cont)):
        k = K_cont[i]
        pr_k = math.exp(-mu) * (mu**k) / (math.gamma(k+1))
        P_cont.append(pr_k)

    return K_cont, P_cont

# Paramètrage
mu = 5         # Paramètre mu
n_max = 20     # Valeur maximale
finesse = 500  # nombre de points

# On génère la distribution
K_cont, P_cont = distrib_poisson_continu(mu, n_max, finesse)

# On visualise la distribution - CLASSIQUEMENT
plt.plot(K_cont, P_cont)
plt.title("Loi de Poisson continue de paramètre mu = {}.".format(mu))
plt.xlabel("k")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/1_Poisson_continu.png")
plt.close()

# On visualise la distribution - REMPLIE
plt.plot(K_cont, P_cont)
plt.fill_between(K_cont, P_cont, alpha=0.3)
plt.title("Loi de Poisson continue de paramètre mu = {}.".format(mu))
plt.xlabel("k")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/1_Poisson_continu_remplie.png")
plt.close()


## Question 1.B.2 - Loi Normale
# Loi Normale : "La fameuse Gaussienne"
#                ... centrée en la valeur mu
#                ... s'étend de - infini à + infini
#                ... mais 99.7% se trouvent entre mu - 3 sigma 
#                                              et mu + 3 sigma
def distrib_normale_continu(mu, sigma, facteur_sigma = 3, finesse = 500):
    K_cont = np.linspace(mu - facteur_sigma*sigma, mu + facteur_sigma*sigma, finesse) # la largeur de l'intervalle est fixée ici
    P_cont = scipy.stats.norm.pdf(K_cont, mu, sigma)

    return K_cont, P_cont

# Paramètrage
mu = 5             # Paramètre mu, valeur centrale
sigma = 20         # Paramètre sigma, impliquant la largeur
facteur_sigma = 3  # Quelle largeur représentée
finesse = 500      # nombre de points

# On génère la distribution
K_cont, P_cont = distrib_normale_continu(mu, sigma, facteur_sigma, finesse)

# On visualise la distribution - CLASSIQUEMENT
plt.plot(K_cont, P_cont)
plt.title("Loi Normale centrée en mu = {}, de largeur {}*sigma (sigma = {})."
          .format(mu, 2*facteur_sigma, sigma))
plt.xlabel("k")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/2_Normale_continu.png")
plt.close()

# On visualise la distribution - REMPLIE
plt.plot(K_cont, P_cont)
plt.fill_between(K_cont, P_cont, alpha=0.3)
plt.title("Loi Normale centrée en mu = {}, de largeur {}*sigma (avec sigma = {})."
          .format(mu, 2*facteur_sigma, sigma))
plt.xlabel("k")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/2_Normale_continu_remplie.png")
plt.close()




## Question 1.B.3 - Loi Log-normale
def distrib_normale_continu(mu, sigma, n_max, finesse = 500):
    K_cont = np.linspace(0.001, n_max, finesse) 
    P_cont = scipy.stats.lognorm.pdf(K_cont, s=sigma, scale=np.exp(mu))

    return K_cont, P_cont

# Paramètrage
mu = 1             # Paramètre mu
sigma = 0.5        # Paramètre sigma
n_max = 20         # valeur maximale
finesse = 500      # nombre de points

# On génère la distribution
K_cont, P_cont = distrib_normale_continu(mu, sigma, n_max, finesse)

# On visualise la distribution - CLASSIQUEMENT
plt.plot(K_cont, P_cont)
plt.title("Loi Log-normale (avec mu = {}; sigma = {})".format(mu, sigma))
plt.xlabel("k")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/3_Log_normale_continu.png")
plt.close()

# On visualise la distribution - REMPLIE
plt.plot(K_cont, P_cont)
plt.fill_between(K_cont, P_cont, alpha=0.3)
plt.title("Loi Log-normale (avec mu = {}; sigma = {})".format(mu, sigma))
plt.xlabel("k")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/3_Log-normale_continu_remplie.png")
plt.close()




## Question 1.B.4 - Loi Uniforme
def distrib_uniforme_continu(x_min, a, b, x_max, finesse = 500):
    K_cont = np.linspace(x_min, x_max, finesse)
    P_cont = scipy.stats.uniform.pdf(K_cont, loc=a, scale=b-a)

    return K_cont, P_cont

# Paramètrage
x_min = -10    # borne sup de la fenêtre
a     = -2     # borne inférieure
b     =  8     # borne supérieure
x_max = 10     # borne sup de la fenêtre
finesse = 500  # nombre de points

# On génère la distribution
K_cont, P_cont = distrib_uniforme_continu(x_min, a, b, x_max, finesse)

# On visualise la distribution - CLASSIQUEMENT
plt.plot(K_cont, P_cont)
plt.title("Loi uniforme de bornes [a ; b] = [{} ; {}]".format(a,b))
plt.xlabel("x")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/4_Uniforme_continu.png")
plt.close()

# On visualise la distribution - REMPLIE
plt.plot(K_cont, P_cont)
plt.fill_between(K_cont, P_cont, alpha=0.3)
plt.title("Loi uniforme de bornes [a ; b] = [{} ; {}]".format(a,b))
plt.xlabel("k")
plt.ylabel("Pr(k)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/4_Uniforme_continu_remplie.png")
plt.close()




## Question 1.B.5 - Loi du Chi²
def distrib_chi2_continu(k, n_max, finesse = 500):
    K_cont = np.linspace(0.001, n_max, finesse)
    P_cont = scipy.stats.chi2.pdf(K_cont, df=k)

    return K_cont, P_cont

# Paramètrage
k = 5          # Paramètre k
n_max = 50    # Valeur maximale
finesse = 500  # nombre de points

# On génère la distribution
K_cont, P_cont = distrib_chi2_continu(k, n_max, finesse)

# On visualise la distribution - CLASSIQUEMENT
plt.plot(K_cont, P_cont)
plt.title("Loi du chi² pour k = {}".format(k))
plt.xlabel("Valeur de la statistique χ²")
plt.ylabel("Densité de probabilité f(x)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/5_Chi2_continu.png")
plt.close()

# On visualise la distribution - REMPLIE
plt.plot(K_cont, P_cont)
plt.fill_between(K_cont, P_cont, alpha=0.3)
plt.title("Loi du chi² pour k = {}".format(k))
plt.xlabel("Valeur de la statistique χ²")
plt.ylabel("Densité de probabilité f(x)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/5_Chi2_continu_remplie.png")
plt.close()



## Question 1.B.6 - Loi de Pareto
def distrib_pareto_continu(alpha, x_m, n_max, finesse = 500):
    K_cont = np.linspace(x_m, n_max, finesse)
    P_cont = scipy.stats.pareto.pdf(K_cont, b=alpha, scale=x_m)

    return K_cont, P_cont


# paramètres
alpha = 1      # shape
x_m = 1          # x_m
n_max = 20
finesse = 500  # nombre de points

# On génère la distribution
K_cont, P_cont = distrib_pareto_continu(alpha, x_m, n_max, finesse)

# On visualise la distribution - CLASSIQUEMENT
plt.plot(K_cont, P_cont)
plt.title("Loi de Pareto (avec x_m = {}, alpha = {})".format(x_m, alpha))
plt.xlabel("x")
plt.ylabel("Densité de probabilité f(x)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/6_Pareto_continu.png")
plt.close()

# On visualise la distribution - REMPLIE
plt.plot(K_cont, P_cont)
plt.fill_between(K_cont, P_cont, alpha=0.3)
plt.title("Loi de Pareto (avec x_m = {}, alpha = {})".format(x_m, alpha))
plt.xlabel("x")
plt.ylabel("Densité de probabilité f(x)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("./output/1_B_Distrib_Continues/6_Pareto_continu_remplie.png")
plt.close()

## 2 - CALCUL MOYENNE ET ECART-TYPE
# Définition des fonctions

# Test des fonctions