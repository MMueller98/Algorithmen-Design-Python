
# sol_queen und K_queen vorher deklarieren
from vl.lek04.queen_exh import sol_queen
from vl.lek04.queen_bt import K_queen



# def queen_backtracking_all(m):
#     T = set()
#     # todo
#     return T 

def queen_backtracking_all(m):
    T = set()   # Ergebnismenge
    M = {()}    # Menge der aktiven Knoten
    while M:
        t_prev = M.pop()
        for a in range(m):          # bei QUEEN ist k=m
            t = t_prev + (a,)       # neues Tupel
            if len(t) == m:
                if sol_queen(m,t):
                    T.add(t)
            else:
                if K_queen(m,t):
                    M.add((t))
                else:
                    pass
    return T

print(f"m=3: {queen_backtracking_all(3)}")
print(f"m=4: {queen_backtracking_all(4)}")
# print(f"m=5: {queen_backtracking_all(5)}")

print(f"Zulässige Stellungen bei m=11: {len(queen_backtracking_all(11))}")
