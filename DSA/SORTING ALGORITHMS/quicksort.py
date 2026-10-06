def partition(start, end, l1):
    i = start
    j = end-1
    pivot = l1[end]
    while i < j:
        while l1[i] < pivot:
            i += 1
        while l1[j] > pivot:
            j -= 1
        if i < j:
            l1[i],l1[j] = l1[j],l1[i]

    if l1[i] > pivot:
        l1[i],l1[end] = l1[end],l1[i]
    return i

def quicksort(start, end, l1):
    if start < end:
        pi = partition(start,end,l1)
        quicksort(start,pi-1,l1)
        quicksort(pi+1,end,l1)

l1 = [3,5,4,1,2,9,4,7,6]
print("QuickSort")
print("Before sorting: ",l1)
quicksort(0,len(l1)-1,l1)
print("After Sorting: ",l1)
