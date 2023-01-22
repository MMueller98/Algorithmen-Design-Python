
# MAX KNAPSACK

# verwendet max_ks_bab 
from c02_3_max_ks_bab import max_ks_bab
from c02_1_max_ks_exh import sol_max_ks, m_max_ks
from c02_2_max_ks_bt import K_max_ks
from collections import deque

# Verbesserung der oberen Schranke:

# Problem: wir beachten das Gewicht in Schrankenfunktion garnicht
#   -> somit kann Schranke Wert annehmen, bei dem die Gegenstaende 
#   weit über der Gewichtsgrenze liegen
#   -> gueltige Loesungen koennen diesen Wert nie erreichen
#   -> somit ist Schranke viel zu groß gewaehlt 
  
# 1. Idee zur Schrankenverbesserung
#   -> so lange beliebige Einträge streichen, bis Gewichtgrenze nicht mehr
#    ueberschritten wird
#   -> funktioniert nicht, weil so mögliche Lösungen gestrichen werden könnten

# 2. Idee zur Schrankenverbesserung
#   -> nur "die besten Gegenstände" mitnehmen, sodass man unter Gewichtsgrenze 
#   bleibt
#   -> damit machen wir das, was unser Algorithmus eigentlich machen soll 

# 3. Idee zur Schrankenverbesserung
#   -> Kosten-Nutzen-Funktion erstellen, die zu jedem Zeitpunkt bewertet
#      wie die Kosten-Nutzen im Vergleich zur besten Lösung aussehen






# 2. Aenderung der Schrankenfunktion durch Neudeklaration
def o_max_ks(s,v,S,t):
    s_ges = 0
    v_ges = 0
    for i in range(len(t)):
        if t[i] == 1:
            s_ges += s[i]
            v_ges += v[i]
    
    if v_ges > 0:
        return s_ges/v_ges
    
    return 0

# 3. Anpassung BaB-Algorithmus
def max_ks_bab2(s,v,S):
    opt = [-1,-1]                   # optimaler Wert
    m = len(s)                      # Anzahl der Gegenstände
    M = deque({()})                 # Menge der aktiven Knoten
                                    # () = Wurzel
    counter = 0
    while M:
        t_prev = M.pop()                # beliebigen Knoten entnehmen
        if o_max_ks(s,v,S,t_prev) > opt[1]:
            for a in range(2):          # nächsten Gegenstand mitnehmen oder nicht
                t = t_prev + (a,)       # neues Tupel
                if len(t) == m:
                    if sol_max_ks(s,v,S,t):         # überprüfe ob t zulässige Lösung ist
                        value = m_max_ks(s,v,S,t)
                        if value > opt[0]:             # überprüfe ob t neue beste Lösung ist
                            opt[0] = value
                            opt[1] = o_max_ks(s,v,S,t)

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
    print(max_ks_bab2([3,2,1,5],[3,1,1,4],7))
    print(max_ks_bab2([3,8,1,5],[3,1,1,4],8))

