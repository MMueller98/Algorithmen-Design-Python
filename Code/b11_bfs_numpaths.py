
# Anzahl kuerzester Pfade (bzgl Kantenanzahl)
# verwendet bfs
from vl.lek03.bfs import bfs

def bfs_numpaths(G,s):
    m = len(G)
    distance = [None]*m
    S_u = [None]*m

    result = bfs(G,s)       # Ergebnis der Breitensuche
    L_j = result[0]         # Liste L_j der Schichten      
    for v in range(m):                          # Bestimme S_u für alle Knoten v
        j = 0
        for x in range(len(L_j)):               # Finde Nummer j der Schicht in der enthalten ist
            if v in L_j[x]:
                j = x
                break

        if(j != 0):              # Schicht 0 wird nicht betrachtet
            distance[v] = j
            count = 0            # Anzahl der Pfade mit kürzester Länge (j)

            nodes_to_check = set({v})               # Hilfsvariablen
            parent_nodes_upper_layer = set()

                            # Durchlaufe alle Schichten ab j nach oben um zu überprüfen, von wie vielen Knoten
            while j > 0:    # aus der momentan betrachtete Knoten v erreichbar ist -> entspricht count   
                for node in L_j[j - 1]:
                    for n in G[node]:
                        if n in nodes_to_check:
                            parent_nodes_upper_layer.add(n)
                            count += 1

                nodes_to_check = parent_nodes_upper_layer   # alle Knoten von denen v aus erreichbar sind nach oben verfolgen
                parent_nodes_upper_layer = set()
                j -= 1
            
            S_u[v] = count

    print("DISTANCE: ", distance)
    return S_u


def define_G():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2}
    G[1] |= {0,2,3,4}
    G[2] |= {0,1,4,6,7}
    G[3] |= {1,4}
    G[4] |= {1,2,3,5}
    G[5] |= {4}
    G[6] |= {2,7}
    G[7] |= {2,6}
    G[8] |= {9}
    G[9] |= {8}

    return G

G = define_G()
print("NUMBER OF SHORTEST PATHS: ", bfs_numpaths(G,4))


