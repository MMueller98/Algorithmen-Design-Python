
def inc(b): 
    m = len(b)                          # O(1)
    for i in range(m, 0, -1):           # höchstens O(m)
        if i-1 == 0 and b[i-1] == 1:    # O(1)
            b.append(0)
            break
        else:                           # O(1)
            if b[i-1] == 0:
                b[i-1] = 1
                break
            else:
                b[i-1] = 0
    return b

print(inc([1,0,1,1,1]))