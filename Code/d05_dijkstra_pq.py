
# (SINGLE-SOURCE) SHORTEST PATH

# Verbesserung von dijkstra mittels MinPrioQueue
from heapq import heappush, heappop

def dijkstra_pq(G,s):
    m = len(G)                  # O(1)
    d = [None]*m                # O(m)  (geschaetzte) Pfadkosten
    d[s] = 0                    # O(1)   sind 0 fuer den Startknoten
    Q = []                      # O(1)   Min-Priority-Queue mit Schätzwerten als Schlüssel
    visited = set()             # O(1)   Menge aller bereits besuchten Knoten

    # Proirity Queue enthält Tupel aus Schätzwert und Knotennummer
    heappush(Q,(0,s))           # O(1)   Initialisierung mit s
    
    while Q:                                        # O(m) Iterationen
        # Auswahl von v als Knoten aus Q mit kleinstem Schlüsselwert 
        (dist,v) = heappop(Q)                       # O(log m)

        # Überprüfe ob Pfadkosten aktualisiert werden müssen
        if d[v] == None or d[v] > dist:             # O(1)
            d[v] = dist
        
        # Nachfolger der nicht-besuchten Knoten in Heap pushen
        if not v in visited:                        # O(1)
            for u in G[v]:                          # O(deg(v))
                heappush(Q, (dist + G[v][u], u))    # O(log m)

        # v als besucht eintragen
        visited.add(v)                              # O(1)
             
    return d
    
    



def define_G():
    G = [   {1:1, 4:4, 2:2},   # Nachfolger von s
            {3:3, 4:1},        # von u
            {4:2, 5:3},        # von x
            {},                # von y
            {3:1, 5:2},        # von v
            {}                 # von z
        ]
    return G


if __name__ == "__main__":
    G = define_G()
    print(dijkstra_pq(G,0))    





