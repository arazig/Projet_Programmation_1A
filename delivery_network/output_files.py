##################################
# This python file is used to create output.x.out files from the routes.x.in files.
# Format : for each routes.x.in file, a routes.x.out file contains T lines with a single 
# number on each line corresponding to the minimum power to cover the path.
##################################

# Importation :
from graph import Graph, graph_from_file, kruskal, oriented_tree_construction, tree_min_power
import time
from random import randint
import sys
sys.setrecursionlimit(5000000)


directory_path_out = "/Users/aminerazig/Desktop/ENSAE 1A/INFO/Projet_Programmation_1A/output/"
directory_path_in = "/Users/aminerazig/Desktop/ENSAE 1A/INFO/Projet_Programmation_1A/input/"

x=10  # for each routes file
output_file = "routes." + str(x)
input_file = "network." + str(x)

g = graph_from_file((directory_path_in + input_file + ".in"))
or_tree = oriented_tree_construction(kruskal(g))
with open(directory_path_out + output_file + ".out", "w") as out:
    with open(directory_path_in + output_file + ".in", "r") as f :
        n = f.readline().split()
        n = int(n[0]) # numbers of trips
        for _ in range(0,n-1):
            trip = f.readline().split()
            src, dest, weight = map(float, trip)
            min_power = tree_min_power(or_tree, int(src), int(dest))[1]

            out.write(str(min_power) + "\n")
        # added manually the last line     
        trip = f.readline().split()
        src, dest, weight = map(float, trip)
        min_power = tree_min_power(or_tree, int(src), int(dest))[1]
        out.write(str(min_power))

"""
with open(output_file + ".out", "w") as out:
    with open(output_file + ".in", "r") as f :
        n = f.readline().split()
        n = int(n[0]) # numbers of trips
        for _ in range(0,n):
            trip = f.readline().split()
            src, dest, weight = map(int, trip)
            t0 = time.perf_counter()
            tree_min_power(oriented_tree_construction(kruskal(g)), src, dest)
            t1 = time.perf_counter()
            t = t1 - t0

            out.write(str(t) + "\n")
"""