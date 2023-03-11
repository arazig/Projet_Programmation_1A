# This python file is used to estimate the time needed to 
# calculate (using the code developed in Graph.py) the minimum
# power (and the associated path) over all the paths for each of the given routes.x.in files.

from graph import Graph, graph_from_file, graph_from_file_Routes
import time
from random import randint
import sys
sys.setrecursionlimit(5000000)

def mean(L=[]):
    """ return the average value of a list"""
    s=0
    for n in range(0,len(L)):
        s += n
    return s/len(L)


#/!\ only for graphs of files in the format network.0x.in :
# print("There is a path that connects the two nodes !") if Graph.possible_path(g,src,dest) == True else  print("No path possible")
     

for x in range(1,11):
    data_path= "input/"
    g= graph_from_file_Routes(data_path + 'routes.'+str(x)+'.in')
    Time=[]
    for _ in range(0,10):
        # Choice of parameters :
        src = randint(1, g.nb_nodes)
        dest = randint(1, g.nb_nodes) 

        t0= time.perf_counter()
        Graph.min_power(g, src, dest)
        t1=time.perf_counter()

        t= t1 - t0
        print("Trajet : "+str(src)+ " ----> " + str(dest)+ "\n t = "+ str(t))
        Time.append(t)

    print(' INPUT : routes.'+str(x)+'.in '+"Le temps moyen d'execution de min_power est : "+str(mean(Time)))
    nbr_trajets = 1
    print("Approximation du temps necessaire pour l'ensemble des trajets est : "+ str(mean(Time)*nbr_trajets))
