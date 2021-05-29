#code
def getMax(lst):
    
    if not lst:
        return None
    else:
        max = lst[0]
        for item in lst:
            if item > max:
                max = item
        return(max)
        
sam_list = [1,2,4,10]
print(getMax(sam_list))