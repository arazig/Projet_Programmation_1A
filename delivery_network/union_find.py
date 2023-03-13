class UnionFind:
    def __init__(self, n):
        """
        n : the initiale size of each tree (nb of nodes)
        """
        self.parent = list(range(n+1)) 
        # c'est une liste des parents pour chaque indice
        self.rank = [0] * (n+1)
        
    def find(self, x):
        """
        Permet de trouver le représentant (ou la racine) 
        de l'ensemble auquel appartient un élément donné.
        Modifie tous les parents durant l'execution en les remplacant par la racine
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def Union(self, x, y):
        """
        Permet de fusionner les deux ensembles contenant x et y
        """
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
