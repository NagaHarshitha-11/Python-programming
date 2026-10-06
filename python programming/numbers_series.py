# general series 1,2,3,4,5,6............

# n=int(input("enter n: "))
# for i in range(1,n+1):
#     print(i,end=' ')

# enter n: 10
# 1 2 3 4 5 6 7 8 9 10 

# even series 2,4,6..................
# n=int(input("enter n: "))
# val=2
# for i in range(n):
#     print(val,end=' ')
#     val+=2

# or

# n=int(input("enter n: "))
# for i in range(1,n+1):
#     print(2*i,end=' ')

# enter n: 4
# 2 4 6 8 
# enter n: 3
# 2 4 6

# odd series 1,3,5....................
# n=int(input("enter n: "))
# for i in range(1,n+1):
#     print(2*i-1,end=' ')
# enter n: 4
# 1 3 5 7 

# multiples of 5 ....................
# n=int(input("enter n: "))
# val=5
# for i in range(n):
#     print(val,end=' ')
#     val+=5

# # or

# n=int(input("enter n: "))
# for i in range(1,n+1):
#     print(5*i,end=' ')
# enter n: 5
# 5 10 15 20 25 

# square of the number............
# n=int(input("enter n: "))
# for i in range(1,n+1):
#     print(i**2,end=' ')
# enter n: 5
# 1 4 9 16 25 

# cubing of a number...............
# n=int(input("enter n: "))
# for i in range(1,n+1):
#     print(i**3,end=' ')
# enter n: 5
# 1 8 27 64 125 

# 2,1,4,3,6,5
# n=int(input("enter n:"))
# for i in range(n):
#     if i%2==0:
#         print(i+2,end=' ')
#     else:
#         print(i ,end=' ')
# enter n:6
# 2 1 4 3 6 5 

# Fibanocii series(print n numbers from the series)
# n=int(input("enter n: "))
# a,b=0,1
# for i in range(n):
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c
# enter n: 7
# 0 1 1 2 3 5 8 

# or

# n=int(input("enter n: "))
# a,b=0,1
# for i in range(n):
#     print(a,end=' ')
#     a,b=b,a+b
# enter n: 7
# 0 1 1 2 3 5 8 

# fibanocci series in function
# def finbanocci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=' ')
#         a,b=b,a+b
#     print()
# finbanocci(5)

# 0 1 1 2 3 

# class Number_series:
#     def finbanocci(self,n):
#         a,b=0,1
#         for i in range(n):
#             print(a,end=' ')
#             a,b=b,a+b
#         print()
# obj=Number_series()
# obj.finbanocci(7)

# 0 1 1 2 3 5 8 


# class Number_series:
#     def finbanocci(self,n):
#         a,b=0,1
#         for i in range(n):
#             print(a,end=' ')
#             a,b=b,a+b
#         print()
#     def even(self,n):
#         for i in range(1,n+1):
#             print(2*i,end=' ')
#         print()
#     def odd(self,n):
#         for i in range(1,n+1):
#             print(2*i-1,end=' ')
#         print()

# obj=Number_series()
# obj.finbanocci(7)
# obj.even(6)
# obj.odd(6)

# 0 1 1 2 3 5 8 
# 2 4 6 8 10 12 
# 1 3 5 7 9 11 















