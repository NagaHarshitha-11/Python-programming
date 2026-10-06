import math

# BUBBLE SORT
def bubblesort(l1):
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            if l1[i] > l1[j]:
                l1[i], l1[j] = l1[j], l1[i]

    return l1

def bucketsort(l1):
    '''step-1'''
    # Finding total buckets to create based on the total element in the list
    total_buckets = round(math.sqrt(len(l1)))
    print("Total number of buckets:",total_buckets)

    '''step-2'''
    # Creation of buckets with above value
    buckets = []
    for _ in range(total_buckets):
        buckets.append([])
    print(buckets)

    '''step-3'''
    # iterate through each element in list and insert each element into its respective bucket
    for i in l1:
        idx = math.ceil(i*total_buckets/max(l1))
        # print(i,"->",idx,"bucket") optional
        buckets[idx-1].append(i)
    print()
    print(buckets)
    
    '''step-4'''
    # Sort the buckets
    for i in range(len(buckets)):
        buckets[i] = bubblesort(buckets[i])
    print(buckets)

    '''step-5'''
    # Merge the buckets
    k = 0 #pointing to 0th index
    for i in range(total_buckets):
        for j in range(len(buckets[i])):
            l1[k] = buckets[i][j]
            k+=1

# l1 = [8,2,1,7,4,6,5,3,9, 8 ,4,4,3,7,89, 765, 97, 9,7, 121,113,103,176,987,564,789,8765,8907,865,54,78,98,65,789,543,65,724,743,825]
l1 = [8,2,1,7,4,6,5,3,9]
print("Bucket Sort")
print("Before sort: ",l1)
bucketsort(l1)
print("After Sort: ",l1)