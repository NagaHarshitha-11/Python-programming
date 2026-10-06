# # row=int(input("row: "))
# # col=int(input("col: "))
# # for i in range(row):
# #     for j in range(col):
# #         print("*",end=' ')
# #     print()

# # output:
# # row: 3
# # col: 3
# # * * *
# # * * *  
# # * * * 

# # r=int(input("r: "))
# # c=int(input("c: "))
# # val=1
# # for i in range(r):
# #     for j in range(c):
# #         print(val,end=' ')
# #     print()
    
# # o/:p
# # r: 2
# # c: 3
# # 1 1 1 
# # 1 1 1 


# # r=int(input("r: "))
# # c=int(input("c: "))
# # val=1
# # for i in range(r):
# #     for j in range(c):
# #         print(val,end=' ')
# #         val+=1
# #     print()

# # o/p:
# # r: 4
# # c: 4
# # 1 2 3 4 
# # 5 6 7 8 
# # 9 10 11 12 
# # 13 14 15 16 


# # r=int(input("r: "))
# # c=int(input("c: "))
# # width=len(str(r*c))
# # print(str(width),end=" ")

# # o/p:
# # r: 10    (10*10=100 in 100 it displays digits that is 3)
# # c: 10
# # 3 


# r=int(input("r: "))
# c=int(input("c: "))
# val=1
# w=len(str(r*c))
# for i in range(r):
#     for j in range(c):
#         print(str(val).zfill(w),end=" ")
#         val+=1
#     print()  

# # o/p:
# # r: 4
# # c: 4
# # 01 02 03 04 
# # 05 06 07 08 
# # 09 10 11 12 
# # 13 14 15 16 

# # r=int(input("r: "))
# # c=int(input("c: "))
# # val=1
# # for i in range(r):
# #     for j in range(c):
# #         print(val,end=' ')
# #         val+=1
# #         if val>9:
# #           val=1
# #     print() 
# # o/p:
# # r: 4
# # c: 6
# # 1 2 3 4 5 6 
# # 7 8 9 1 2 3
# # 4 5 6 7 8 9
# # 1 2 3 4 5 6
  


# # r=int(input("r: "))
# # c=int(input("c: "))
# # val=1
# # w=len(str(r*c))
# # for i in range(r):
# #     for j in range(c):
# #         print(str(val).zfill(w),end=" ")
# #     print() 
# #     val+=1
# #     if val>9:
# #         val=1

# # o/p:
# # r: 12
# # c: 3 
# # 01 01 01 
# # 02 02 02 
# # 03 03 03
# # 04 04 04
# # 05 05 05
# # 06 06 06
# # 07 07 07
# # 08 08 08
# # 09 09 09
# # 01 01 01
# # 02 02 02
# # 03 03 03



# # r=int(input("r: "))
# # c=int(input("c: "))
# # val=1
# # for i in range(r):
# #     if i%2==0:
# #         for j in range(c):
# #             print(val,end=' ')
# #         val+=1
# #     else:
# #         for j in range(c):
# #             print("*",end=' ')
# #     print()

# # o/p:
# # r: 5
# # c: 4
# # 1 1 1 1 
# # * * * * 
# # 2 2 2 2 
# # * * * * 
# # 3 3 3 3 


# # (or)

# # r=int(input("r: "))
# # c=int(input("c: "))
# # val=1
# # for i in range(r):
# #     for j in range(c):
# #             if i%2==0:
# #                 print(val,end=' ')  
# #             else:
# #                 print("*",end=' ')
# #     print()
# #     if i%2==0:
# #          val+=1

# # o/p:
# # r: 5
# # c: 4
# # 1 1 1 1 
# # * * * * 
# # 2 2 2 2 
# # * * * * 
# # 3 3 3 3 


# # r=int(input("r: "))
# # c=int(input("c: "))
# # val=1
# # ch='A'
# # for i in range(r):
# #     for j in range(c):
# #         if (i+j)%2==0:
# #             print(val,end=" ")
# #             val+=1
# #         else:
# #             print(ch,end=" ")
# #             ch=chr(ord(ch)+1)
# #     print()

# # o/p:
# # r: 3
# # c: 5
# # 1 A 2 B 3 
# # C 4 D 5 E 
# # 6 F 7 G 8 

# # (or)

# # r=int(input("r: "))
# # c=int(input("c: "))
# # val1,val2=1,ord("A")
# # p=True
# # for i in range(r):
# #     for j in range(c):
# #         if p:
# #             print(val1,end=" ")
# #             val1+=1
# #             p=False 
# #         else:
# #             print(chr(val2),end=" ")
# #             val2+=1
# #             p=True
# #     print()

# # o/p:

