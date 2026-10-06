def binary_search(l1,val):
    low = 0
    high = len(l1) - 1
    while low <= high:
        mid = (low + high) // 2
        if l1[mid]  == val:
            return mid
        elif val > l1[mid]:
            low = mid + 1
        elif val <l1[mid]:
            high = mid - 1
        
    return -1


l1 = [2,8,11,14,16,19,23,29]
val = int(input("enter value to seaarch: "))
print(binary_search(l1,val))

        
