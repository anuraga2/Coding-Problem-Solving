#Function to sort the array using bubble sort algorithm.
def bubbleSort(self,arr, n):
    # code here
    
    # running the outer loop
    for i in range(n-1):
        swapped = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = False
        
        if swapped:
            return arr
    
    return arr