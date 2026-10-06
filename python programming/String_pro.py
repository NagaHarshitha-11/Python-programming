'''ANAGRAM STRING:
DEFINITION:
length must be same and same type of characters present in a given string.'''

# def bubble_sort(s):
#     l1=list(s)
#     for i in range(len(l1)):
#         for j in range(i+1,len(l1)):
#             if l1[i]>l1[j]:
#                 l1[i],l1[j]=l1[j],l1[i]
#     return "".join(l1)
# s1=input("S1:")
# s2=input("S2:")
# if bubble_sort(s1)==bubble_sort(s2):
#     print("Anagram String")
# else:
#     print("Not an anagram strings")

# output:
# S1:silent
# S2:listen
# Anagram String

# S1:good
# S2:bad
# Not an anagram strings

# S1:good      
# S2:food
# Not an anagram strings


'''PANAGRM STRING:
DEFINITION: 
A sentence should contain all the 26 letters either they should be in upper or lower alphabets (not a problem with duplicates )'''

# s=input("enter any sentence which is having all the 26 letter (either the sentenc is completely upper or completely lower case):")
# res=set()
# for i in s:
#     if i==" ":
#         continue
#     elif i not in res:
#         res.add(i.lower())
# if len(res)==26:
#     print("Panagram")
# else:
#     print("Not a panagram String")

# output:
# enter any sentence which is having all the 26 letter (either the sentenc is completely upper or completely lower case):the quick brown fax jumps over a lazy dog
# Panagram

# enter any sentence which is having all the 26 letter (either the sentenc is completely upper or completely lower case):the quick brown fox jumps over the dog
# Not a panagram String


'''3.String in the pattern format'''
# s1=input("enter any string: ")
# if len(s1)%2!=0:
#     for i in range(len(s1)):
#         for j in range(len(s1)):
#             if i==len(s1)//2:
#                 print(s1[j],end=' ')
#             elif j==len(s1)//2:
#                 print(s1[i],end=' ')
#             else:
#                 print(' ',end=' ')
#         print()
# else:
#     print("Not output")

# outpt:
'''enter any string: pyspi
    p     
    y     
p y s p i 
    p     
    i  '''   

'''4.String in the form of pyramid'''
# s1='pyTHOn'
# n=8
# val=0
# for i in range(1,n):
#     for j in range(1,n-i):
#         print('-',end=' ')

#     for k in range(1,i*2):
#         print(s1[val],end=' ')
#         val+=1
#         if val>=len(s1):
#             val=0
#     print()
# # output:
# - - - - - - p 
# - - - - - y T H 
# - - - - O n p y T 
# - - - H O n p y T H 
# - - O n p y T H O n p 
# - y T H O n p y T H O n 
# p y T H O n p y T H O n p

'''5.program to count total number of special characters in each word of a given string, if the length is even reverse the word in the same place or add the remaining word without any reverse '''

# s1="Hey!@#$ chandh$%^&^ how*&^%$# are^%$ ou^&#@!"

# s2=s1.split()
# print(s2)
# print()
# s3=""
# for i in s2:
#     cnt=0
#     # print(i)
#     for  j in i:
#         if ord(j)>=65 and ord(j)<=90 or ord(j)>97 and ord(j)<=122:
#             continue
#         else:
#             cnt+=1
#     if cnt%2==0:
#         s3+=i[::-1]+' '
#     else:
#         s3+=i+' '
# print(s3)

# print(i ,"->",cnt)


'''program to divide the given string for total number of characters based on square root of total length of a given string excluding spce character?'''

# import math
# s1="making money is a skill, maintaining money is discipline ,multiplying money is art, so plan it accordingly from now you need to work for money for next 20 years and then your money should work for you"

