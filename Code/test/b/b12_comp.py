

# alle Zusammenhangskomponenten eines unger. Graphen
# verwendet dfs
def dfs(G,s):
    m = len(G)
    S = [s]                 # Stack statt Rekursion
    explored = [False]*m    # alle Nachbarn bereits behandelt, O(m)
    parent = [None]*m       # Vorgaenger im DFS-Baum
    while S:
        u = S.pop()
        if not explored[u]:
            explored[u] = True  # 1. Markieren u
                                # 2. R ergibt sich später aus expored
            for v in G[u]:      # 3. Alle Nachbarn v
                S.append(v)         # auf den Stack
                # Vorgaenger nur bei erster Entdeckung merken
                if not explored[v]: parent[v] = u       
    return { u for u in range(m) if explored[u]}, parent    # O(m)
    
def comp(G):
    m = len(G)
    not_visited = {i for i in range(m)}
    C = []  

    while not_visited:
        v = not_visited.pop()
        dfs_result = dfs(G, v)[0]
        not_visited -= dfs_result

        C.append(dfs_result)
    
    return C


def define_G():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2}
    G[1] |= {0,2}
    G[2] |= {0,1,6,7}
    G[3] |= {4}
    G[4] |= {3}
    # G[5] |= 
    G[6] |= {2,7}
    G[7] |= {2,6}
    G[8] |= {9}
    G[9] |= {8}
    return G

G = define_G()
print(comp(G))

