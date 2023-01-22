# verwendet dfs
from operator import truediv
from vl.lek03.dfs import dfs


# Umkehrgraph eines Digraphen
def reverse(G):
    m = len(G)
    Grev = [set() for _ in range(m)]  # alle Mengen leer anlegen

    for i in range(m):           # Eintrag und Index vertauschen
        for v in G[i]:
            Grev[v].add(i)
    return Grev

# alle starken Zusammenhangskomponenten eines Digraphen
def strong_comp(G):
    C = [] 

    Grev = reverse(G)       # Umkehrgraph von G
    m = len(G)
    reached = [False]*m     # bereits erreicht Knoten
    node_available = True   # zeigt an ob noch unerreichte Knoten im Graph existieren

    while node_available:
        v = getUnreachedNode(reached)   
        if(v != -1):                        # Es existieren noch unerreichte Knoten im Graphen     
            result = dfs(G,v)               # Tiefensuche von v in Graph und Umkehrgraph
            result_rev = dfs(Grev,v)

            intersection = result[0] & result_rev[0]    # Schnittmenge der erreichten Knoten von Tiefensuche
            
                                            # Alle erreichten Knoten in Zusammenhangskomponente speichern
            for u in intersection:          # und erreichten Knoten in reached markieren
                reached[u] = True
            
            C.append(intersection)
        else:                               # Alle Knoten des Graphen wurden besucht
            node_available = False

    return C


def getUnreachedNode(reached):
    for i in range(len(reached)):
        if reached[i] == False:
            return i

    return -1


# gerichteter Graph
def define_diG():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {2}
    G[1] |= {0,2}
    G[2] |= {0,7}
    G[3] |= {4}
    # G[4] |= 
    # G[5] |= 
    G[6] |= {7}
    G[7] |= {6}
    # G[8] |=
    G[9] |= {3,8}
    return G

if __name__ == "__main__":
    G = define_diG()
    Grev = reverse(G)

    # G unveraendert
    print(G == define_diG())
    print(G == reverse(Grev))

    print("DFS: ", dfs(G,0))
    print("DFS rev: ", dfs(Grev,0))
    print(strong_comp(G))

    #print("TIEFENSUCHE: ", dfs(G, 0))
    #print("BREITENSUCHE: ", bfs(G, 0))