# # n=int(input("n:"))
# cnt=0
# for i in s1:
#     if i==' ':
#         continue
#     else:
#         cnt+=1
# print(cnt)
# div=round(math.sqrt(cnt))
# print(div)
# s2=""
# v=0
# for i in s1:
#     if v==div:
#         s2+='\n'
#         v=0
#     s2+=i
#     v+=1
# print(s2)


# output:
# making money 
# is a skill, m
# aintaining mo
# ney is discip
# line ,multipl
# ying money is
#  art, so plan
#  it according
# ly from now y
# ou need to wo
# rk for money 
# for next 20 y
# ears and then
#  your money s
# hould work fo
# r you


'''program to check the given string can become a mirror string or not?'''

# def is_mirror(s1):"
#     mirror_char={'A','H','I','M','O','T','U','V','W','X','Y','v','o','w','x','0','8'}
#     for i in s1:
#         if i not in mirror_char:
#             return False
#     return True
# s1=input("Enter any string:")
# if is_mirror(s1):
#     print("Mirror String")
# else:
#     print("Not a "mirror string")
# O/P:
# Enter any string:mam
# Not a mirror string

# Enter any string:MAM
# Mirror String

# Enter any string:aha
# Not a mirror string

# Enter any string:AHA
# Mirror String



'''program to display the word indesex as a value? '''
# s1="if you always do what you always did you will always get what you always got"

# res={}
# s2=s1.split()

# for i in  range(len(s2)):
#     if s2[i] not in res:
#         res[s2[i]]=[i]
#     else:
#         res[s2[i]]+=[i]
# print(res)
# o/p:
# {'if': [0], 'you': [1, 5, 8, 13], 'always': [2, 6, 10, 14], 'do': [3], 'what': [4, 12], 'did': [7], 'will': [9], 'get': [11], 'got': [15]}


'''program to find the vowels and consonents in each word present in string?'''
# s1="once the most violent man called one man the most violent"
# d1={}
# vow='aeiouAEIOU'
# for i in s1.split():
#     v,c=0,0
#     for j in i:
#         if j in vow:
#             v+=1
#         else:
#             c+=1
#     if i not in d1:
#         d1[i]=[v,c]
# # print(d1)
# for i in d1:
#     print(i,d1[i])
# o/p:
# once [2, 2]
# the [1, 2]
# most [1, 3]
# violent [3, 4]
# man [1, 2]
# called [2, 4]
# one [2, 1]

'''wap to check the given input can become password or not.
it should contains minimum of 8 characters less than 30 characters  and it should contains one numeric,one lower case, one upper case and one special characters'''

# s1=input("enter the password: ")
# num=0
# lc=0
# uc=0
# sc=0
# if len(s1)>=8 and len(s1)<=30:
#     for i in range(len(s1)):
#         if ord(s1[i])>=65 and ord(s1[i])<=90:
#             uc+=1
#         elif ord(s1[i])>=97 and ord(s1[i])<=122:
#             lc+=1
#         elif ord(s1[i])>=48 and ord(s1[i])<=57:
#             num+=1
#         else:
#             sc+=1
#     if uc>=1 and lc>=1 and num>=1 and sc>=1:
#         print("valid password")
#     else:
#         print("invald password")
# else:
#     print("password must contain atleast 8 chracters")

# enter the password: Harshitha@11
# valid password

# enter the password: harshitha@11
# invald password

# enter the password: Harshitha11
# invald password

# enter the password: Harshitha@
# invald password


'''convert the given input into encryption format using below conditions
1.if length of a string is even check each characters asci value and if that asci value is even add +2 to it and convert that to asci character again,
if asci value is odd add +4 to it and again convert that to asci character

2. if length of a string is odd check each characters asci value and if that asci value is even add +3 to it and convert that to asci character again,
if asci value is odd add +5 to it and again convert that to asci character '''

