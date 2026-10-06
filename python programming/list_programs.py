# 1. count number of elements present in list without using in-built functions?
# l1=[1,2,4,11,5,6,0,7]
# cnt=0
# for i in l1:
#     cnt+=1
# print("Total elements in l1 is: ",cnt)
# o/p:  Total elements in l1 is:  8

# l1=[1,2,4,11,5,6,0,7]
# cnt=0
# for i in l1:
#     if i==0:
#         continue
#     cnt+=1
# print("Total elements in l1 is: ",cnt)
# o/p: Total elements in l1 is:  7

# 2. wap to display max element in list along with its index?
# l1=[1, 2, 4, 20, 5, 6, 0, 7]
# mx_ele=l1[0]
# idx=0
# for i in range(1,len(l1)):
#     if l1[i]>mx_ele:
#         mx_ele=l1[i]
#         idx=i
# print("Max element in l1:",mx_ele,"its index position:",idx)
# o/p: Max element in l1: 20 its index position: 3


# finding max and min element in a given list?
# l1=[1,4,36,100,3]
# l1.sort()
# print(l1[-1])
# print(l1[0])
# o/p:
# 100
# 1

# 3. wap to display min element in list along with its index?
# l1=[1, 2, 4, 20, 5, 6, 0, 7, -67, -3]
# min_ele=l1[0]
# idx=0
# for i in range(1,len(l1)):
#     if l1[i]<min_ele:
#         min_ele=l1[i]
#         idx=i
# print("Min element in l1:",min_ele,"its index position:",idx)
# o/p: Min element in l1: 0 its index position: 6
# o/p: Min element in l1: -67 its index position: 8

# 4. wap to display first two maximum element along with its difference?
# l1=[1, 2, 4, 67, 12, 10, 0, 9, 2]

# max1=l1[0]
# mx2=l1[1]

# for i in range(1,len(l1)):
#     if l1[i]>max1:
#         max2=max1
#         max1=l1[i]
#     elif l1[i]>max2:
#         max2=l1[i]

# print("First Max element in l1:",max1)
# print("First Max element in l1:",max2)
# print("Differnece is:",max1-max2)
# o/p:
# First Max element in l1: 67
# First Max element in l1: 12
# Differnece is: 55

# 5.wap to display missing elements from the list excluding the number itself?
# l=[2, 12, 18, 27, 38, 42, 57]
# for i in range(len(l)-1):
#     first_ele=l[i]+1
#     last_ele=l[i+1]
#     for j in range(first_ele,last_ele):
#         print(j,end=' ')
# o/p: 3 4 5 6 7 8 9 10 11 13 14 15 16 17 19 20 21 22 23 24 25 26 28 29 30 31 32 33 34 35 36 37 39 40 41 43 44 45 46 47 48 49 50 51 52 53 54 55 56

# (or)

# l=[2, 12, 18, 27, 38, 42, 57]
# for i in range(len(l)-1):
#     for j in range(l[i]+1, l[i+1]):
#         print(j,end=' ')
# 3 4 5 6 7 8 9 10 11 13 14 15 16 17 19 20 21 22 23 24 25 26 28 29 30 31 32 33 34 35 36 37 39 40 41 43 44 45 46 47 48 49 50 51 52 53 54 55 56  

# 6. program to check is given list is palindrome or not?
# l1=[1,2,3,4,3,2,1]
# j=len(l1)-1
# for i in range(len(l1)):
#     if l1[i]!=l1[j]:
#         print("list is not a palindrome")
#     j-=1
# print("list is a palindrome")
# list is a palindrome

# l1=[1,2,3,4,5,2,1]
# j=len(l1)-1
# for i in range(len(l1)):
#     if l1[i]!=l1[j]:
#         print("list is not a palindrome")
#     j-=1
# print("list is a palindrome")
# wrong output:
# list is not a palindrome
# list is not a palindrome
# list is a palindrome

# l1=[1,2,3,4,3,2,1]
# l1=[1,2,3,4,5,2,1]  #list is not a palindrome
# j=len(l1)-1
# for i in range(len(l1)):
#     if l1[i]!=l1[j]:
#         print("list is not a palindrome")
#         break
#     j-=1
# else:
#     print("list is a palindrome")
# o/p:list is a palindrome

