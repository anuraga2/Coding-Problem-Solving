lst = [1,1,2,2,30,30,43,1,1,5]


def reverse_list(lst):
    
    if len(lst) <= 1:
        return(lst)
    
    else:
        s = 0
        e = len(lst) - 1
        
        while(s < e):
            lst[s], lst[e] = lst[e], lst[s]
            s = s+1
            e = e-1
    
    return(lst)

print(reverse_list(lst))