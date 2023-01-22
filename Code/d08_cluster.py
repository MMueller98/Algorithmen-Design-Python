
# l-CLUSTERING
from d07_kruskal import kruskal
from b12_comp import comp

def cluster(m,d,l):
    # 1. vollstaendigen Graph mit m Knoten, m^2 Kanten und Kosten d[u,v] konstruieren
    G = [{j:d[i,j] for j in range(m) if i!=j} for i in range(m)]    # O(m^2)

    # 2. Alg. kruskal unveraendert aufrufen
    (mst,_) = kruskal(G)    # O(k*log(m))

    # 3. die l-1 teuersten Kanten löschen
    # Liste mit Kanten und dazugehörigen Kosten erstellen 
    li = []
    for e in mst:   # O(k)
        (u,v) = e               
        dist = d[u,v]
        li.append((dist,(u,v)))

    # Liste reversed sortieren und ersten l-1 Elemente "entfernen"
    edges = sorted(li, reverse=True)[l-1:]      # O(k*log(k))


    # 4. Zush.komponenten bestimmen,  via B.12 (comp)
    # dazu Graph mit allen Knoten konstuieren und Kanten einf.
    Graph = [set() for _ in range(m)]
    for e in edges:     # O(k)
        (_,(u,v)) = e
        Graph[u].add(v)
        Graph[v].add(u)
    
    # Zusammenhangskomponenten bestimmen
    comps = comp(Graph)     # O(m+k)

    return comps


# Distanzfunktion symmetrisch, Diag. 0
def define_d():
    d = {}
    d[0,0]= 0
    d[0,1]= 11
    d[0,2]= 7
    d[0,3]= 15
    d[0,4]= 8
    d[1,0]= 11
    d[1,1]= 0
    d[1,2]= 12
    d[1,3]= 9
    d[1,4]= 2
    d[2,0]= 7
    d[2,1]= 12
    d[2,2]= 0
    d[2,3]= 13
    d[2,4]= 14
    d[3,0]= 15
    d[3,1]= 9
    d[3,2]= 13
    d[3,3]= 0
    d[3,4]= 6
    d[4,0]= 8
    d[4,1]= 2
    d[4,2]= 14
    d[4,3]= 6
    d[4,4]= 0  

    return d  

if __name__ == "__main__":
    d = define_d()
    m = 5
    for l in range(1,6):
        print("=========================================================")
        print(f"cluster: {cluster(m,d,l)}")
       
        
 




