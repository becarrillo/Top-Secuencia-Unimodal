my_list = [1, 2, 7, 8, 81, 43, 21, 18]

def top(v, l, r):
    
    if (l+1 >= r): return max(v[l], v[r])   # CASO BASE: cuando el vector tiene tamaño <= 2
    else:
        m = (l+r) // 2  # elemento del medio
        
        if v[m] < v[m+1]:  # pico o top está a la derecha
           return top(v, m+1, r)
        elif v[m-1] > v[m]:     # pico o top está a la izquierda 
            return top(v, l, m-1)
        else: return v[m]
    
t = top(my_list, 1, len(my_list))
print(t)