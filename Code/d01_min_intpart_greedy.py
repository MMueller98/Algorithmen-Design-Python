
# MINIMUM INTERVAL PARTITIONING


# Enwurfsmuster Greedy
# Laufzeit: O(m^2)
def min_intpart_greedy(L):      
    m = len(L)                                  # O(1)
    R = [{0}]                                   # O(1)
    (_,last) = L[0]                             # O(1)
    Lasts = [last]                              # O(1)

    for i in range(1,m):                        # O(m)
        (s,f) = L[i]                                # O(1)
        ressource_found = False                     # O(1)
        for j in range(len(Lasts)):                 # O(m)
            if s >= Lasts[j]:                           # O(1)
                R[j].add(i)                     
                Lasts[j] = f
                ressource_found = True
                break
        
        if not ressource_found:                         # O(1)
            R.append({i})
            Lasts.append(f)

    print(R)

    return len(R)


# Bsp
L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
print(min_intpart_greedy(L))
print(min_intpart_greedy([(0,2),(0,3),(1,3),(2,4)]))
print(min_intpart_greedy([(0,3),(0,2),(2,3),(3,4)]))


# Laufzeit
#

