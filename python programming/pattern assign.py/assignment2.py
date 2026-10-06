# 1.
# n=int(input("n: "))
# for i in range(n):
#     val=ord('D')
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
                
#     print()

#     n: 4
#       D 
#     D C 
#   D C B 
# D C B A 

# 2.
# n=int(input("n: "))
# for i in range(n):
#     val=ord('Z')
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
                
#     print()
# n: 4
#       Z 
#     Z Y 
#   Z Y X 
# Z Y X W 

# 3.
# n=int(input("n: "))
# val=ord('Z')
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')
                
#     print()
#     val-=1

# n: 4
#       Z 
#     Y Y 
#   X X X 
# W W W W

# 4.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')     
#     print()
#     val+=1

# n: 4
#       1 
#     2 2 
#   3 3 3 
# 4 4 4 4

# 5.
# n=int(input("n: "))
# for i in range(n):
#     val=1
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
                
#     print()

# n: 4
#       1 
#     1 2
#   1 2 3
# 1 2 3 4

# 6.
# n=int(input("n: "))
# val=4
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')     
#     print()
#     val-=1
# n: 4
#       4 
#     3 3 
#   2 2 2 
# 1 1 1 1


# 7.
# n=int(input("n: "))
# for i in range(n):
#     val=4
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')     
#     print()
# n: 4
#       4 
#     4 3
#   4 3 2
# 4 3 2 1

# 8.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')     
#     print()
#     val+=1

# n: 4
# 1 1 1 1 
# 2 2 2   
# 3 3     
# 4 

# 9.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     val=1
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(val,end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')   
#             val=1  
#     print()

# n: 4
# 1 2 3 4 
# 1 2 3   
# 1 2     
# 1

# 10.
# n=int(input("n: "))
# for i in range(n):
#     val=4
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(val,end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')   
#             val=4 
#     print()

# n: 4
# 4 3 2 1 
# 4 3 2   
# 4 3     
# 4

# 11.
# n=int(input("n: "))
# for i in range(n):
#     val=ord('A')
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')   
#             val=ord('A')
#     print()

# n: 4
# A B C D 
# A B C
# A B
# A

# 12.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(chr(val),end=' ')

#         else:
#             print(' ',end=' ')   
#     print()
#     val+=1

# n: 4
# A A A A 
# B B B   
# C C     
# D


# 13.
# n=int(input("n: "))
# val=ord('Z')
# for i in range(n):
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(chr(val),end=' ')

#         else:
#             print(' ',end=' ')   
#     print()
#     val-=1

# n: 4
# Z Z Z Z 
# Y Y Y   
# X X     
# W 

# 14.
# n=int(input("n: "))
# for i in range(n):
#     val=ord('Z')
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ') 

#     print()

# n: 4
# Z Y X W 
# Z Y X
# Z Y
# Z

# 15.
# n=int(input("n: "))
# val=ord('D')
# for i in range(n):
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(chr(val),end=' ')
            
#         else:
#             print(' ',end=' ') 
#     print()
#     val-=1
# n: 4
# D D D D 
# C C C
# B B
# A

# 16.
# n=int(input("n: "))

# for i in range(n):
#     val=ord('D')
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(chr(val),end=' ')
#             val-=1

#         else:
#             print(' ',end=' ') 
#     print()
# n: 4
# D C B A 
# D C B
# D C
# D  

# 17
# n=int(input("n: "))
# val=1
# p=True
# for i in range(n):
#     for j in range(n):
#         if (i+j)<=n-1:
#             if p:
#                 print(val,end=' ')
#                 val+=1
#                 p=False
#             else:
#                 print('*',end=' ')
#                 p=True
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# 1 * 2 * 
# 3 * 4   
# * 5     
# *     



# 18.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if (i+j)<=n-1:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ') 
#     print()
# n: 4
# A B C D 
# E F G
# H I
# J


# 19.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if (i+j)==n-1:
#             print(val,end=' ')
#             val+=1
#         else:
#             print(' ',end=' ') 
#     print()
# n: 4
#       1 
#     2
#   3
# 4


# 20.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if (i+j)==n-1:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ') 
#     print()
# n: 4
#       A 
#     B
#   C
# D

# 21.
# n=int(input("n: "))
# val=4
# for i in range(n):
#     for j in range(n):
#         if (i+j)==n-1:
#             print(val,end=' ')
#             val-=1
#         else:
#             print(' ',end=' ') 
#     print()

# n: 4
#       4 
#     3
#   2
# 1

# 22.
# n=int(input("n: "))
# val=ord('Z')
# for i in range(n):
#     for j in range(n):
#         if (i+j)==n-1:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ') 
#     print()
# n: 4
#       Z 
#     Y   
#   X
# W

# 23.
# n=int(input("n: "))
# val=ord('D')
# for i in range(n):
#     for j in range(n):
#         if (i+j)==n-1:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ') 
#     print()

# n: 4
#       D 
#     C
#   B
# A

# 24.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if (i+j)==n-1:
#             if i%2==0:
#                 print(val,end=' ')
#                 val+=1
#             else:
#                 print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
#       1 
#     *
#   2
# *

# 25.
# n=int(input("n: "))
# val=ord('A')    
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')            
#     print()
#     val+=1
# n: 4
#       A 
#     B B 
#   C C C 
# D D D D 

# 26.
# n=int(input("n: "))

# for i in range(n):
#     val=ord('A')
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(chr(val),end=' ')
#             val+=1

#         else:
#             print(' ',end=' ')  
#             val=ord('A') 
#     print()

# n: 4
#       A 
#     A B
#   A B C
# A B C D


# 27.
# n=int(input("n: "))
# val=ord('D')    
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')            
#     print()
#     val-=1
# n: 4
#       D 
#     C C 
#   B B B 
# A A A A 