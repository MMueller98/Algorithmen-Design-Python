
# MAX KNAPSACK

# zulaessige Loesung, auch fuer Teilloesungen
def sol_max_ks(s,v,S,t):
    size = 0
    for i in range(len(t)):             # Größen der Gegenstände addieren 
        if t[i] == 1:
            size += s[i]
    
    if size <= S:           # Überprüfen ob Maximalgröße überschritten
        return True

    return False

# Bewertungsfunktion, auch fuer Teilloesungen
def m_max_ks(s,v,S,t):
    value = 0
    for i in range(len(t)):             # Werte der Gegenstände addieren
        if t[i] == 1:
            value += v[i]

    return value

# Entwurfsmuster Exhaustive Search
from itertools import product
def max_ks_exhaustive(s,v,S):
    opt = -1    
    for t in product((0,1), repeat=len(s)):
        if sol_max_ks(s,v,S,t):                 # überprüfe ob t zulässige Lösung ist
            value = m_max_ks(s,v,S,t)
            if value > opt:                     # überprüfe ob t neue beste Lösung ist
                opt = value
    
    return opt


# Bsp m=4, S=7
if __name__ == "__main__":
    print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],7))
    print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],8))




