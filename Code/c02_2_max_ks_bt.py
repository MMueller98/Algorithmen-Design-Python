
# MAX KNAPSACK

# verwendet sol_max_ks, m_max_ks
from c02_1_max_ks_exh import sol_max_ks, m_max_ks

# vereinfachtes Backtracking-Kriterium:
# Teilloesung noch zulaessig?
def K_max_ks(s,v,S,t):
    size = 0
    for i in range(len(t)):         # Größen der Gegenstände addieren 
        if t[i] == 1:
            size += s[i]
    
    if size <= S:                   # Überprüfen ob Maximalgröße überschritten
        return True

    return False

# Entwurfsmuster Backtracking
def max_ks_backtracking(s,v,S):
    opt = -1                        # optimaler Wert
    m = len(s)                      # Anzahl der Gegenstände
    M = {()}                        # Menge der aktiven Knoten
                                    # () = Wurzel
    while M:
        t_prev = M.pop()            # beliebigen Knoten entnehmen
        for a in range(2):          # nächsten Gegenstand mitnehmen oder nicht
            t = t_prev + (a,)       # neues Tupel
            if len(t) == m:
                if sol_max_ks(s,v,S,t):         # überprüfe ob t zulässige Lösung ist
                    value = m_max_ks(s,v,S,t)
                    if value > opt:             # überprüfe ob t neue beste Lösung ist
                        opt = value

            else:
                if K_max_ks(s,v,S,t):
                    M.add(t)
                else:
                    pass
    return opt


# Bsp m=4, S=7
if __name__ == "__main__":
    print(max_ks_backtracking([3,2,1,5,1,3,2,4],[3,1,1,4,4,5,3,7],10))
    print(max_ks_backtracking([3,8,1,5],[3,1,1,4],8))
