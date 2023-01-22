
# MINIMUM INTERVAL PARTITIONING

# ist Intervallmenge M kompatibel?
# für jedes i,j mit i!=j in M muss gelten: 
# si >= fj  oder  sj >= fi 
def compatible(L,M):
    for i in M:
        for j in M:
            if i != j:
                (si, fi) = L[i]
                (sj, fj) = L[j]
                if (not si >= fj) and (not sj >= fi):
                    return False
    return True

# Bsp
L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
# print(compatible(L,{0,2,5}))
# print(compatible(L,{0,3,4,7}))
# print(compatible(L,{1,2}))
# print(compatible(L,set()))




# zulaessige Loesung:
# - r ist stets total
# - jede Intervallmenge pro Ressource ist kompatibel
def sol_min_intpart(L,r):
    m = len(L)
    R = [set() for _ in range(m)]           # O(m)

    for i in range(m):                      # O(m)
        R[r(i)].add(i)

    for ressource in R:                     # O(m)
        if not compatible(L, ressource):    # O(m^2)
            return False

    return True

# Bewertungsfunktion:
# - Kardinalitaet Wertebereich von r
def m_min_intpart(L,r):
    m = len(L)
    R = [set() for _ in range(m)]           # O(m)
    value = 0

    for i in range(m):                      # O(m)
        R[r(i)].add(i)
    
    for ressource in R:                     # O(m)
        if ressource != set():
            value += 1

    return value

# Entwurfsmuster Exhaustive Search
from itertools import product

# gibt eine Funktion zurück, die jedes Intervall i einer 
# Ressource zuordnet
def def_r(t):
    def r(i):
        return t[i]
    return r


# Laufzeit: O(m^(m+2))
def min_intpart_exhaustive(L):
    m = len(L)            
    opt = m
    r_opt = None

    # Erstelle alle möglichen Funktionen r und wähle diejenige
    # mit dem kleinsten Wertebereich
    for t in product([i for i in range(m)], repeat=m): #O(m^m)
        r = def_r(t)  
        # Falls Lösung zulässig (Intervalle in Ressourcen sind kompatibel)
        if sol_min_intpart(L, r):       # O(m^3)      
            deg = m_min_intpart(L,r)    # O(m)
            # Vergleiche Wertebereich von r mit Wertebereich der (bisher) optimalen Lösung
            if deg < opt:               
                opt = deg
                r_opt = r               # optimale Funktion 

    return opt


print("Optimale Anzahl an Ressourcen: ", min_intpart_exhaustive([(0,2),(1,3),(0,3),(2,4)]))
print("Optimale Anzahl an Ressourcen: ", min_intpart_exhaustive([(0,2),(0,3),(2,3),(3,4),(2,4),(4,7)]))

lenn = 0
for k in product([i for i in range(5)], repeat=5):
    lenn += 1


print(lenn)




