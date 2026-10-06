def selectonsort(l1):
    for i in range(len(l1)):
        min_ele = i
        for j in range(i+1, len(l1)):
            if l1[min_ele] > l1[j]:
                min_ele = j
        l1[i],l1[min_ele] = l1[min_ele], l1[i]

l1=[8,3,1,5,2]
print("Before Sorting:",l1)
selectonsort(l1)
print("After Sorting:",l1)

#output:
# Before Sorting: [8, 3, 1, 5, 2]
# After Sorting: [1, 2, 3, 5, 8]