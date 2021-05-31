
arr = [34,42,56,21,74,22,81,45,94,28]


def lomuto_partition(arr,l,h):
    pivot = arr[h]
    i = l - 1
    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return(i+1, arr)


print(lomuto_partition(arr,0,len(arr)-1))