# # r: 3
# # c: 5
# # 1 A 2 B 3 
# # C 4 D 5 E 
# # 6 F 7 G 8 

# # r=int(input("r: "))
# # c=int(input("c: "))
# # val1,val2=1,ord("A")
# # p=True
# # for i in range(r):
# #     for j in range(c):
# #         if p:
# #             print(val1,end=" ")
# #             val1+=1
# #             if val1>9:
# #                 val1=1
# #             p=False 
# #         else:
# #             print(chr(val2),end=" ")
# #             val2+=1
# #             if val2>ord('Z'):
# #                 val2=ord('A')
# #             p=True
# #     print()

# # o/p:
# # r: 10
# # c: 10
# # 1 A 2 B 3 C 4 D 5 E 
# # 6 F 7 G 8 H 9 I 1 J
# # 2 K 3 L 4 M 5 N 6 O
# # 7 P 8 Q 9 R 1 S 2 T
# # 3 U 4 V 5 W 6 X 7 Y
# # 8 Z 9 A 1 B 2 C 3 D
# # 4 E 5 F 6 G 7 H 8 I
# # 9 J 1 K 2 L 3 M 4 N
# # 5 O 6 P 7 Q 8 R 9 S
# # 1 T 2 U 3 V 4 W 5 X




# # r=int(input("r: "))
# # c=int(input("c: "))
# # for i in range(r):
# #     val=1
# #     for j in range(c):
# #         if j%2==0:
# #             print(val,end=' ')
# #             val+=1
# #         else:
# #             print("*",end=' ')
# #     print()


# # o/p:
# # r: 3
# # c: 5
# # 1 * 2 * 3 
# # 1 * 2 * 3 
# # 1 * 2 * 3 

# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if i>=j:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()

# # n: 5
# # *
# # * *       
# # * * *     
# # * * * *   
# # * * * * * 


# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if i<=j:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()

# # n: 5
# # * * * * * 
# #   * * * *
# #     * * *
# #       * *
# #         *


# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if i==j:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()

# # n: 5
# # *
# #   *
# #     *
# #       *
# #         *

# # n=int(input("n: "))
# # for i in range(n):
# #     val=ord('A')
# #     for j in range(n):
# #         if i>=j:
# #             print(chr(val),end=' ')
# #             val+=1
# #         else:
# #             print(' ',end=' ')
# #     print()

# # n: 5
# # A
# # A B
# # A B C
# # A B C D
# # A B C D E

# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if (i+j)==n-1:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()

# # n: 5
# #         * 
# #       *
# #     *
# #   *
# # *

# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if (i+j)>=n-1:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()

# #     n: 5
# #         * 
# #       * * 
# #     * * * 
# #   * * * * 
# # * * * * * 

# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if (i+j)<=n-1:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()

# #     n: 5
# # * * * * * 
# # * * * *   
# # * * *     
# # * *       
# # *

# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n):
# #         if i==j:
# #             print("*",end=' ')
# #         elif i>=j:
# #             print("#",end=' ')
# #         else:
# #             print("$",end=' ')
# #     print()
# n: 5
# # * $ $ $ $ 
# # # * $ $ $ 
# # # # * $ $ 
# # # # # * $ 
# # # # # # * 


# # n=int(input("n: "))
# # for i in range(n):
# #     val1,val2=1,1
# #     for j in range(n):
# #         if i==j:
# #             print("*",end=' ')
# #         elif i>j:
# #             print(val1,end=' ')
# #             val1+=1
# #         else:
# #             print(val2,end=' ')
# #             val2+=1
# #     print()

# # n: 5
# # * 1 2 3 4 
# # 1 * 1 2 3
# # 1 2 * 1 2
# # 1 2 3 * 1
# # 1 2 3 4 *

# # (or)

# # n=int(input("n: "))
# # for i in range(n):
# #     val=1
# #     for j in range(n):
# #         if i==j:
# #             print("*",end=' ')
# #             val=1
# #         elif i>j:
# #             print(val,end=' ')
# #             val+=1
# #         else:
# #             print(val,end=' ')
# #             val+=1
# #     print()

# # (or)

# # n=int(input("n: "))
# # for i in range(n):
# #     val=1
# #     for j in range(n):
# #         if i==j:
# #             print("*",end=' ')
# #             val=1
# #         else:
# #             print(val,end=' ')
# #             val+=1
# #     print()
# # 
# n: 5
# # * 1 2 3 4 
# # 1 * 1 2 3
# # 1 2 * 1 2
# # 1 2 3 * 1
# # 1 2 3 4 *

# # n=int(input("n: "))
# # spc=n-1
# # star=1
# # for i in range(n):
# #     for j in range(spc):
# #         print(' ',end=' ')
# #     for k in range(star):
# #         print("*",end=' ')
# #     print()
# #     spc-=1
# #     star+=2

