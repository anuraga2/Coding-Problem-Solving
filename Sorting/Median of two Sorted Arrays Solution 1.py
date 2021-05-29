class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        
        i = 0
        j = 0
        emp_list = []
        

        for k in range(len(num1) + len(num2)):
            
            
            # Checking for empty lists
            if not num1:
                emp_list = num2
                break
            elif not num2:
                emp_list = num1
                break
            
            # This block of code will be executed if both the lists are non empty
            else:
                if num1[i] <= num2[j]:
                    emp_list.append(num1[i])
                    i = i+1

                elif num2[j] <= num1[i]:
                    emp_list.append(num2[j])
                    j = j+1
                
                # if the end of array 2 is achieved then take the remaining elements of array 1 and put it in emp_list
                # and break out of the loop
                
                if j == len(num2):
                    emp_list = emp_list + num1[i:]
                    break
                # if the end of array 1 is achieved then take the remaining elements of array 1 and put it in emp_list
                # and break out of the loop
                
                if i == len(num1):
                    emp_list = emp_list + num2[j:]
                    break
        
        # Code chunk to return the median of the sorted arrays
        if len(emp_list) % 2 == 0:
            return((emp_list[int(len(emp_list)/2)] + emp_list[int((len(emp_list)/2)) - 1])/2)
        else:
            return(emp_list[int(len(emp_list)/2)])

        