# 7. wap to shift all the zero's to right side and one's to left side?(without creating empty list)
# l1=[1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0]
# print(l1)
# cnt=0
# for i in l1:
#     if i==1:
#         cnt+=1
# print("total one's in l1:",cnt)
# for i in range(len(l1)):
#     if i<cnt:
#         l1[i]=1
#     else:
#         l1[i]=0
# print(l1)
# o/p:[1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0]
# total one's in l1: 6
# [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# or

# l1=[1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0]
# c=l1.count(1)
# l1=[1]*c+[0]*(len(l1)-c)
# print(l1)
# o/p: [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# or

# l1=[1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0]
# l1=[1]*l1.count(1)+[0]*l1.count(0)
# print(l1)
# o/p: [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]











# finding second max ele present in a given list?
# l1=[1,4,36,100,3]
# l1.sort()
# m=l1[-1]
# for i in range(len(l1)-1,-1,-1):
#     if l1[i]!=m:
#         print(l1[i])
#         break
# o/p: 36

# or

# l1=[1,4,36,100,3,100]
# l1.sort()
# print(l1)
# m=l1[-1]
# for i in range(len(l1)-1,-1,-1):
#     if l1[i]!=m:
#         print(l1[i])
#         break
# o/p: [1, 3, 4, 36, 100, 100]
# 36

# to find the nth largest
# l1=[1,4,36,100,3,100,100,4,36]
# l1.sort()
# print(l1)
# n=int(input("n: "))
# c=0
# m=l1[-1]
# for i in range(len(l1)-1,-1,-1):
#     if l1[i]!=m:
#         m=l1[i]
#         c+=1
#     if c==n-1:
#             print(l1[i])
#             break
    
# o/p:
# [1, 3, 4, 4, 36, 36, 100, 100, 100]
# n: 1
# 100
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 4, 36, 36, 100, 100, 100]
# n: 2
# 36
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 4, 36, 36, 100, 100, 100]
# n: 3
# 4
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 4, 36, 36, 100, 100, 100]
# n: 4
# 3
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 4, 36, 36, 100, 100, 100]
# n: 5
# 1
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 4, 36, 36, 100, 100, 100]
# n: 6
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"


# or

# l1=[1,4,36,100,3,100,4,100]
# l1=list(set(l1))
# l1.sort()
# print(l1)
# n=int(input("n: "))
# print(l1[-n])

# o/p:
# [1, 3, 4, 36, 100]
# n: 1
# 100
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 36, 100]
# n: 2
# 36
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 36, 100]
# n: 3
# 4
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 36, 100]
# n: 4
# 3
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 36, 100]
# n: 5
# 1
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# [1, 3, 4, 36, 100]
# n: 6
# Traceback (most recent call last):
#   File "d:\python programming\list_programs.py", line 183, in <module>
#     print(l1[-n])
#           ~~^^^^
# IndexError: list index out of range
# PS D:\python programming> 



# creating user input list?
# l=[]
# for i in range(5):
#     l.append(int(input()))


# n=int(input())
# l1=[int(input()) for i in range(n)]
# print(l1)

# l2=list(map(int,input().split()))
# print(l2)
# o/p; 1 2 3 4 5 6 7
# [1, 2, 3, 4, 5, 6, 7]

# n=int(input('n: '))
# l2=list(map(int,input().split()))[:n]
# print(l2)

# o/p:
# n: 3
# 1 2 3 4 5 6 7
# [1, 2, 3]


'''22-04-26'''

'''Sum of list elements '''
# n = int(input("n:"))
# l1 = eval(input())[:n]
# res =0
# for i in l1:
#     if type(i) != str:
#         res+=i
# print(res)

''' sum of given element'''
# l1 = [1,2,4,8,2,7,3,9,3,3,5,3]
# res =0
# target = int(input("target: "))
# for i in l1:
#     if i==target:
#         res+=i
# print(res)
'''or'''
# l1 = [1,2,4,8,2,7,3,9,3,3,5,3]
# target = int(input("target: "))
# res = l1.count(target)*target
# print(res)


