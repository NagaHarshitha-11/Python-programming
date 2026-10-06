# sum of 1 to n elements
# n=int(input())
# res=0
# for i in range(1,n+1):
#     res+=i
# print(res)
# o/p:
# 5
# 15

# or

# def sum_1_to_n(n):
#     res=0
#     for i in range(1,n+1):
#         res+=i
#     return res
# print(sum_1_to_n(6))  #21

# or

# class logical:
#     def sum_1_to_n(self,n):
#         res=0
#         for i in range(1,n+1):
#             res+=i
#         return res
# obj=logical()
# print(obj.sum_1_to_n(7))   #28



# 2. factorial of n 
# n=int(input())
# res=1
# for i in range(1,n+1):
#     res*=i
# print(res)
# 5
# 120


# class logical:
#     def sum_1_to_n(self,n):
#         res=0
#         for i in range(1,n+1):
#             res+=i
#         return res
#     def factorial(self,n):
#         res=1
#         for i in range(1,n+1):
#             res*=i
#         return res
#     def factors(self,n):
#         for i in range(1,n+1):
#             if n%i==0:
#                 print(i,end=' ')
#     def count_factors(n):
#         c=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 c+=1
#         return c


# obj=logical()
# # print(obj.sum_1_to_n(7))
# # print(obj.factorial(4))    #24
# obj.factors(15)   #1 3 5 15
# obj.count_factors()


#3. factors of 1 to n
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=' ')
# 10
# 1 2 5 10 

# def factors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=' ')
# factors(15)   #1 3 5 15

# 4.count of factors
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         # print(i,end=' ')
#         c+=1
# print(c)


#5.prime numbers

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(f'{n} is prime no')
else:
    print(f'{n} is not prime no')

# 7
# 7 is prime no

# or

# n=int(input())
# c=0
# loop_count=0
# for i in range(1,n+1):
#     loop_count+=1
#     if n%i==0:
#         # print(i,end=' ')
#         c+=1
# if c==2:
#     print(f'{n} is prime no')
# else:
#     print(f'{n} is not prime no')
# print(loop_count)

# 10
# # 10 is not prime no
# 10  #it tells how many time loop is running



# n=int(input())
# c=0
# loop_count=0
# for i in range(2,n//2+1):
#     loop_count+=1
#     if n%i==0:
#         c+=1
#         break
# if c==0:
#     print(f'{n} is prime no')
# else:
#     print(f'{n} is not prime no')
# print(loop_count)
# 10
# 10 is prime no
# 4  #optimized toabove code for loop count


# 100000000000000000000
# 100000000000000000000 is not prime no
# 1

# def isprime(n):
#     c=0
#     for i in range(2,n//2+1):
#         if n%i==0:
#             c+=1
#             break
#     if c==0:
#         return True
#     return False
# print(isprime(9)) #False
# print(isprime(71)) #True
# print(isprime(-1))

# class logical:
#     def isprime(n):
#         c=0
#         for i in range(2,n//2+1):
#             if n%i==0:
#                 c+=1
#                 break
#         return c==0
# obj=logical()
# obj.isprime()


# #count of digits
# n=int(input())
# n=abs(n)
# c=0
# while n>0:
#     c+=1
#     n//=10
# print(c)



# #to reverse the number 
# n=int(input())
# temp=n
# n=abs(n)
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n//=10
# print(rev if temp>0 else -rev)
# # rev=0
# # while n>0:
# #     res=n%10
# #     rev=rev*10+res
# #     n//=10
# # print(rev)


# #count of even,odd and zeros
# n=int(input()) 
# zero=0
# even=0
# odd=0
# while n>0:
#     res=n%10
#     if res==0:
#         zero+=1
#     elif res%2==0:
#         even+=1
#     else :
#         odd+=1
#     n//=10
# print("zeros: ",zero)
# print("even no: ",even)
# print("odd no: ",odd)

            
# #sum of even numbers
# # n=int(input()) 
# # even=0
# # sum=0
# # while n>0:
# #     res=n%10
# #     if res%2==0:
# #         even+=1
# #         sum+=res
# #     n//=10
# # print(sum)

