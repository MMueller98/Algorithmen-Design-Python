
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
                    M.add(t)
                else:
                    pass
    return T

queen_backtracking_all(3)
queen_backtracking_all(4)
queen_backtracking_all(5)



# for m in range(2,12):
#     T = queen_backtracking_all(m)
#     print('m =',m, '#T =', len(T))

# # Backtracking-Kriterium
# def K_queen(m,t):
#     l = len(t)-1        # Index der neuen Dame
#     for i in range(l):
#         if t[i]==t[l] or abs(t[i]-t[l])==abs(i-l):
#             return False
#     return True

# def queen_backtracking(m):
#     M = {()}
#     while M:
#         t_prev = M.pop()
#         for a in range(m):          # bei QUEEN ist k=m
#             t = t_prev + (a,)       # neues Tupel
#             if len(t) == m:
#                 if sol_queen(m,t): return 1,t
#             else:
#                 if K_queen(m,t):
#                     M.add(t)
#                 else:
#                     pass
#     return 0