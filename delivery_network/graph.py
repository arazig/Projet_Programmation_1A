class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.powers = []

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
# Il faut dans un premier temps verifier que les noeuds sont dans le graph sinon on les ajoutes 
        
        if node1 not in self.graph.keys():
            self.graph[node1] = []
            self.nodes.append(node1)
            self.nb_nodes += 1
        if node2 not in self.graph.keys():
            self.graph[node2] = []
            self.nodes.append(node2)
            self.nb_nodes += 1

        self.graph[node1].append((node2, power_min, dist))  # On ajoute la relation a partir de la 1ere extremité de l'arrete 
        self.graph[node2].append((node1, power_min, dist))  # On ajoute également de l'autre coté ( vice versa)
        self.nb_edges += 1
      
    def connected_components(self):
        """
        return a list of all the conected components of a graph
        """
        # création d'un dictionnaire permettant de voir si un noeud est visité
        visited = {i: False for i in self.nodes} 

        def exploration(s):
            # this function return all the nodes of a graph explorated from an initial one
            L = [s]  # list of the connected nodes
            s_neigh = [self.graph[s][j][0] for j in range(0, len(self.graph[s]))]  # list of the node's neighbours
            for neigh in s_neigh: 
                if not visited[neigh]:  # for each neighbor not visited
                    visited[neigh] = True
                    L = L + exploration(neigh)
            return L

        Components = []
        N = self.nodes
        for node in N:
            if visited[node] is False:
                Components.append(exploration(node))
        return Components


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component),
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))


    def get_path_with_power(self, src, dest, power):
        """This function allows you to see if there is a possible path between
        two nodes for a truck with a given power. If yes, it returns one of the 
        of the possible paths.

        Args:
            src (int): source, starting node
            dest (int): destinantion
            power (int): power of the truck
        """
        explo = [(src, [src])]
        list_paths = []  # list of the paths between the nodes
        visited = {i: False for i in self.nodes}
        while explo:
            node, path = explo.pop(0)  # it allows us to update the paths used
            n_neigh = [self.graph[node][j] for j in range(0, len(self.graph[node]))]  # list of (node's neighbours,powermin,dist)
            for neighb in n_neigh:
                powermin = neighb[1]
                if neighb[0] not in path and power >= powermin:  # for each neighbor accessible (by truck's power) not yet in the path
                    if neighb[0] == dest:
                        list_paths.append(path + [neighb[0]])
                    elif not visited[neighb[0]]:
                        explo.append((neighb[0], path + [neighb[0]]))
                        visited[neighb[0]] = True
        return None if list_paths == [] else list_paths[0]
    
    def min_power(self, src, dest):
        """     
        calculates, for a given journey t, by a dichotomic method the minimum power of
        a truck that can cover a given journey.
        Return a path and the minimal power.

        Args:
            src (int): source, starting node
            dest (int): destinantion
        Output :
        path (list)
        min_power (int)
        """
        list_power = sorted(self.powers)
        x = 0
        y = len(list_power)-1
        m = (x+y)//2
        while x < y:
            #print(x,y,m)
            if self.get_path_with_power(src, dest, list_power[m]) != None:
                y = m
            else:
                x = m + 1
            m = (x+y)//2
        pth = self.get_path_with_power(src, dest, list_power[x])
        puiss = list_power[x]
        return pth, puiss


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = file.readline().split()
            if len(edge) == 3:
                node1, node2, power_min = int(edge[0]), int(edge[1]), int(edge[2])
                g.add_edge(node1, node2, power_min)  # will add dist=1 by default
                # g.edges.append((node1, node2, power_min, 1))
                g.powers.append(power_min)
            elif len(edge) == 4:
                node1, node2, power_min, dist = int(edge[0]), int(edge[1]), int(edge[2]), float(edge[3])  #Pour pouvoir lire 10
                g.add_edge(node1, node2, power_min, dist)
                #g.edges.append((node1, node2, power_min, dist))
                g.powers.append(power_min)
            else:
                raise Exception("Format incorrect")
    return g

def graph_from_file_Routes(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        first_line = file.readline().split()
        if len(first_line) == 2 :
            n, m = int(first_line[0]), int(first_line[1])
        elif len(first_line) == 1 :
            n = int(first_line[0])
        g = Graph(range(1,n+1))
        lines =file.readlines() # c'est une liste de lignes ["1 2 3","2 3 5"]
        for line in lines[0::] :
            line = line.split()
            if len(line)==3 :
                node1, node2, power_min= map(int,line)
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
                g.powers.append(power_min)
            elif len(line)==4 :
                #print(map(int,line))
                node1, node2, power_min, dist= map(int,line)
                g.add_edge(node1, node2, power_min, dist)
                g.powers.append(power_min)
            else :
                    raise Exception("Incorrecte format")
    return g




def possible_path(self, source, destination):
    """
    This function allows you to check if it is possible to find a path between
    two nodes thanks to the connected components.
    /!\ CAUTION /!\  :
        If the graph is too large, it is assumed that there is always a path
        between two nodes and therefore this function should not be used
    -----------------
    Output :
    pos_path (Bool) : True or False
    """
    pos_path = False
    for comp in self.connected_components_set():
        if source in comp and destination in comp:
            pos_path = True
            return pos_path