# # n: 5
# #         * 
# #       * * * 
# #     * * * * * 
# #   * * * * * * * 
# # * * * * * * * * * 

# # n=int(input("n: "))
# # spc=n-1
# # star=1
# # val=ord('A')
# # for i in range(n):
# #     for j in range(spc):
# #         print(' ',end=' ')
# #     for k in range(star):
# #         print(chr(val),end=' ')
# #     print()
# #     spc-=1
# #     star+=2
# #     val==1

# # n: 5
# #         A 
# #       A A A 
# #     A A A A A 
# #   A A A A A A A 
# # A A A A A A A A A


# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(n-i-1):
# #         print(' ',end=' ')
# #     for k in range(2*i+1):
# #         print("*",end=' ')
# #     print()
# # n: 5
# #         * 
# #       * * *
# #     * * * * *
# #   * * * * * * *
# # * * * * * * * * *


# # n=int(input("n: "))
# # spc=0
# # str=2*n-1
# # for i in range(n):
# #     for j in range(spc):
# #         print(' ',end=' ')
# #     for k in range(str):
# #         print("*",end=' ')
# #     print()
# #     spc+=1
# #     str-=2
   
# # n: 4
# # * * * * * * * 
# #   * * * * * 
# #     * * * 
# #       *

# # n=int(input("n: "))
# # for i in range(n):
# #     for j in range(i):
# #         print(' ',end=' ')
# #     for k in range(2*(n-i)-1):
# #         print("*",end=' ')
# #     print()
   
# # n: 4
# # * * * * * * * 
# #   * * * * *
# #     * * *
# #       *

# # n=int(input("n: "))
# # for i in range(n-1,-n,-1):
# #     for j in range(n-abs(i)):
# #         print("*",end=' ')
# #     print()


# # n: 3
# # * 
# # * *
# # * * *
# # * *
# # *


# # n=int(input("n: "))
# # for i in range(n-1,-n,-1):
# #     for j in range(abs(i)):
# #         print(' ',end=' ')
# #     for k in range(n-abs(i)):
# #         print("*",end=' ')

# #     print()

# # n: 3
# #     * 
# #   * *
# # * * *
# #   * *
# #     *












# 03-04-2026

# import math as m
# a,b=int(input("a: ")), int(input("b: "))
# print(m.comb(a,b))


# n=int(input('n: '))
# for i in range(n):
#     print("* "*n)
# n: 4
# * * * * 
# * * * * 
# * * * * 
# * * * * 


# n=int(input('n: '))
# val=1
# for i in range(n):
#     print((str(val)+' ')*n)
#     val+=1
# n: 4
# 1 1 1 1 
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# row-wise
# n=int(input('n: '))
# for i in range(n):
#     print((str(val)+' ')*n)
#     val+=1
# n: 4
# 1 1 1 1 
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# n=int(input('n: '))
# for i in range(1,n+1):
#     print('*'*i)
# n: 4
# *
# **
# ***
# ****

# n=int(input('n: '))
# val=1
# for i in range(1,n+1):
#     print((str(val)+' ')*i)
#     val+=1
# 1 
# 2 2
# 3 3 3
# 4 4 4 4

# n=int(input('n: '))
# val=1
# for i in range(1,n+1):
#     print((str(val)+' ')*i)
#     val+=1
#     if val>9:
#         val=1
# n: 10
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9
# 1 1 1 1 1 1 1 1 1 1

# n=int(input('n: '))
# for i in range(n,0,-1):
#     print('*'*i)
# n: 4
# ****
# ***
# **
# *

# n=int(input('n: '))
# for i in range(n):
#     print('* '*(n-i))
# n: 4
# * * * * 
# * * * 
# * * 
# *



# n=int(input('n: '))
# for i in range(1,n+1):
#     print('  '*(n-i)+' *'*i)
# n: 4
#        *
#      * *
#    * * *
#  * * * *

# n=int(input('n: '))
# val=1
# for i in range(1,n+1):
#     print('  '*(n-i)+(str(val)+' ')*i)
# n: 4
#       1 
#     1 1 
#   1 1 1 
# 1 1 1 1

# n=int(input('n: '))
# val=1
# for i in range(1,n+1):
#     print('  '*(n-i)+(str(val)+' ')*i)
#     val+=1
# n: 5
#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5

# n=int(input('n: '))
# val=1
# for i in range(n,0,-1):
#     print('  '*(n-i)+("* "*i))
#     val+=1
# n: 5
# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *

# n=int(input('n: '))
# for i in range(n):
#     print('  '*(n-i-1)+("* ")*(2*i+1))
# n: 4
#       * 
#     * * *
#   * * * * *
# * * * * * * *

