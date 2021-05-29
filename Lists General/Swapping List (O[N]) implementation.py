lst = [1,1,2,2,30,30,43,1,1]

def reverse(lst):
    
    if len(lst) <=1:
        return(lst)
    else:
        rev_lst = [0]*len(lst)
        for i in range(len(lst)):
            rev_lst[-i-1] = lst[i]
    
    return(rev_lst)
    

print(reverse(lst))