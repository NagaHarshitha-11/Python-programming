def mergesort(l1):
    if len(l1) > 1:       #BASE CONDITION
        mid = len(l1)//2
        left_half = l1[:mid]
        right_half = l1[mid:]
        mergesort(left_half)
        mergesort(right_half)
    
        i = 0 #left list elements
        j = 0 #Right list elements
        k = 0 #Original list

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l1[k] = left_half[i]
                i += 1
            else:
                l1[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            l1[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            l1[k] = right_half[j]
            j += 1
            k += 1



l1 = [2,4,1,7,8,6,5,3]
print("Before Sorting: ",l1)
mergesort(l1)
print("After Sorting: ",l1)
