# 1.
# n=int(input("n: "))
# for i in range(n):
#     val=i+1
#     for j in range(n):
#         if i>=j:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# 1       
# 2 2     
# 3 3 3   
# 4 4 4 4 

# (or)

# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')
#     val+=1
#     print()
# n: 4
# 1       
# 2 2     
# 3 3 3   
# 4 4 4 4 

# 2.
# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         val=j+1
#         if i>=j:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# 1       
# 1 2     
# 1 2 3   
# 1 2 3 4 

# 3.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=' ')
#             val+=1
#             if val>9:
#                 val=1
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# 1       
# 2 3     
# 4 5 6   
# 7 8 9 1 

# 4.
# n=int(input("n: "))
# for i in range(n):
#     val=ord('A')+i
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# A       
# B B     
# C C C   
# D D D D



# 5.
# n=int(input("n: "))
# for i in range(n):
#     val=ord('A')
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# A       
# A B     
# A B C   
# A B C D

# 6.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# A       
# B C
# D E F
# G H I J

# 7.
# n=int(input("n: "))
# val=4
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#     val-=1

# n: 4
# 4       
# 3 3
# 2 2 2
# 1 1 1 1

# 8.
# n=int(input("n: "))
# for i in range(n):
#     val=4
#     for j in range(n):
#         if i>=j:
#             print(val,end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# 4       
# 4 3
# 4 3 2
# 4 3 2 1

# 9.
# n=int(input("n: "))
# val=ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#     val-=1

# n: 4
# Z       
# Y Y     
# X X X   
# W W W W

# 10.
# n=int(input("n: "))
# val=ord("D")
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#     val-=1
# n: 4
# D       
# C C
# B B B
# A A A A

# 11.
# n=int(input("n: "))
# for i in range(n):
#     val=ord("D")
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# D       
# D C
# D C B
# D C B A

# 12.
# n=int(input("n: "))
# val=ord('A')+n-1
# for i in range(n):
#     for j in range(i+1):
#         if i>=j:
#             print(chr(val),end=' ')
#             val-=1
#             if val<ord('A'):
#                 val=ord('A')+n-1

#         else:
#             print(' ',end=' ')
#     print()

# n: 5
# E 
# D C
# B A E
# D C B A
# E D C B A

# 13.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#     val+=1
# n: 4
# A A A A 
#   B B B 
#     C C 
#       D   

# 14.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#             val=ord('A')
#     print()
# n: 4
# A B C D 
#   A B C 
#     A B 
#       A 

# 15.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# A B C D 
#   E F G 
#     H I 
#       J 

# 16.
# n=int(input("n: "))
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i<=j:
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')
#             val+=1

#     print()

# n: 4
# 1 1 1 1 
#   2 2 2 
#     3 3 
#       4 

# 17.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#             val=1

#     print()

# n: 4
# 1 2 3 4 
#   1 2 3
#     1 2
#       1



# 18.
# n=int(input("n: "))
# val=4
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#             val=4

#     print()


# n: 4
# 4 3 2 1 
#   4 3 2
#     4 3
#       4

# 19
# n=int(input("n: "))
# for i in range(n):
#     val=ord('D')
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')
#             val-=1
#     print()

# n: 4
# D D D D 
#   C C C 
#     B B 
#       A 



# 20.
# n=int(input("n: "))
# val=ord('D')
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#             val=ord('D')

#     print()


# n: 4
# D C B A 
#   D C B
#     D C
#       D

# 21.

# n=int(input("n: "))
# val=ord('Z')
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#     print()
#     val=ord('Z')-(i+1)

# n: 4
# Z Y X W 
#   Y X W
#     X W
#       W

# (or)

# n=int(input("n: "))
# for i in range(n):
#     val=ord('Z')-i
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
    # print()

# n: 4
# Z Y X W 
#   Y X W
#     X W
#       W
# 22.

# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# 1       
#   2     
#     3   
#       4 

# 23.
# n=int(input("n: "))
# val=4
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# 4       
#   3     
#     2   
#       1

# 24.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# A       
#   B
#     C
#       D

# 25.
# n=int(input("n: "))
# val=ord('D')
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# D       
#   C
#     B
#       A

# 26.
# n=int(input("n: "))
# val=ord('z')
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=' ')
#             val-=1
#         else:
#             print(' ',end=' ')
#     print()
# n: 4
# z       
#   y
#     x
#       w

# 27.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             if i%2==0:
#                 print(val,end=' ')
#                 val+=1
#             else:
#                 print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n: 4
# 1       
#   *     
#     2   
#       * 

# 28.
