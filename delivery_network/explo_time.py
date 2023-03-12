# This python file is used to estimate the time needed to 
# calculate (using the code developed in Graph.py) the minimum
# power (and the associated path) over all the paths for each of the given routes.x.in files.

from graph import Graph, graph_from_file, graph_from_file_Routes
import time
from random import randint
import sys
sys.setrecursionlimit(5000000)

def mean(L):
    """ return the average value of a list"""
    return sum(L)/len(L)


# /!\ only for graphs of files in the format network.0x.in :
# print("There is a path that connects the two nodes !") if Graph.possible_path(g,src,dest) == True else  print("No path possible")
     

for x in range(1,11):
    data_path = "input/"
    g = graph_from_file_Routes(data_path + 'routes.'+str(x)+'.in')
    l_time = []
    nbr_trajets = 5
    for _ in range(0,nbr_trajets):
        # Choice of parameters :
        src = randint(1, g.nb_nodes)
        dest = randint(1, g.nb_nodes)

        t0 = time.perf_counter()
        Graph.min_power(g, src, dest)
        t1 = time.perf_counter()

        t = t1 - t0  # difference between the times before and after execution of the function
        l_time.append(t)

    print(' INPUT => routes.'+str(x)+'.in, '+" The average time is : "+str(mean(l_time)))
    print(" Approximation of the time needed for all trips is: "+ str(mean(l_time)*nbr_trajets) + ' secondes \n')

""" RESULT OF THE PROGRAMME :

INPUT => routes.6.in,  The average time is : 38.711043321405306
 Approximation of the time needed for all trips is: 193.55521660702652 secondes 

 INPUT => routes.7.in,  The average time is : 17.713787204399704
 Approximation of the time needed for all trips is: 88.56893602199852 secondes 

 INPUT => routes.8.in,  The average time is : 24.75009866579785
 Approximation of the time needed for all trips is: 123.75049332898925 secondes 

 INPUT => routes.9.in,  The average time is : 6.035689906193875
 Approximation of the time needed for all trips is: 30.178449530969374 secondes 

 INPUT => routes.10.in,  The average time is : 42.48826046480099
 Approximation of the time needed for all trips is: 212.44130232400494 secondes 
"""