# #sum of odd number
# n=int(input())
# sum=0
# while n>0:
#     res=n%10
#     if res%2==1:
#         sum+=res
#     n//=10
# print(sum)


# #finding the lowest number
# n=int(input("Enter n: "))
# a=9
# while n>0:
#     res=n%10
#     if res<a:
#         a=res
#     n//=10

# print(a)

# n=int(input("Enter n: "))
# max=0
# while n>0:
#     res=n%10
# if res>n:
#     res=max
#     n//=10
# print(max)



# ARMSTRONG NUMBER

# n=int(input("n: "))
# temp=n
# sum=0
# p=len(str(n))
# while n>0:
#     rem=n%10
#     sum+=rem**p
#     n//=10
# if temp==sum:
#     print(temp)
# n: 153
# 153


# n=int(input("n: "))
# for i in range(1,n+1):
#     temp=i
#     sum=0
#     p=len(str(i))
    # while i>0:
    #     rem=i%10
    #     sum+=rem**p
    #     i//=10
#     if temp==sum:
#         print(temp)
# n: 1000
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407


# count n number of armstrong numbers
# n=int(input("n: "))
# count=0
# for i in range(1,n+1):
#     temp=i
#     sum=0
#     p=len(str(i))
#     while temp>0:
#         rem=temp%10
#         sum+=rem**p
#         temp//=10
#     if sum==i:
#         print(i)
#         count+=1
# print()
# print(count)


# n=int(input("n: "))
# count=0
# for i in range(1,n+1):
#     temp=i
#     sum=0
#     p=len(str(i))
#     while temp>0:
#         rem=i%10
#         sum+=rem**p
#         i//=10
#     if temp==i:
#         # print(i)
#         count+=1
# # print()
# print(count)
















# strong number
# n=int(input("n:"))
# res=0
# tem=n
# while n>0:
#     rem=n%10
#     f=1
#     for i in range(1,rem+1):   
#         f*=i
#     res+=f
#     n//=10
# print("strong number" if tem==res else "not a strong number")  

# output:
# n:145
# strong number

# n:123
# not a strong number

# n=int(input("n:"))
# for val in range(1,n+1):   
#     res=0
#     temp=val
#     while val>0:
#       rem=val%10
#       f=1
#       for i in range(1,rem+1):
#           f*=1
#       res+=f
#       val//=10
#     if temp==res:
#         print(temp)



'''CONVERSIONS'''
# decimal to binary conversion 
# n=int(input())
# b=""
# while n>0:
#     rem=n%2
#     b=str(rem)+b
#     n=n//2
# print(b)
# 10
# 1010

# or

# n=int(input())
# b=0
# p=1
# while n>0:
#     rem=n%2
#     b=b+rem*p
#     n=n//2
#     p*=10
# print(b)

# binary to decimal conversion
# here p is a bit value
# n=int(input())
# decimal=0
# p=1
# while n>0:
#     rem=n%10
#     decimal=decimal+rem*p
#     n=n//10
#     p*=2
# print(decimal)
# 1111
# 15

# decimal to octal conversion
# n=int(input())
# octal=0
# p=1
# while n>0:
#     rem=n%8
#     octal=octal+rem*p
#     n=n//8
#     p*=10
# print(octal)

124
174

# octal to decimal conversion
# n=int(input())
# octal=0
# p=1
# while n>0:
#     rem=n%10
#     octal=octal+rem*p
#     n=n//10
#     p*=8
# print(octal)


# decimal to hexa-decimal
# hexa-decimal to decimal
# decimal to roman



class string:
    def __init__(self,name,age):
        self.name = name
        self.age=age


    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"
obj=string("john",34)
print(obj)