# This python file is used to estimate the time needed to 
# calculate (using the code developed in Graph.py) the minimum
# power (and the associated path) over all the paths for each of the given routes.x.in files.

from graph import Graph, graph_from_file
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
    """
    x index of teh file in the format network.x.in and routes.x.in
    """
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
        print(' INPUT => routes.' + str(x) + '.in, ' + " The average time is : " + str(mean(l_time)) + ' secondes')
        print(" Approximation of the time needed for all trips is: "+ str(mean(l_time)*n) + ' secondes, càd '+str(mean(l_time)*n/3600)+' heures. \n')


for x in range(10,11):
    time_explo(x)

""" RESULT OF THE PROGRAM:
 INPUT => routes.1.in,  The average time is : 0.0005744263995438814 secondes
 Approximation of the time needed for all trips is: 0.0804196959361434 secondes, càd 2.23388044267065e-05 heures. 

 INPUT => routes.2.in,  The average time is : 3.509813237603521 secondes
 Approximation of the time needed for all trips is: 350981.3237603521 secondes, càd 97.49481215565336 heures. 

 INPUT => routes.3.in,  The average time is : 8.231395321595482 secondes
 Approximation of the time needed for all trips is: 4115697.660797741 secondes, càd 1143.2493502215946 heures. 

 INPUT => routes.4.in,  The average time is : 17.89923995300196 secondes
 Approximation of the time needed for all trips is: 8949619.97650098 secondes, càd 2486.00554902805 heures. 

 INPUT => routes.5.in,  The average time is : 26.270301272196228 secondes
 Approximation of the time needed for all trips is: 2627030.127219623 secondes, càd 729.7305908943397 heures. 

 INPUT => routes.6.in,  The average time is : 21.715683386602905 secondes
 Approximation of the time needed for all trips is: 10857841.693301452 secondes, càd 3016.067137028181 heures. 

 INPUT => routes.7.in,  The average time is : 24.826700999808963 secondes
 Approximation of the time needed for all trips is: 12413350.499904482 secondes, càd 3448.1529166401338 heures. 

 INPUT => routes.8.in,  The average time is : 16.14622365120449 secondes
 Approximation of the time needed for all trips is: 8073111.8256022455 secondes, càd 2242.5310626672904 heures. 

 INPUT => routes.9.in,  The average time is : 17.577709830593086 secondes
 Approximation of the time needed for all trips is: 8788854.915296543 secondes, càd 2441.348587582373 heures. 

(base) MacBook-Air-de-Amine:Projet_Programmation_1A aminerazig$ 
 Approximation of the time needed for all trips is: 8616705.526804434 secondes, càd 2393.529313001232 heures.
"""