'''Multiple of target'''
# l1 = [1,2,4,8,2,7,3,6,12,9]
# target = int(input("target: "))
# res=0
# for i in l1:
#     if i%target==0:
#         res+=i
# print(res)
'''or'''
# l1 = [1,2,4,8,2,7,3,6,12,9]
# target = int(input("target: "))
# res=sum([i for i in l1 if i%target==0])
# print(res)

'''Removing or eliminating the target element from list'''
# l1=[1,2,3,4,5,1,1,1,2,7,8,7]  # Inplace algorithm
# target = int(input("target: "))
# for i in l1:
#     if i==target:
#         l1.remove(i)
# print(l1)
'''Fails test caces'''
'''or'''
# l1=[1,2,3,4,5,1,1,1,2,7,8,7]    # Outplace algorithm
# target = int(input("target: "))
# res=[]
# for i in l1:
#     if i!=target:
#         res.append(i)
# print(res)

# l1=[1,1,1,1,7,2,3,4,5,1,1,1,2,7,8,7,1,1,1,7,7,7]  # Inplace algorithm
# target = int(input("target: "))
# i=0
# while i<len(l1):
#     if l1[i] == target:
#         l1.remove(l1[i])
#     else:
#         i+=1
# print(l1)

# l1=[1,1,1,2,3,4,5,1,1,1,2,7,8,7,1,1,1]    
# target = int(input("target: "))
# count=0
# while True:
#     if l1.count(target)>0:
#         l1.remove(target)
#     else:
#         break
#     count+=1
# print(l1)
# print(count)


# 23-04-26
# program to rotate the list to left side for n number of times?
# l=[11,22,33,44,55]
# n=int(input("enter the number of rotations"))
# for _ in range(n):
#     temp=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[len(l)-1]=temp
#     print(l)
# o/p:
# enter the number of rotations5
# [22, 33, 44, 55, 11]
# [33, 44, 55, 11, 22]
# [44, 55, 11, 22, 33]
# [55, 11, 22, 33, 44]
# [11, 22, 33, 44, 55]


# number of times the original lis is repeated
# l=[11,22,33,44,55]
# l1=l.copy()
# count=0
# n=int(input("enter the number of rotations"))
# for _ in range(n):
#     temp=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[len(l)-1]=temp
#     if l1==l:
#         count+=1      
# print(l)
# print(count)
# o/p:
# enter the number of rotations5
# [11, 22, 33, 44, 55]
# 1
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# enter the number of rotations2
# [33, 44, 55, 11, 22]
# 0
# PS D:\python programming> & C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe "d:/python programming/list_programs.py"
# enter the number of rotations10
# [11, 22, 33, 44, 55]
# 2


# program to rotate the list to right side for n number of times?
# l=['a','b','c','d','e']
# n=int(input("enter the number of rotations: "))
# for _ in range(n):
#     temp=l[len(l)-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=temp
#     print(l)

# enter the number of rotations: 5
# ['e', 'a', 'b', 'c', 'd']
# ['d', 'e', 'a', 'b', 'c']
# ['c', 'd', 'e', 'a', 'b']
# ['b', 'c', 'd', 'e', 'a']
# ['a', 'b', 'c', 'd', 'e']


# l=['a','b','c','d','e']
# l1=l.copy()
# c=0
# n=int(input("enter the number of rotations: "))
# for _ in range(n):
#     temp=l[len(l)-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=temp
#     if l==l1:
#         c+=1
# print(l)
# print(c)
# o/p:

# enter the number of rotations: 5
# ['a', 'b', 'c', 'd', 'e']
# 1

# enter the number of rotations: 10
# ['a', 'b', 'c', 'd', 'e']
# 2

# enter the number of rotations: 15
# ['a', 'b', 'c', 'd', 'e']
# 3

# wap to count the frequency of each element present in the given list?

# l=[1,2,'a',3,2,5,'b','a',4,8,1,'a','c',3,7,2,'d',3,'c']
# for i in range(len(l)):
#     count=0
#     for j in range(len(l)):
#         if l[j]==l[i]:
#             count+=1
#     print(l[i]," is repeated ",count)

# or

