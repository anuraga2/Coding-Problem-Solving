# Rotate array
lst = [1,2,3,4,5,6,78,32,4,5]

def rotate1(lst):
    
    if len(lst) <= 1:
        return(lst)
    
    else:
        
        start = lst[0]
        i = 1
        while(i < len(lst)):
            lst[i-1] = lst[i]
            i = i+1
        
        lst[len(lst)-1] = start
        return(lst)


print(rotate1(lst))