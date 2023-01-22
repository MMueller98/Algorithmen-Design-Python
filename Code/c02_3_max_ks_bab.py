
# MAX KNAPSACK

# verwendet sol_max_ks, m_max_ks, K_max_ks 
from collections import deque
from c02_1_max_ks_exh import sol_max_ks, m_max_ks
from c02_2_max_ks_bt import K_max_ks


# obere Schranke:
# Bewertung der Teilloesung t + Werte aller restlichen Gegenstaende
def o_max_ks(s,v,S,t):
    max_value = m_max_ks(s,v,S,t)       # alle bisherigen Gegenstaende einpacken

    for i in range(len(t), len(s)):     # alle verbleibende Gegenstaende einpacken
        max_value += v[i]

    return max_value

# Entwurfsmuster Branch and Bound
def max_ks_bab(s,v,S):
    opt = -1                        # optimaler Wert
    m = len(s)                      # Anzahl der Gegenstände
    M = deque({()})                 # Menge der aktiven Knoten
                                    # () = Wurzel
    counter = 0
    while M:
        t_prev = M.pop()                # beliebigen Knoten entnehmen
        if o_max_ks(s,v,S,t_prev) > opt:
            for a in range(2):          # nächsten Gegenstand mitnehmen oder nicht
                t = t_prev + (a,)       # neues Tupel
                if len(t) == m:
                    if sol_max_ks(s,v,S,t):         # überprüfe ob t zulässige Lösung ist
                        value = m_max_ks(s,v,S,t)
                        if value > opt:             # überprüfe ob t neue beste Lösung ist
                            opt = value

                else:
                    if K_max_ks(s,v,S,t):
                        M.appendleft(t)
                    else:
                        pass
        else: 
            counter += 1
    print("COUNTER: ", counter)
    return opt


# Bsp m=4, S=7
if __name__ == "__main__":
    print(max_ks_bab([3,2,1,5,1,3,2,4],[3,1,1,4,4,5,3,7],10))
    print(max_ks_bab([3,8,1,5],[3,1,1,4],8))
