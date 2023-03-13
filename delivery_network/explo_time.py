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
     

def time_explo(x):
    data_path = "input/"
    g = graph_from_file(data_path + 'network.'+str(x)+'.in')
    route_file = data_path + 'routes.'+ str(x) + '.in'

    with open(route_file, "r") as file:
        n = file.readline().split()
        n = int(n[0]) # numbers of trips
        lines =file.readlines() # c'est une liste de lignes ["1 2 3","2 3 5"]
        l_time = []
        for line in lines[0:5] :
            line = line.split()
            if len(line)==3 :
                src, dest, weight = map(float,line) # Choice of parameters

                t0 = time.perf_counter()
                Graph.min_power(g, src, dest)
                t1 = time.perf_counter()

                t = t1 - t0  # difference between the times before and after execution of the function
                l_time.append(t)
            else :
                    raise Exception("Incorrecte format")
        print(' INPUT => routes.'+str(x)+'.in, '+" The average time is : "+str(mean(l_time)+' secondes'))
        print(" Approximation of the time needed for all trips is: "+ str(mean(l_time)*n) + ' secondes, càd '+str(mean(l_time)*n/3600)+' heures.' \n')


for x in range(1,11):
    time_explo(x)
"""
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
"""
""" RESULT OF THE PROGRAM:
INPUT => routes.1.in,  The average time is : 0.0001272825989872217
Approximation of the time needed for all trips is: 0.0006364129949361086 secondes

INPUT => routes.2.in,  The average time is : 3.7666614988062066
Approximation of the time needed for all trips is: 18.833307494031033 secondes 

INPUT => routes.3.in,  The average time is : 23.87172478159773
Approximation of the time needed for all trips is: 119.35862390798866 secondes

INPUT => routes.4.in,  The average time is : 11.767614766198676
Approximation of the time needed for all trips is: 58.83807383099338 secondes 

INPUT => routes.5.in,  The average time is : 0.2704593005997594
Approximation of the time needed for all trips is: 1.3522965029987972 secondes

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