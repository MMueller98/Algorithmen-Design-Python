from collections import deque

# BFS als Queue
def bfs_queue(G,s):
    m = len(G)
    Q = deque({s})         # Queue der Schichten, mit Startknoten initialisiert 
    Nodes = set({s})       # Menge der erreichten Knoten, mit Startknoten initialisiert
    reached = [False]*m    # bereits besuchte Knoten
    reached[s] = True      #
    parent = [None]*m      # Vorgaenger im BFS-Baum

    while len(Q) > 0:          # solange Queue nicht leer ist
        current_node = Q.pop()  # zu betrachtender Knoten
        for child_node in G[current_node]:  # alle Nachbarn von current_node aus erreichbaren Knoten
            if not reached[child_node]:     # falls neuer Knoten
                Nodes.add(child_node)
                Q.appendleft(child_node)    # neuer Knoten an Anfang der Queue -> wird erst nach allen Knoten
                                            # der aktuellen Schicht betrachtet
                reached[child_node] = True
                parent[child_node] = current_node

    return Nodes, parent    



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
bfs_queue(G,0)


# Vergleich mit bfs aus VL
from vl.lek03.bfs import bfs

for s in range(len(G)):
    print('s = ', s)
    L = bfs(G,s)[0]  # erste Komponente ist Liste der L_i
    # alle L_i vereinigen
    R = { u for i in range(len(L)) for u in L[i]}
    # Vergleich
    print(R == bfs_queue(G,s)[0])
    print(bfs(G,s)[1] == bfs_queue(G,s)[1])




