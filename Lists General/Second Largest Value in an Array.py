# Function to return second largest element

def secondlargest(lst):
    max = None
    second_max = None
    
    if not lst:
        return(None)
    elif len(lst) == 1:
        return(None)
    else:
        if lst[0] > lst[1]:
            max = lst[0]
            second_max = lst[1]
        
        elif lst[1] > lst[0]:
            max = lst[1]
            second_max = lst[0]
        else:
            max = lst[0]
            second_max = None
        
        for item in lst[2:]:
            if ((not second_max) & (item < max)):
                second_max = item
            elif item < max & item > second_max:
                second_max = item
            elif item > max:
                second_max = max
                max = item
            else:
                second_max = None
        
        return(second_max)
        
lst = [10, 10, 10, 50]
print(secondlargest(lst))
            