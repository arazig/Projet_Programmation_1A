"""
##################################

# This python file is used to estimate the time needed to 
# calculate (using the code developed using kruskal algo) the minimum
# power (and the associated path) over all the paths for each of the given routes.x.in files.

RESULTS : It can be seen that compared to the execution times of the first approach to find the minimum power,
 the times are much lower.
 Indeed, whereas it took several days in the first instance, it now only takes about a minute to complete.
 This is much more reasonable.

##################################
"""

# Importation :
from graph import Graph, graph_from_file, kruskal, oriented_tree_construction, tree_min_power
import time
from random import randint
import sys
sys.setrecursionlimit(5000000)


def mean(L):
    """ return the average value of a list"""
    return sum(L)/len(L)


def time2_explo(x):
    """
    x index of teh file in the format network.x.in and routes.x.in
    """
    data_path = "input/"
    g = graph_from_file(data_path + 'network.'+str(x)+'.in')
    or_tree = oriented_tree_construction(kruskal(g))
    route_file = data_path + 'routes.'+ str(x) + '.in'

    with open(route_file, "r") as file:
        n = file.readline().split()
        n = int(n[0]) # numbers of trips
        lines =file.readlines() # c'est une liste de lignes ["1 2 3","2 3 5"]
        l_time = []
        for line in lines[0::] :
            line = line.split()
            if len(line)==3 :
                src, dest, weight = map(float,line) # Choice of parameters

                t0 = time.perf_counter()
                tree_min_power(or_tree, src, dest)
                t1 = time.perf_counter()

                t = t1 - t0  # difference between the times before and after execution of the function
                l_time.append(t)
            else :
                    raise Exception("Incorrecte format")

        print(' INPUT => routes.' + str(x) + '.in, ' + " The average trip time is : " + str(mean(l_time)) + ' sec')
        print(" Time needed for all trips is: "+ str(sum(l_time)) + ' sec, càd '+str(sum(l_time)/3600)+' h. \n')


for x in range(1,11):
    time2_explo(x)


""" OUTPUT :

INPUT => routes.1.in,  The average trip time is : 8.045465386073505e-06 sec
 Time needed for all trips is: 0.0011263651540502906 sec, càd 3.1287920945841404e-07 h. 

 INPUT => routes.2.in,  The average trip time is : 2.0967763451335487e-05 sec
 Time needed for all trips is: 2.0967763451335486 sec, càd 0.0005824378736482079 h. 

 INPUT => routes.3.in,  The average trip time is : 0.00020931276324915235 sec
 Time needed for all trips is: 104.65638162457617 sec, càd 0.029071217117937826 h. 

 INPUT => routes.4.in,  The average trip time is : 0.00026685581363894743 sec
 Time needed for all trips is: 133.42790681947372 sec, càd 0.03706330744985381 h. 

 INPUT => routes.5.in,  The average trip time is : 0.00017365322453610134 sec
 Time needed for all trips is: 17.365322453610133 sec, càd 0.004823700681558371 h. 

 INPUT => routes.6.in,  The average trip time is : 0.0002107499095913372 sec
 Time needed for all trips is: 105.3749547956686 sec, càd 0.02927082077657461 h. 

 INPUT => routes.7.in,  The average trip time is : 0.00024121082643215776 sec
 Time needed for all trips is: 120.60541321607889 sec, càd 0.033501503671133026 h. 

 INPUT => routes.8.in,  The average trip time is : 0.00017664925487380242 sec
 Time needed for all trips is: 88.32462743690121 sec, càd 0.02453461873247256 h. 

 INPUT => routes.9.in,  The average trip time is : 0.00021742960970912826 sec
 Time needed for all trips is: 108.71480485456414 sec, càd 0.030198556904045593 h. 

 INPUT => routes.10.in,  The average trip time is : 0.00032992032028280666 sec
 Time needed for all trips is: 164.96016014140332 sec, càd 0.045822266705945365 h.

"""