# l1=[1,2,'a',3,2,5,'b','a',4,8,1,'a','c',3,7,2,'d',3,'c']
# d1={}
# for i in l1:
#     if i not in d1:
#         d1[i]=1
#     else:
#         d1[i]+=1
# print(d1)

# {1: 2, 2: 3, 'a': 3, 3: 3, 5: 1, 'b': 1, 4: 1, 8: 1, 'c': 2, 7: 1, 'd': 1}

'''Bubble sort/sinking sort
steps:
1. take 2 variables i and j
2.if'''

# def bubble_sort(l1):
#     for i in range(len(l1)):
#         for j in range(i+1,len(l1)):
#             if l1[i]>l1[j]:
#                 l1[i],l1[j]=l1[j],l1[i]
# l1=[3,6,1,2,4]
# print("Bubble sort")
# print("before sorting",l1)
# bubble_sort(l1)
# print("after sorting",l1)
# o/p:
# Bubble sort
# before sorting [3, 6, 1, 2, 4]
# after sorting [1, 2, 3, 4, 6]

'''Linear Search Algorithm(it works on unsorted arrays also)'''
# search the element in given list?

# def linear_search(l1,n):
#     for i in range(len(l1)):
#         if l1[i]==n:
#             print("value found")
#             break
#     else:
#         print("value not found")
# l1=[2,3,55,6,8,2,9,0]
# n=int(input("Enter the element to be search: "))
# linear_search(l1,n)

# o/p:
# Enter the element to be search: 2
# value found

# Enter the element to be search: 1111
# value not found

# or

# l=[1,2,4,6,2,7,8,9]
# target=int(input("key:"))
# found=False
# for i in range(len(l)):
#     if l[i]==target:
#         print(f"{target} is found at the index {i}")
#         found=True
#         break
# if not found:
#     print(f"{target} is not found")

# o/p:
# key:12
# 12 is not found
# key:2
# 2 is found at the index 1

'''second occurance of an element present in list'''
# l=[1,2,4,6,2,7,8,9,4]
# target=int(input("key:"))
# c=0
# found=False
# for i in range(len(l)):
#     if l[i]==target:
#         c+=1
#         if c==2:
#             print(f"{target} is second occurace found at the index {i}")
#             found=True
#             break
# if not found:
#     print(f"{target} is not found")
# o/p:
# key:4
# 4 is second occurace found at the index 8

'''nth occurance'''
# l=[1,2,4,6,2,7,8,9,4,5,4,3,1]
# target=int(input("key:"))
# n=int(input("n: "))
# c=0
# found=False
# for i in range(len(l)):
#     if l[i]==target:
#         c+=1
#         if c==n:
#             print(f"{target} is second occurace found at the index {i}")
#             found=True
#             break
# if not found:
#     print(f"{target}'s {n}th occurance is not found")
# o/p:

# key:1
# n: 1
# 1 is second occurace found at the index 0
# key:1
# n: 2
# 1 is second occurace found at the index 12



'''reverse the list without using any built-in methods?(it is out-of-place algorithm)'''
# l=[1,2,3,4]
# res=[]
# for i in range(len(l)-1,-1,-1):
#     res+=[l[i]]
# print(res)

# o/p: [4, 3, 2, 1]

# or

# l=[1,2,3,4]
# l=l[::-1]
# print(l)
# o/p: [4, 3, 2, 1]

'''reverssing a list (two pointer approach)'''
# l=[10,20,30,40]
# i=0
# j=len(l)-1
# while i<j:
#     l[i],l[j]=l[j],l[i]
#     i+=1
#     j-=1
# print(l)

#   [40, 30, 20, 10]
            
# or

# l=[10,20,30,40,50]
# i=0
# j=len(l)-1
# while i<j:
#     l[i],l[j]=l[j],l[i]
#     i+=1
#     j-=1
# print(l)    

# [50, 40, 30, 20, 10]



# def isEven(n):
#     if i%2==0:
#         print("even")
# isEven(0)


