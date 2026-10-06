''' recursion example '''
# def dolls(n):
#     if n==0:
#         print("All dolls are opened")
#     else:
#         print(f"{n}th doll is opened")
#         dolls(n-1)
# dolls(10)
# 10th doll is opened
# 9th doll is opened
# 8th doll is opened
# 7th doll is opened
# 6th doll is opened
# 5th doll is opened
# 4th doll is opened
# 3th doll is opened
# 2th doll is opened
# 1th doll is opened
# All dolls are opened

'''1.program to find the factorial of given number without using loops? '''
# def fact(n):
#     if n==1:
#         return 1
#     else: 
#         return n*fact(n-1)
# print(fact(6)) #720
# print(fact(5)) #120
# print(fact(3)) #6
# print(fact(10)) #3628800

'''2.program to find sum of first 10 natural numbers'''
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum(n-1)
# print(sum(10))

'''3.sum of given number using recursion'''
# def sum_of_given_number(n):
#     if n == 0:
#         return 0
#     else:
#         return (n%10)+sum_of_given_number(n//10)

# print(sum_of_given_number(5432)) #14
# print(sum_of_given_number(86214))#21
# print(sum_of_given_number(0))#0

'''4.print all the even numbers from 1-10 using recursion'''
# def evens(n):
#     if n<=10:
#         print(n,end=" ")
#         evens(n+2)
# evens(2)
# o/p: 2 4 6 8 10  


'''5.print all the odd numbers from 1-10 using recursion'''
# def odds(n):
#     if n<=10:
#         print(n,end=" ")
#         odds(n+2)
# odds(1)
# o/p: 1 3 5 7 9

'''6.wap to convert decimal to binary using recursion'''
# decimal to binary conversion 

# def dec_to_binary(n):
#     if n==1:
#         return 1
#     else:
#         return str(dec_to_binary(n//2)) + str(n%2) 

# print(dec_to_binary(10))  #1010
# print(dec_to_binary(20))  #10100
# print(dec_to_binary(25))  #11001

# or
# def dec_to_bin(n):
#     if n>1:
#         dec_to_bin(n//2)
#     print(n%2,end=" ")

# dec_to_bin(10)


'''7.find the sum of given list elements using recursion?'''

# def sum_of_list_ele(l):
#     if len(l)==0:
#         return 0
#     return l[0]+sum_of_list_ele(l[1:])
# print(sum_of_list_ele([5,2,1,7,3])) #18

'''8.find the product of given list elements using recursion?'''

# def prod(l):
#     if len(l)==0:
#         return 1
#     return l[0] * prod(l[1:])

# print(prod([5,2,1,7,3])) #210

'''9.wap to reverse the given string using recursion ?'''

# def rev_string(s):
#     if len(s)==0:
#         return ""
#     return s[-1] + rev_string(s[:-1])

# print(rev_string("pyspiders"))  #sredipsyp
# print(rev_string("harshi"))     #ihsrah


'''10wap to check whether the given string is palindrome or not ?'''

def palindrome(s):
    if len(s)==0:
        return "String is palindrome"

    if s[0] != s[-1]:
        return "String is not palindrome"
    
    return palindrome(s[1:-1])

print(palindrome("mam")) #String is palindrome
print(palindrome("cat")) #String is not palindrome

'''ASSIGNMENT 
convert each word character upper case and lower case ?
input: l1=["python","recursion","is","awesome"]
output: [PythoN, RecursioN, IS, AwesomE]'''

# l1=["python","recursion","is","awesome"]
# def change(word,i):
#     if i == len(word):
#         return ""
#     ch=word[]

#     if i==0 or i==len(word)-1:
#         if 'a' <=