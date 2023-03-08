from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.02.in"

g = graph_from_file(data_path + file_name)
print(g)

assert ( frozenset({1,2,3}) == frozenset({3,2,1}))

for comp in Graph.connected_components_set(g):
    print(comp)


def get_path_with_power(g, src, dest, power):
        #raise NotImplementedError

        """Cette fonction permet de svoir si il existe un trajet possible entre 
        deux neouds pour un camion avec une puissance donnée. Si oui, elle nous renvoie un 
        des chemins possible.

        Args:
            src (int): source, starting node
            dest (int): destinantion
            power (int): power of the truck
        """
        #Tout d'abord, on regarde si les deux noeuds sont la meme composantes, si non on retourne None
        #samecomp= False
        #for comp in Graph.connected_components_set(g):
        #    if (frozenset([src,dest])) in comp :
        #        samecomp = True
       # if samecomp == False :
         #   return None

        #A present il nous faut récuperer tous les chemins possibles entre les deux noeuds
        explo=[(src,[src])]
        list_paths = [] # list of the paths between the nodes
        while explo : 
            node, path = explo.pop(0) # cela nous permet d'actualiser les chemins explo
            n_neigh = [g.graph[node][j] for j in range(0,len(g.graph[node]))] #list of (node's neighbours,powermin,dist)
            for neighb in n_neigh : 
                powermin = neighb[1]
                if neighb[0] not in path and power >= powermin:  #for each neighbor accessible (by truck's power) not yet in the path
                    if neighb[0] == dest:
                        list_paths.append(path + [neighb[0]])
                    else:
                        explo.append((neighb[0], path + [neighb[0]]))
        return None if list_paths ==[] else list_paths

print(get_path_with_power(g, 1, 4,3))