'''Binary Search Algorithm (works for only sorted array)'''
# l=[10,20,30,40,50,60,70]
# n=int(input("n: "))
# first=0
# last=len(l)-1
# found=False
# while first<=last:
#     mid=(first+last)//2
#     if n<l[mid]:
#         last=mid-1
#     elif n>l[mid]:
#         first=mid+1
#     else:
#         print(f'{n} is found at index {mid}')
#         found=True
#         break
# if not found:
#     print(f'{n} is not found')

# n: 10
# 10 is found at index 0

# n: 70
# 70 is found at index 6

# n: 12
# 12 is not found



'''wap to accept list of non negative integer And during iteration find the product of all the elements excluding the number'''
# l=[2,4,6,8,10]
# res=[]
# for i in l:
#     product=1
#     for j in l:
#         if i==j:
#             continue
#         else:
#             product*=j
#     res.append(product)
# print(res)  
# [1920, 960, 640, 480, 384]


# l=[2,4,6,8,10]
# prod=1
# for i in l:
#     prod*=i
# print([prod//i for i in l])
# [1920, 960, 640, 480, 384]

'''display the first and last index of given target value'''

# l=[1,3,5,3,7,9,3,2]
# first_index=-1
# last_index=-1
# target=int(input("Target value is: "))
# for i in range(len(l)):
#     if l[i]==target:
#         first_index=i
#         break
# for j in range(len(l)-1,-1,-1):
#     if l[j]==target:
#         last_index=j
#         break
# print("First index",first_index)
# print("last index",last_index)

# o/p:
# Target value is: 3
# First index 1
# last index 6

# Target value is: 7
# First index 4
# last index 4

# Target value is: 10
# First index -1
# last index -1

# or

# def first_last_index(target,l):
#     f_i=-1
#     l_i=-1
#     for i in range(len(l)):
#         if l[i]==target:
#             if f_i==-1:
#                 f_i=i
#             l_i=i
#     return f_i,l_i
# l=[1,3,5,3,7,9,3,2]
# target=int(input("Target is: "))
# f,l=first_last_index(target,l)
# print(f"First Index of {target} is",f)
# print(f"last Index of {target} is",l)

# o/p:
# Target is: 4
# First Index of 4 is -1
# last Index of 4 is -1



'''swaping the characters and numbers given in string if any special character is present in list no need to change its position.'''
'''
1.count the total chars nd numbers in the list.
2.create a empty list based on count
3.insert all the chars and numbers to new list.
4.reverse the new list.
5.merge to the original list if the chars is chars or numbers.'''

# l=['2','l','@','3','u','h','$','1','a','7','r','#','r']
# cnt=0
# for i in range(len(l)):
#     if ord(l[i]) >=97 and ord(l[i]) <=122 or ord(l[i]) >=65 and ord(l[i]) <=90 or ord(l[i]) >=48 and ord(l[i])<=57:
#         cnt+=1
# print(cnt)

# new_list=[0]*cnt
# print(new_list)
# print()

# k=0
# for i in range(len(l)):
#     if ord(l[i]) >=97 and ord(l[i]) <=122 or ord(l[i]) >=65 and ord(l[i]) <=90 or ord(l[i]) >=48 and ord(l[i])<=57:
#         new_list[k]=l[i]
#         k+=1
# print(new_list)
# print()
# new_list=new_list[::-1]
# print(new_list)
# print()

# k=0
# for i in range(len(l)):
    # if ord(l[i]) >=97 and ord(l[i]) <=122 or ord(l[i]) >=65 and ord(l[i]) <=90 or ord(l[i]) >=48 and ord(l[i])<=57:
#         l[i]=new_list[k]
#         k+=1
# print(l)

# o/p:
# 10
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# ['2', 'l', '3', 'u', 'h', '1', 'a', '7', 'r', 'r']

# ['r', 'r', '7', 'a', '1', 'h', 'u', '3', 'l', '2']

# ['r', 'r', '@', '7', 'a', '1', '$', 'h', 'u', '3', 'l', '#', '2']

'''or'''

# l=['2','l','@','3','u','h','$','1','a','7','r','#','r']
# print(l)
# print()
# def find_char_or_num(val):
#     if ord(val) >=97 and ord(val) <=122 or ord(val) >=65 and ord(val) <=90 or ord(val) >=48 and ord(val)<=57:
#         return True
#     else:
#         return False

