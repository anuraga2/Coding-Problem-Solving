#Function to sort the array using bubble sort algorithm.
def selectionSort(arr,n):
    #code here
    
    for i in range(n-1):
        min_ind = i
        for j in range(i+1,n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    
    return arr