# n=int(input('n: '))
# for i in range(n):
#     print('  '*(i)+("* ")*(2*(n-i)-1))
# n: 4
# * * * * * * * 
#   * * * * *
#     * * *
#       *

# (or)

# n=int(input('n: '))
# for i in range(n,0,-1):
#     print('  '*(n-i)+("* ")*(2*i-1))
# n: 4
# * * * * * * * 
#   * * * * *
#     * * *
#       *

# n=int(input('n: '))
# for i in range(n-1,-n,-1):
#     print("* "*(n-abs(i)))
# n: 4
# * 
# * *
# * * *
# * * * *
# * * *
# * *
 # *

# n=int(input('n: '))
# for i in range(n-1,-n,-1):
#     print(' '*(abs(i))+"* "*(n-abs(i)))
# n: 4
#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    * 

# n=int(input('n: '))
# for i in range(n-1,-n,-1):
#     print('  '*(abs(i))+"* "*(n-abs(i)))
# n: 4
#       * 
#     * * 
#   * * * 
# * * * * 
#   * * * 
#     * * 
#       * 


# n=int(input("enter: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     for k in range(i+1):
#         print("*",end=' ')
#     print()
# enter: 4
#       * 
#     * * 
#   * * * 
# * * * *

# pascals program
# n=int(input('n: '))
# for i in range(1,n+1):
#     print(' '*(n-i)+'* '*i)
# n: 4
#     *
#    * *
#   * * *
#  * * * *



# import math
# n=int(input("enter: "))
# for i in range(n):
#     print(" "*(n-i-1),end=' ')
#     for k in range(i+1):
#         print(math.comb(i,k),end=' ')
#     print()
# enter: 4
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1

# enter: 5
#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1 
#  1 4 6 4 1 

#   HOLLOW PATTERN

# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n: 10
# * * * * * * * * * * 
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *


# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1 or i==j:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# * * * * *
# * *     *
# *   *   *
# *     * *
# * * * * *
# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 6
# * * * * * * 
# * *     * *
# *   * *   *
# *   * *   *
# * *     * *
# * * * * * *

'''this code works for odd numbers'''
# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
#     *     
#     *     
# * * * * * 
#     *     
#     *


# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==j:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# *       * 
# * *     * 
# *   *   * 
# *     * * 
# *       * 

# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n//2:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# * * * * * 
#     *     
#     *
#     *
#     *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==n-2:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n: 5
# * * * * * 
# *       *
# *       *
# * * * * *
# *       *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or i+j==n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# * * * * * 
#       *
#     *
#   *
# * * * * *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1 or i+j==n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#     n: 5
# *       * 
#   *   *
#     *
#   *   *
# *       *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(2*n-1):
#         if i==j or i+j==2*n-2 :
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# *               * 
#   *           *   
#     *       *
#       *   *
#         *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(2*n-1):
#         if i==j or i+j==2*n-2 or i==0 :
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# * * * * * * * * * 
#   *           *   
#     *       *     
#       *   *       
#         *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(2*n-1):
#         if i+j==n-1 or j-i==n-1 :
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 6
#           *
#         *   *
#       *       *       
#     *           *     
#   *               *   
# *                   * 

# n=int(input("n: "))
# for i in range(n):
#     for j in range(2*n-1):
#         if i+j==n-1 or j-i==n-1 or i==n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n: 6
#           *
#         *   *
#       *       *
#     *           *
#   *               *
# * * * * * * * * * * *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(2*n-1):
#         if i+j==n-1 or j-i==n-1 or i==j or i+j==2*n-2:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 6
# *         *         * 
#   *     *   *     *
#     * *       * *
#     * *       * *
#   *     *   *     *
# *         *         *

# n=int(input("n: "))
# for i in range(2*n-1):
#     for j in range(n):
#         if i==j or i+j==2*n-2:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# *
#   *
#     *
#       *
#         *
#       *
#     *
#   *
# *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i+j==n-1):
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n: 5
# * * * * * 
# *       *
# *   *   *
# *       *
# * * * * *

'''
* *
*   *
*   *
* *
*
'''

# n=int(input('n: '))
# for i in range(n):
#     print('  '*(n-i-1)+("* ")*(2*i+1))
# for i in range(n):
#     print('  '*(n-i-1)+("* ")*(2*i+1))
# for i in range(n):
#     print('  '*(n-i-1)+("* ")*(2*i+1))


n=int(input('n: '))
for k in range(n):
    for i in range(n):
        print('  '*(n-i-1)+("* ")*(2*i+1))
for j in range(n):
    for l in range(2*j+1):
        if l==0 or l==2*j:
            print(' ',end=' ')
        else:
            print("*",end=' ')
        
