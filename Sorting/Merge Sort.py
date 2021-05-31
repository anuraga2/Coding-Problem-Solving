class Solution:
    def merge(self, arr, low, mid, high):
        
        # extracting left and right part of the subarray
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]
        
        # storing the length of the left and right subpart in separate arrays
        a = len(left)
        b = len(right)
        
        # declaring pointers
        i = j = 0
        k = low 
        
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
        
        
    def mergeSort(self,arr, l, r):


        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)