# j=len(l)-1
# for i in range(len(l)//2):
#     if find_char_or_num(l[i]) and find_char_or_num(l[j]):
#         l[i],l[j]=l[j],l[i]
#     j-=1
# print(l)


'''wap to accept list of non negative integers and divide thelist into two parts nd place first half to second half , second half to first half'''








'''program to find sum of all prime numbers present in a given list using functions.'''


# l=[1,2,11,8,6,9,15,17,2,13,21]
# def isprime(val):
#     c=0
#     for i in range(2,val//2+1):
#         if val%i==0:
#             c+=1
#             break
#     if c==0:
#         return True
#     return False
# print(isprime(11))
# print(isprime(9)) 
# print(isprime(71)) 
# print(isprime(-1))



# def isprime(num):
#     if num==1:
#         return False
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 return False
#         return True
# l=[1,2,11,8,6,9,15,17,2,13,21,5]
# cnt=0
# for i in l:
#     if isprime(i):
#         cnt+=i
# print("Sum of all the prime numbers in a given list is: ",cnt)

# o/p: Sum of all the prime numbers in a given list is:  50


'''find the super digit of sum of all the even numbers given in the list'''

# l=[2,12,19,23,54,102,654,10,199]
# c=0
# n=0
# for i in l:
#     if i%2==0:
#         n+=i
#         c+=1
# print(n)
# sum=0
# for i in range(c):
#     rem=n%10
#     sum+=rem
#     n=n//10
# print(sum)
# o/p: 834
# 15

# l=[2,12,19,23,54,102,654,10,199]
# res=0
# for i in l:
#     if i%2==0:
#         res+=i
# print(res)
# while res>=10:
#     temp=res
#     s=0
#     while temp!=0:
#         rem=temp%10
#         s=s+rem
#         temp=temp//10
#     # print(s)
#     res=s
# print(res)
# o/p:
# 834
# 6


'''display all the pairs of given target value'''

# l=[1,2,4,2,6,4,8,6,9,3,8,0,3,4,6,8,7,9,2,4,8,3]
# target=int(input("Enter targe value:"))
# res=[]
# for i in l:
#     for j in l:
#         if i+j==target:
#             pair=[i,j]
#             if pair in res:
#                 continue
#             else:
#                 res.append(pair)
# print(res)

# or

# l=[1,2,4,2,6,4,8,6,9,3,8,0,3,4,6,8,7,9,2,4,8,3]
# target=int(input("Enter targe value:"))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print(l[i],l[j])

# o/p:Enter targe value:9
# [[1, 8], [2, 7], [6, 3], [8, 1], [9, 0], [3, 6], [0, 9], [7, 2]]

'''display the intersection of two lists'''

# l1=[1,2,5,3,7,6]
# l2=[5,7,10,11,15,1]
# res=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             res.append(i)
# print("The intersection elements:",res)
# o/p: The intersection elements: [1, 5, 7]


'''display the union of two lists'''
# l1=[1,2,5,3,7,6,1,2]
# l2=[5,7,10,11,15,1]
# res=[]
# for i in l1:
#     if i not in res:
#         res.append(i)
# for j in l2:
#     if j not in l1:
#         res.append(j)
# print(res)

# or

# l1=[1,2,5,3,7,6,1,2]
# l2=[5,7,10,11,15,1]
# res=[]
# for i in l1:
#     if i not in res:
#         res+=[i]
# for i in l2:
#     if i not in l1:
#         res+=[i]
# print(res)
# o/p: [1, 2, 5, 3, 7, 6, 10, 11, 15]


'''display the duplicate elements present in a list'''

# l=[1,2,3,4,5,1,5,6,4,1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j]:
#             print(l[i],end=' ')
# o/p: 1 1 4 5 1 


'''wap to build index grid by accepting two input values'''

Row=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
r=[]
for i in range(Row):
    c=[]
    for j in range(col):
        c.append((i,j))
    r+=[c]
print(r)

# o/p: [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]

# or

val1=int(input("val1: "))
val2=int(input("val2: "))
res=[]
for i in range(val1):
    l=[]
    for j in range(val2):
        l+=[(i,j)]
    res+=[l]
print(res)


