# 1.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(val,end=' ')
#     print()
#     val+=1
# n: 4
#       1 
#     2 2 2 
#   3 3 3 3 3 
# 4 4 4 4 4 4 4 

# 2.
# n=int(input("n: "))
# for i in range(n):
#     val=1
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(val,end=' ')
#         val+=1
#     print()
# n: 4
#       1 
#     1 2 3 
#   1 2 3 4 5 
# 1 2 3 4 5 6 7

# 3.
# n=int(input("n: "))
# val=4
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(val,end=' ')
#     print()
#     val-=1
# n: 4
#       4 
#     3 3 3
#   2 2 2 2 2
# 1 1 1 1 1 1 1

# 4.
# n=int(input("n: "))
# for i in range(n):
#     val=4
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(val,end=' ')
#         val-=1
#         if val<0:
#             val=4
#     print()
# n: 4
#       4 
#     4 3 2
#   4 3 2 1 0
# 4 3 2 1 0 4 3
# 5.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(chr(val),end=' ')
#     print()
#     val+=1
# n: 4
#       A 
#     B B B 
#   C C C C C 
# D D D D D D D 

# 6.
# n=int(input("n: "))
# val=ord('D')
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(chr(val),end=' ')
#     print()
#     val-=1
# n: 4
#       D 
#     C C C
#   B B B B B
# A A A A A A A

# 7.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(n-i)-1):
#         print(val,end=' ')
#     print()
#     val+=1
#     if val>3:
#         val=1
# n: 4
# 1 1 1 1 1 1 1 
#   2 2 2 2 2
#     3 3 3
#       1


# 8.
# n=int(input("n: "))
# for i in range(n):
#     val=1
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(n-i)-1):
#         print(val,end=' ')
#         val+=1
#     print()
#     if val>7:
#         val=1
# n: 4
# 1 2 3 4 5 6 7 
#   1 2 3 4 5
#     1 2 3
#       1

# 9.
# n=int(input("n: "))
# val=ord('D')
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(n-i)-1):
#         print(chr(val),end=' ')
#     print()
#     val-=1
# n: 4
# D D D D D D D 
#   C C C C C 
#     B B B 
#       A 

# 10.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(chr(val),end=' ')
#         val+=1
#     print()
# n: 4
#       A 
#     B C D 
#   E F G H I 
# J K L M N O P 

# 11.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print(val,end=' ')
#         val+=1
#         if val>9:
#             val=1
#     print()
# n: 4
#       1 
#     2 3 4 
#   5 6 7 8 9 
# 1 2 3 4 5 6 7

# 12.
# n=int(input("n: "))
# val=ord('Z')
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(n-i)-1):
#         print(chr(val),end=' ')
#         val-=1
#     print()
# n: 4
# Z Y X W V U T 
#   S R Q P O
#     N M L
#       K

# # 13.
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         if i%2==0:
#             print(val,end=' ')
#         else:
#             print("*",end=' ')
#     print()
#     if i%2==0:
#         val+=1
# n: 4
#       1 
#     * * * 
#   2 2 2 2 2 
# * * * * * * *

# 15.
# n=int(input("n: "))
# val1=1
# for i in range(n):
#     val2=ord('A')
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         if i%2==0:
#             print(val1,end=' ')
#         else:
#             print(chr(val2),end=' ')
#             val2+=1
#     print()
#     if i%2==0:
#         val1+=1

# n: 4
#       1 
#     A B C
#   2 2 2 2 2
# A B C D E F G

# 16.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(n-i)-1):
#         print(chr(val),end=' ')
#         val+=1
#     print()
#     val=ord('A')
# n: 4
# A B C D E F G 
#   A B C D E 
#     A B C 
#       A 

# 18.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(n-i)-1):
#         print(chr(val),end=' ')

#     print()
#     val+=1

# n: 4
# A A A A A A A 
#   B B B B B 
#     C C C 
#       D


# 13
# 17.
# n=int(input("n: "))
# val=1
# for i in range(1,n+1):
#     print(" "*(n-i),end=' ')
#     for j in range(2*(n-i)-1):
#         if j%2==0:
#             print(val,end=' ')
#             val+=1
#         else:
#             print('*',end=' ')
#     print()






# class assignment
# 1.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=1
#     for j in range(n-abs(i)):
#         print(val,end=' ')
#         val+=1
#     print()
# n: 3
# 1 
# 1 2
# 1 2 3
# 1 2
# 1

# 2.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=ord('A')
#     for j in range(n-abs(i)):
#         print(chr(val),end=' ')
#         val+=1
#     print()
# n: 3
# A 
# A B
# A B C
# A B
# A

# 3.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=ord('C')
#     for j in range(n-abs(i)):
#         print(chr(val),end=' ')
#         val-=1
#     print()
# n: 3
# C 
# C B
# C B A
# C B
# C

# 4.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=3
#     for j in range(n-abs(i)):
#         print(val,end=' ')
#         val-=1
#     print()
#     n: 3
# 3 
# 3 2
# 3 2 1
# 3 2
# 3

# 5.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=1
#     for j in range(abs(i)):
#         print(' ',end=' ')
#     for k in range(n-abs(i)):
#         print(val,end=' ')
#         val+=1
#     print()
# n: 3
#     1 
#   1 2 
# 1 2 3 
#   1 2 
#     1

# 6.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=ord('A')
#     for j in range(abs(i)):
#         print(' ',end=' ')
#     for k in range(n-abs(i)):
#         print(chr(val),end=' ')
#         val+=1
#     print()
# n: 3
#     A 
#   A B
# A B C
#   A B
#     A

# 7.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=ord('C')
#     for j in range(abs(i)):
#         print(' ',end=' ')
#     for k in range(n-abs(i)):
#         print(chr(val),end=' ')
#         val-=1
#     print()
# n: 3
#     C 
#   C B 
# C B A 
#   C B
#     C

# 8.
# n=int(input("n: "))
# for i in range(n-1,-n,-1):
#     val=3
#     for j in range(abs(i)):
#         print(' ',end=' ')
#     for k in range(n-abs(i)):
#         print(val,end=' ')
#         val-=1
#     print()
# n: 3
#     3 
#   3 2
# 3 2 1
#   3 2
#     3

# 9.
# n=int(input("n: "))
# val=1
# for i in range(n-1,-n,-1):
#     for j in range(n-abs(i)):
#         if i%2==0:
#             print(val,end=' ')
#         else:
#             print('*',end=' ')
#     print()
#     if i%2==0:
#         val+=1
# n: 3
# 1 
# * *
# 2 2 2
# * *
# 3

# 10.
# n=int(input("n: "))
# val=ord('A')
# for i in range(n-1,-n,-1):
#     for j in range(abs(i)):
#         print(' ',end=' ')
#     for k in range(n-abs(i)):
#         if i%2==0:
#             print(chr(val),end=' ')
#         else:
#             print('*',end=' ')
#     print()
#     if i%2==0:
#         val+=1
# n: 3
#     A 
#   * *
# B B B
#   * *
#     C