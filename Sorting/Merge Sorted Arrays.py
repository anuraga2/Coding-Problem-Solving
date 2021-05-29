# writing merge subroutine for two sorted arrays

arr1 = [10,15]
arr2 = [5,6,6,30,40]

def merge_sorted(arr1, arr2):
    
    if len(arr1) == 0 and len(arr2) == 0:
        return []
    elif len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1
    
    comb_arr = []
    a = len(arr1)
    b = len(arr2)
    i = j = 0
    while i < a and j < b:
        if arr1[i] <= arr2[j]:
            comb_arr.append(arr1[i])
            i+=1
        else:
            comb_arr.append(arr2[j])
            j+=1
    
    while i < a:
        comb_arr.append(arr1[i])
        i += 1
    
    while j < b:
        comb_arr.append(arr2[j])
        j += 1
    
    return comb_arr
    
print(merge_sorted(arr1,arr2))