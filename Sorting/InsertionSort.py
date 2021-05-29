def insertionSort(alist, n):
    #code here
    # Running the outer loop from 1 to the end of the list
    for i in range(1,n):
        x = alist[i]
        j = i - 1
        while j>= 0 and alist[j] > x:
            alist[j+1] = alist[j]
            j = j-1
        
        alist[j+1] = x
    
    return alist