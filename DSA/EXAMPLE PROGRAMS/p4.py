'''WAP TO MERGE TWO SORTED LISTS'''
def merge_two_sorted_list(l1,l2):
    res = []
    i = 0 #list 1
    j = 0 #list 2


    while i <len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res += [l1[i]]
            i += 1
        else:
            res += [l2[j]]
            j += 1

    while i < len(l1):
        res += [l1[i]]
        i += 1

    while j < len(l2):
        res +=[l2[j]]
        j += 1

    print(res)

l1 = [1,4,7,8,11,11]
l2 = [2,3,6,9,12,14]
# print("Before Sorting: ",l1, l2)
merge_two_sorted_list(l1,l2)
# print("After Sorting: ",l1, l2)
