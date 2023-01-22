
# MINIMUM SPANNING TREE

# Verbesserung von prim mittels MinPrioQueue
from heapq import heappush, heappop

def prim_pq(G):
    m = len(G)
    # (geschaetzte) Kosten für die Anbindung von Knoten an den Spannbaum
    # mittels einer weiteren Kante
    T = set()           # Ergebnis: Spannbaum als Kantenmenge
    c = 0               # und dessen Kosten
    Q = []              # Min-Priority-Queue mit Schätzwerten als Schlüssel
    visited = set()     # Menge aller bereits besuchten Knoten

    # Proirity Queue enthält Tupel aus Schätzwert, aktueller Knotennummer und Vorgänger
    heappush(Q,(0,0,None))      # Initialisierung mit Knoten 0

    while Q:
        # Auswahl von v als Knoten aus Q mit kleinstem Schlüsselwert
        (cost, v, p_v) = heappop(Q)
        
        # Überprüfe ob Knoten noch betrachtet werden muss
        if not v in visited:
            # Kante in Spannbaum hinzufügen
            T.add(frozenset((p_v,v)))
            c += cost
            # Nachfolger in Queue pushen
            for u in G[v]:
                heappush(Q, (G[v][u], u, v))

        # v als besucht eintragen
        visited.add(v)


    return T-{frozenset((None,0))},c    
  

# Bsp aus der VL
def define_G():
    G = [   {1:4, 2:1, 3:3}, 
            {0:4, 2:4, 3:4}, 
            {0:1, 1:4, 3:2, 5:4},
            {0:3, 1:4, 2:2, 5:6},  
            {5:5},  
            {2:4, 3:6, 4:5}  
        ]
    return G

G = define_G()
print(prim_pq(G))
