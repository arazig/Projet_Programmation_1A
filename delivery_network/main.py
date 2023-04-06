from graph import Graph, graph_from_file
import time
from random import randint
import sys

sys.setrecursionlimit(5000000)
data_path = "input/"
file_name = "network.2.in"

g = graph_from_file(data_path + file_name)
print(g)

print(Graph.min_dist_dijkstra(g, 83, 642, 4656695))

"""
# Estimation du temps necessaire pour calculer la puissance minimale ( et le chemin associé) sur l'ensemble
# des trajets pour chacuns des fichier routes.x.in
def mean(L=[]):
    s=0
    for n in range(0,len(L)):
        s += n
    return s/len(L)

for x in range(1,5):
    data_path= "input/"
    g= graph_from_file_bis(data_path + 'network.0'+str(x)+'.in')
    Time=[]
    for _ in range(0,10):

        src = randint(1, g.nb_nodes)
        dest = randint(1, g.nb_nodes) 

        t0= time.perf_counter()
        Graph.min_power(g, src, dest)
        t1=time.perf_counter()

        t= t1 - t0
        print("Trajet : "+str(src)+ " ----> " + str(dest)+ "\n t = "+ str(t))
        Time.append(t)

    print("Le temps moyen d'execution de min_power est : "+str(mean(Time)))
    nbr_trajets = 1
    print("Approximation du temps necessaire pour l'ensemble des trajets est : "+ str(mean(Time)*nbr_trajets))
"""