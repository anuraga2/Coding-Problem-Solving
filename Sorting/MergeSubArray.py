# writing a fucntion to merge subarrays

arr = [10,15,20,40,8,11,55]
low = 0
high = 6
mid = 3

def merge(arr, low, mid, high):
    
    # extracting left and right part of the subarray
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    
    # storing the length of the left and right subpart in separate arrays
    a = len(left)
    b = len(right)
    
    # declaring pointers
    i = j = k = 0
    
    while i < a and j < b:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    
    while i < a:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < b:
        arr[k] = right[j]
        j += 1
        k +=1
    
    return arr

print(merge(arr, low, mid, high))
        
    
    