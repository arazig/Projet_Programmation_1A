"""
 L' approche théorique la plus instinctive est dans un premier temps de trier les trajets du fichiers
 route par profit décroissant. Ensuite on parcours chcuns des trajets en lui associant le camion qui coute le moins 
 chere ayant la puissnace minimale requise. On effectue cette opération jusqu'a épuisement du budget ( ie somme des couts > B)
"""

# Importation :
from graph import Graph, graph_from_file, kruskal, oriented_tree_construction, tree_min_power
import time
from random import randint
import sys
sys.setrecursionlimit(5000000)



############################################################################
#######  2nd METHODE : Une sollution optimale du problème  (dynamique)  ####
############################################################################

# Tout d'abord, on recupere l'utilité max que peut generer chaque camion du catalogue

def Truck(x, catalogue):
    """
    Cette fonction nous permet d'associer a chaque camion du catalogue l'utilité maximale 
    qu'il peur engendrer sur l'intégralité des trajets d'un fichier route 
    args : 
        x(int): indice du fichier routes.x.in (de 1 à 10)
        catalogue(int): indice du catalogue de camion ( 0, 1 ou 2)
    output :
        Trucks(list) : liste de tous les camions du catalogue avec l'utilité maximal que chacun engendre
    """
    # recupération des fichiers 
    route_file = 'input/routes.' + str(x) + '.in'
    powermin_file = 'input/powermin.' + str(x) + '.in'
    trucks_file = 'input/trucks.' + str(catalogue) + '.in'

    Selection = [] 
    # Ouverture des fichier et stockage des valeurs dans des listes
    Trajets = []
    with open(route_file, "r") as route :
        with open(powermin_file, "r") as power :
            n = int(route.readline())
            for _ in range(n):

                src, dest, utility = map(int, route.readline().split())
                pwr = int(power.readline())
                Trajets.append((src, dest, utility, pwr)) 
                #  il est aussi possible de calculer directement pwr a chaque itération sans passer par lecture des fichier powermin

    Trucks = []      
    with open(trucks_file, "r") as trucks :   
        nb_trucks = trucks.readline()
        for _ in range(int(nb_trucks)) :
            pow, cost = map(int, trucks.readline().split())
            umax = 0
            for trj in Trajets :
                # si la puissance du c&mion est suffisante et que l'utilité est meilleure on actualise l'utilité max
                if pow >= trj[3] and umax < trj[2] : 
                    umax = trj[2]
            # on associe à chaque camion l'utilité max qu'il peut rapporter         
            Trucks.append((pow, cost, umax)) 
    return Trucks

#print(Truck(6,1))



def opti(x, catalogue, Budget):
    '''
    On utilise un algorithme de type sac à dos où la capacité du sac est donnée par le budget B et les éléments à ranger 
    dans le sac à dos sont les camions en fonction de leurs prix.
    
    Cette fonction permet d'effecteur une selection optimale de camion qui va permetre de maximiser 
    l'utilité sous contrainte de budget. On se concentre sur le réseau d'indice x. 
    args :
        x(int)        > indice du réseau
        Budget(float) > budget disponible
        Catalogue(int)> indice du catalogue de camion ( 0, 1 ou 2)
    output :
        Selection(list)  > liste de la selection de camion proposée
    '''
    Trucks = Truck(x,catalogue)
    matrice = [[0 for x in range (int(Budget + 1))] for x in range(int(len(Trucks)+1))] 
    # on ajoute des deux cotés 1 pour pouvoir représenter le cas où le budget est nul et celui où il n'y a aucun camion sélectionné
    #print(Trucks[0:8])
    
    for i in range(1, len(Trucks) + 1): 
        # on prend l'indice d'un camion
        for w in range(1, Budget + 1): 
            # on va regarder pour chaque discretisation de notre budget
            if Trucks[i-1][1] <= w:  
                # si le prix du camion est inférieur au budget à cette étape on peut ajouter le camion au catalogue
                matrice[i][w] = max(Trucks[i-1][2] + matrice[i-1][w-Trucks[i-1][1]], matrice[i-1][w])
                # on prend le max entre l'utilité de la ligne prédédente de la matrice pour le meme budget et l'utilité
                # du camion choisi auquel on ajoute la solution optimisé pour le budget correspondant au bugdet actuel moins le prix du camion
            else:
                # sinon quand on ne peut pas acheter le camion on se contente de la sélection faite précedemment pour le budget courant 
                matrice[i][w] = matrice[i-1][w]

    # on va maintenant remonter la matrice afin de trouver la solution optimale du problème i.e la selection optimale de camions ainsi que la flotte de camions sélectionnées
    w = Budget
    n = len(Trucks)
    elements_selection = []
    #print(matrice)
    
    while w >= 0 and n >= 0:
        # on parcours la matrice tant que le budget n'est pas épuisé ou tant que les camions sélectionnés n'ont pas tous été 
        # parcouru en commençant par le dernier élément de la matrice (en bas à droite) correspondant à la sélection optimale
        e = Trucks[n-1]
        if w-e[1] >= 0 : 
            if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
                # on regarde si l'utilité courante ne serait pas la somme des utilités 
                # du camion sélectionné et de celle obtenu quand le budget est la différence entre
                # le budget actuel et le prix du camion 
                elements_selection.append(e)
                w -= e[1]

            n -= 1
        
    return matrice[-1][-1], elements_selection