# s1=input("enter any string: ")
# s2=""
# if len(s1)%2==0:
#     for i in s1:
#         if ord(i)%2==0:
#             s2+=chr(ord(i)+2)
#         else:
#             s2+=chr(ord(i)+4)
# else:
#     for i in s1:
#         if ord(i)%2==0:
#             s2+=chr(ord(i)+3)
#         else:
#             s2+=chr(ord(i)+5)
# print(s2)

# o/p:
# enter any string: AbcD(# even length)
# EdgF

# enter any string: AbcDe(odd length)
# FehGj

'''scissors sciphor encryption -> assignment'''

# s1=input("enter any string: ")
# s2=""
# if len(s1)%2==0:
#     for i in s1:
#         if ord(i)%2==0:
#             s2+=chr(ord(i)+2)
#         else:
#             s2+=chr(ord(i)+4)
# else:
#     for i in s1:
#         if ord(i)%2==0:
#             s2+=chr(ord(i)+3)
#         else:
#             s2+=chr(ord(i)+5)
# print(s2)










'''camel case to snake case program'''
# s1='she saw a kitten eating chicken in the kitchen'
# print(s1)
# print()
# s2=""
# for word in s1.split():
#     for i in range(len(word)):
#         if i==0 or i==len(word)-1:
#             s2+=word[i].upper()
#         else:
#             s2+=word[i]
#     s2+=" "
# print(s2)

# o/p:
# she saw a kitten eating chicken in the kitchen

# ShE SaW A KitteN EatinG ChickeN IN ThE KitcheN 

'''accept two inputs string and an integer, the integer must be single digit and above 2(2,3,....9)
then display the characters from the given string which ascii value is completely divisible by given input'''

# s1='Supercalifragilisticexpiladocious'
# n=int(input("enter integer value b/w 2 to 9: "))

# s2=" "
# if n>=2 and n<=9:
#     for i in s1:
#         if ord(i)%n==0:
#             print(i,end=' ')
# else:
#     print("no output")

# enter integer value b/w 2 to 9: 4
# p l l t x p l d 
    

'''wap to compress the given string as follows:'''
# s1='aaabbcccccdddeeeeeeef'
# s1='aaabbcccccdddeeeeeeefaaaa'
# s2=" "
# for i in s1:
#     cnt=0
#     for j in s1:
#         if i==j:
#             cnt+=1  
#     if i not in s2:
#         s2+=i+str(cnt)
# print(s2)
# o/p: a3b2c5d3e7f1
# o/p: a7b2c5d3e7f1   
    

'''display a pair of first non repeating character along with it index?'''

# s1=input("enter any 'string: ")

# for i in range(len(s1)):
#     if s1.count(s1[i])==1:
#         print((s1[i],i))
#         break
# else:
#     print("no repeating' characters present in the string ")

# o/p: enter any string: breakingbad
# r 1

# enter any string: programming
# ('p', 0)

# enter any string: aabbfffff
# no repeating characters present in the string 


'''rearrange the string by the given string'''
# s1='Hide@ ThE#2 DeadBody'
# uc,lc,num,space,sc,="","","","",""
# for i in s1:
#     if ord(i)>=65 and ord(i)<=91:
#         uc+=i
#     elif ord(i)>=97 and ord(i)<=122:
#         lc+=i
#     elif ord(i)>=48 and ord(i)<=57:
#         num+=i
#     elif i==" ":
#         space+=i
#     else:
#         sc+=i
# # s2=" "+uc+lc+num+space+sc
# # print(s2)
    
# l=[[uc],[lc],[num],[sc]]
# print(l)
    
#o/p: [['HTEDB'], ['ideheadody'], ['2'], ['@#']]

'''program to display nth left rotation of a given string?'''

# s='python'
# n=int(input("enter the number of rotations"))

# n=n%len(s)
# res=s[n:]+s[:n]
# print(res)


'''condtion: take the input as two digit character and lessthan four digit character'''


s='python'
n=int(input("enter the number of rotations"))
for i in range(len(s)):
    res=s[i:]+s[:i]
print(res)