
# MINIMUM SPANNING TREE

# Vervollstaendigung von kruskal mit UnionFind
# verwendet die Klasse UnionFind
from vl.lek07.union_find import UnionFind

def kruskal(G):
    m = len(G)
    # Kantenmenge ohne doppelte Eintraege, in O(m+k)
    E = { (G[u][v],frozenset({u,v})) for u in range(m) for v in G[u] }  
    # Ergebnis: Spannbaum und dessen Kosten
    T = set() 
    c = 0

    # UnionFind-Datenstruktur
    uf = UnionFind(m)

    # Kanten nach Kosten sortiert durchlaufen
    for (cost,(u,v)) in sorted(E):
        contains_u = uf.find(u)
        contains_v = uf.find(v)

        # Üverprüfe ob Knoten in gleicher Menge
        # -> falls nein, dann kreisfrei
        if  contains_u != contains_v:
            # Fasse Mengen zusammen
            uf.union(contains_u, contains_v)
            T.add(frozenset((u,v)))
            c += cost
    return T, c


# Bsp aus der VL
# Knotennnummern: s=0, a=1, b=2, c=3, d=4, e=5, f=6, g=7 
def define_G():
    G = [   {1:2, 2:7, 3:10},   # s 
            {0:2, 2:8},         # a
            {0:7, 1:8},         # b
            {0:10, 4:1, 7:9},   # c
            {3:1, 5:3, 6:4},    # d  
            {4:3, 6:5, 7:6},    # e  
            {4:4, 5:5},         # f
            {3:9, 5:6}          # g
        ]
    return G

def define_G_test():
    G = [   {1:2, 2:3, 3:1},
            {0:2, 2:1, 3:4},
            {0:3, 1:1, 3:4},
            {0:1, 1:4, 2:4},
        ]
    
    return G

if __name__ == "__main__":
    G = define_G_test()
    print(kruskal(G))

