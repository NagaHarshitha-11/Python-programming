'''create a class of you choice when the object is created need to create an empty dictionary automatically.
use a methods like additems(),displayitems(), update and delete.'''

# class Mydictionary:
#     def __init__(self):
#         self.data={}
#     def display(self):
#         print(self.data)
#     def add_items(self,k,v):
#         if k not in self.data:
#             self.data[k]=v
#     def update_items(self,k,v):
#         if k in self.data:
#             self.data[k]=v
#     def delete_items(self,k):
#         if k in self.data:
#             del self.data[k]
            
# m1=Mydictionary()
# m1.add_items('a',10)
# m1.add_items('b',20)
# m1.add_items('c',30)
# m1.add_items('d',40)
# m1.add_items('a',10)
# m1.display()
# m1.update_items('c','programming')
# m1.display()
# m1.delete_items('d')
# m1.display()
# {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# {'a': 10, 'b': 20, 'c': 'programming', 'd': 40}
# {'a': 10, 'b': 20, 'c': 'programming'}


'''create a clss called bank account and it should contains the details like name,address,account_no and account_balance.
create a methods like depoist withdraw and check_balance, ->while performing any functionlities need to check the user is exist or not
->while withdraw check the balance to withdraw the amount ,if there is insufficient balance raise an exception
note: 
1.a user can do only four transactions,if limit s reached display a message(transaction limit has been reached)
2.create four accounts at a same time'''

# class Bank_account:
#     def __init__(self,name,address,account_no,account_balance):
#         self.name=name
#         self.address=address
#         self.account_no=account_no
#         self.account_balance=account_balance
#         self.count=0
#     def deposit(self,amount):
#         if self.count<5:
#             amount=int(input("enter amount that u want to deposit "))
#             self.account_balance+=amount
#             # self.count+=1
#             print("Amount deposited")
#             print(self.account_balance)
#         else:
#             print("Transaction limit reached")
#     def withdraw(self,amount):
#         if self.count<5:
#             amount=int(input("enter how much amount you want to withdraw"))
#             if self.account_balance>=amount:
#                 self.account_balance-=amount
#                 self.count+=1
#                 print("Amount withdrawn")
#                 print(self.account_balance)
#             else:
#                 raise Exception("insufficient balance")
        
#     def check_balance(self):
#         uname=input("Enter the username:")
#         for i in accounts:
#             # print(i)
#             if i.name==uname:
#                 print(f"{i.name} balance is {i.account_balance}")
#                 break
#         else:
#             print("User doesn't exist")
#                 # print("bal",accounts)

# accounts=[
#     Bank_account('harshitha','ymg',56438,1000),
#     Bank_account('chandhu','knl',56434,15000),
#     Bank_account('raju','bnglr',76587,2000),
#     Bank_account('sai','adoni',34256,3000),
#     Bank_account('meghana','ymg',24363,4500)
# ]
# Bank_account.check_balance(Bank_account)
# obj=accounts[0]
# obj.deposit(500)
# obj.withdraw(200)
# obj.check_balance()




'''create a class with name VendingMachine and it should contains some methods like display, additem, updateitems,delete items and the total bill.
when the object is created it should get the dictionary of items along with its price and empty cart need to be created , when we are using add itemss check items are present are not and add the items to its cart with its quantity.
total bill method should display total price of all items in a cart.
'''
# class VendingMachine:
#     def __init__(self,products):
#         self.products=products
#         self.cart={}

#     def display(self):
#         for k,v in self.products.items():
#             print(k, ":" ,v)

#     def add_item(self,name,qty):
#         if name in self.products:
#             self.cart[name]=qty

#     def total_bills(self):
#         total=0
#         for k,v in self.cart.items():
#             print(k ,":", v, "*", self.products[k], "=",v*self.products[k])
#             total+=v*self.products[k]
#         print("------------------------------------")
#         print("Total bill is Rs.",total)

#     def update_item(self,name,qty):
#         if name in self.cart:
#             self.cart[name]=qty
#             print(name,"quantity is updated")
#         else:
#             print("items not found")

#     def del_item(self,name):
#         if name in self.cart:
#             del self.cart[name]
#             print(name,"is deleted")

# products={
#     'cup cake':10,
#     'kitkat':25,
#     'oreo':30,
#     'lays':10,
#     'bingo':30,
#     'cake':60,
#     'chikki':10
    
# }
# vm=VendingMachine(products)
# vm.display()
# print()
# print("Cart items are:")
# vm.add_item('lays',10)
# vm.add_item('oreo',5)
# vm.add_item('cake',10)

# vm.update_item('cake',4)

# vm.del_item('oreo')

# print(vm.cart)
# print()
# vm.total_bills()

# o/p:
# cup cake : 10
# kitkat : 25
# oreo : 30
# lays : 10
# bingo : 30
# cake : 60
# chikki : 10

# Cart items are:
# cake quantity is updated
# oreo is deleted
# {'lays': 10, 'cake': 4}

# lays : 10 * 10 = 100
# cake : 4 * 60 = 240
# ------------------------------------
# Total bill is Rs. 340


'''program to convert the given numeric string to morse code and vice-versa?
morce code dictionary is;
{
'0': '-----',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
}'''


# m_d={
# '0': '-----',
# '1': '.----',
# '2': '..---',
# '3': '...--',
# '4': '....-',
# '5': '.....',
# '6': '-....',
# '7': '--...',
# '8': '---..',
# '9': '----.',
# }

# reverse_morse_code={v:k for k,v in m_d.items()}
# # print(reverse_morse_code)

# def digit_to_morce(nstr):
#     s1=""
#     if nstr.isdigit():
#         for i in nstr:
#             if i in m_d:
#                 s1+=m_d[i]
#     else:
#         return "Invalid input"
#     return s1

# def morce_to_digit(code):
#     res=''
#     for i in code.split():
#         if i in reverse_morse_code:
#             res+=reverse_morse_code[i]
#         else:
#             return "invalid morse code"
#         return res

# print("morse code converter")
# print("1.Numbers to morse code. \n""2.Morse code to numbers")
# options=int(input("Enter the option:"))
# match options:
#     case 1:
#         nstr=input("enter the numeric string:")
#         print(digit_to_morce(nstr))
#     case 2:
#         code=input("enter morse code with 5characters and spaces")
#         print(morce_to_digit(code))
#     case _:
#         print("invalid option")

'''wap to build a functionalities for railway department , it should contains a methods like get_train_name(), get_train_for_the_day() and get_total_price().
consider each train details in the form of dictionary and all the train details in the form of list as follows:'''

# train_details=[{
#     'train_no':6623,
#     'train_name':'Udhyan express',
#     'start':'bnglr',
#     'end':'goa',
#     'days_of_run':['SUN','MON','THU'],
#     'price':{
#         'general':500,
#         'sleeper':1000,
#         'AC':1500
#     }
# },
# {   'train_no':6633,
#     'train_name':'Anjanadri express',
#     'start':'bnglr',
#     'end':'goa',
#     'days_of_run':['MON','THU'],
#     'price':{
#         'general':400,
#         'sleeper':900,
#         'AC':1700
#     }
# },
# {
#     'train_no':6643,
#     'train_name':'delhi express',
#     'start':'bnglr',
#     'end':'goa',
#     'days_of_run':['SUN','MON','THU','SAT'],
#     'price':{
#         'general':300,
#         'sleeper':1100,
#         'AC':1400
#     }
# },
# {   'train_no':6653,
#     'train_name':'karnatak express',
#     'start':'bnglr',
#     'end':'goa',
#     'days_of_run':['SUN','MON'],
#     'price':{
#         'general':200,
#         'sleeper':1200,
#         'AC':1600
#     }
# }
# ]

# class Railway_dept:
#     def get_train_name(self,t_no):
#         for train in train_details:
#             if train['train_no']==t_no:
#                 return train['train_name']
#         return "NO trains available"
#     def get_trains_for_the_day(self,day):
#         alltrains=[]
#         for train in train_details:
#             if day in train['days_of_run']:
#                 alltrains.append(train['train_name'])
#         return alltrains
#     def get_total_price(self,t_no,**kwargs):
#         total=0
#         for train in train_details:
#             if train['train_no']==t_no:
#                 print("General:",train['price']['general'], "*", kwargs['g'],"=",train['price']['general']*kwargs['g'])
#                 print("Sleeper:",train['price']['sleeper'], "*", kwargs['s'],"=",train['price']['sleeper']*kwargs['s'])
#                 print("AC:",train['price']['AC'], "*", kwargs['ac'],"=",train['price']['AC']*kwargs['ac'])

#                 print("----------------------------------")
#                 total+=train['price']['general']*kwargs['g'] + train['price']['sleeper']*kwargs['s'] + train['price']['AC']*kwargs['ac']
#         return total
# rd=Railway_dept()
# print(rd.get_train_name(6623))
# print(rd.get_trains_for_the_day('SUN'))
# print("Total Bill:",rd.get_total_price(6623,g=120,s=80,ac=45))

# o/p:
# Udhyan express
# ['Udhyan express', 'delhi express', 'karnatak express']
# General: 500 * 120 = 60000
# Sleeper: 1000 * 80 = 80000
# AC: 1500 * 45 = 67500
# ----------------------------------
# Total Bill: 207500

'''consider flight details and need to build a functionalities as follows:
methods like generate_tickets(),get_total_price(), search_flights().

generate_ticket() method need to display a ticket numbers as follows, it should contains 
one at the beginning, follwed by three characters from company name, three characters from start point ,four digit random numbers, three characters from destination'''

# import random
# flight_details=[{
#     'Air_lines':'Air India',
#     'f_id':'1Air3265',
#     'start':'bnglr',
#     'end':'hyd',
#     'start time':'',
#     'end time':'',
#     'food':True,
#     'price':5000
# },
# {   'Air_lines':'emarates',
#     'f_id':'2ema6543',
#     'start':'hyd',
#     'end':'chennai',
#     'start time':'',
#     'end time':'',
#     'food':True,
#     'price':4500
# },
# {
#     'Air_lines':'indigo',
#     'f_id':'1ind3475',
#     'start':'bnglr',
#     'end':'mumbai',
#     'start time':'',
#     'end time':'',
#     'food':True,
#     'price':8000
# },
# {
#     'Air_lines':'Quatar Air Lines',
#     'f_id':'1qua3265',
#     'start':'dubai',
#     'end':'singapur',
#     'start time':'',
#     'end time':'',
#     'food':True,
#     'price':5000
# }
# ]

# class Flights:
#     def generate_tickets(self,fno):
#         n=int(input("Enter the total tickets to generate:")) 
#         for i in flight_details:
#             if i['f_id']==fno:
#                 for _ in range(n):
#                     print(str(1)+i['Air_lines'][:3].upper() +i['start'][:3].upper() + str(random.randint(1111,9999)) + i['end'][:3].upper())
#         self.total_price(n,fno)
#     def total_price(self,n,fno):
#         total=0
#         platform_fee=100
#         for i in flight_details:
#             if i['f_id']==fno:
#                 total+=i['price']*n
#         total=platform_fee*n
#         total=total+platform_fee
#         gst=total*18/100
#         total=total+gst

#         print("Total Price:",total)

#     def search_flights(self,fno):
#         for flight in flight_details:
#             if flight['f_id']==fno:
#                 return flight['Air_lines']
#         return "No flights available"


# f=Flights()
# f.generate_tickets('1ind3475')
# print(f.search_flights('1qua3265'))


'''program to display to number of coin denomination based on given total amount and list of coins'''


# def coin_change(amount,coins):
#     N=amount
#     coins.sort()
#     # print(coins)
#     index=len(coins)-1
#     d1={}
#     c=0
#     while True:
#         coinval=coins[index]
#         if N >= coinval:
#             if coinval not in d1:
#                 c+=1
#                 d1[coinval]=1
#             # print(coinval)
#             else:
#                 d1[coinval]+=1
#             N-=coinval
#         if N<coinval:
#             index-=1
#         if N==0:
#             break
#     for k,v in d1.items():
#         print(k, "*", v, '=', k*v)
#     print("Total count",c)

# coins=[10,5,500,20,1,2,200,50,100,1000,2000]
# amount=int(input("enter amount:"))
# coin_change(amount,coins)


# o/p:
# enter amount:7654
# 2000 * 3 = 6000
# 1000 * 1 = 1000
# 500 * 1 = 500
# 100 * 1 = 100
# 50 * 1 = 50
# 2 * 2 = 4


'''program to help den of thieves to robe the houses which they get max amount .
consider a list with both positive and negative values and display output like even number of houses or odd number of houses'''


# List of money in houses
# houses = [10, -5, 20, 15, -2, 30, 5, -4, 12]

# even_sum = 0
# odd_sum = 0

# # Calculate sums
# for i in range(len(houses)):
#     if i % 2 == 0:
#         even_sum += houses[i]
#     else:
#         odd_sum += houses[i]

# print("Even indexed houses amount =", even_sum)
# print("Odd indexed houses amount =", odd_sum)

# # Find maximum
# if even_sum > odd_sum:
#     print("Rob even number of houses")
#     print("Maximum amount =", even_sum)

# elif odd_sum > even_sum:
#     print("Rob odd number of houses")
#     print("Maximum amount =", odd_sum)

# else:
#     print("Both give same amount =", even_sum)

# o/p:
# Even indexed houses amount = 45
# Odd indexed houses amount = 36
# Rob even number of houses
# Maximum amount = 45



'''ACTIVITY SELECTION PROBLEM IN DATASTRUCTURES'''
'''program to solve the maximum tasks based on given start nd end time?
tasks:      A1 A2 A3 A4 A5 A6
start_time: 0  3  1  5  5  8
end_time:   6  4  2  8  7  9
# O/P: A1 A6

after sorting:
tasks:      A3 A2 A1 A5 A4 A6
start_time  1  3  0  5  5  8
end_time:   2  4  6  7  8  9
O/P:A3 A2 A5 A6'''

# tasks=[
#     ['A1',0,6],
#     ['A2',3,4],
#     ['A3',1,2],
#     ['A4',5,8],
#     ['A5',5,7],
#     ['A6',8,9],
# ]

# def activity(tasks):
#     print(tasks)
#     print()
#     tasks.sort(key=lambda x:x[2])
#     print(tasks)

#     i=0
#     print(tasks[i][0])
#     for j in range(len(tasks)):
#         if tasks[j][1]>=tasks[i][2]:
#             print(tasks[j][0])
#             i=j
# activity(tasks)

# o/p:
# [['A1', 0, 6], ['A2', 3, 4], ['A3', 1, 2], ['A4', 5, 8], ['A5', 5, 7], ['A6', 8, 9]]

# [['A3', 1, 2], ['A2', 3, 4], ['A1', 0, 6], ['A5', 5, 7], ['A4', 5, 8], ['A6', 8, 9]]
# A3
# A2
# A5
# A6

'''check the given paranthesis is balanced or not?'''

# def balanced_paranthesis(p):
#     stack = []
#     values={ ']':'[', ')':'(','}':'{'}
#     for ch in p:
#         if ch in "({[":
#             stack.append(ch)
#         elif ch in ")}]":
#             if not stack or stack.pop()!= values[ch]:
#                 return False
#     return len(stack) == 0

# p=input("Enter paranthesis: ")

# if balanced_paranthesis(p):
#     print("Balanced")
# else:
#     print("Not Blanced")
# o/p:
# Enter paranthesis: [[[())]]]
# Not Blanced

# Enter paranthesis: ((({})))
# Balanced


'''sliding window sum problems'''
# l = [1,5,3,0,7,2,6,4,9]
# k = 3
# res = []

# sum = sum(l[:k])
# # print(sum)
# res.append(sum)

# for i in range(k, len(l)):
#     sum = sum - l[i-k] + l[i]
#     res.append(sum)

# print(res)

# o/p: [9, 8, 10, 9, 15, 12, 19]

'''display the sub list given window size and print max value giving the sublist.'''

# Maximum sum sublist using sliding window

l = [1, 5, 3, 0, 7, 2, 6, 4, 9]
window = 3

max_sum = 0
max_sublist = []

for i in range(len(l) - window + 1):
    sub_list = l[i:i + window]
    current_sum = sum(sub_list)

    print("Sub List:", sub_list, " Sum:", current_sum)

    if current_sum > max_sum:
        max_sum = current_sum
        max_sublist = sub_list

print("\nMaximum Sum Sublist:", max_sublist)
print("Maximum Sum:", max_sum)

# o/p:
# Sub List: [1, 5, 3]  Sum: 9
# Sub List: [5, 3, 0]  Sum: 8
# Sub List: [3, 0, 7]  Sum: 10
# Sub List: [0, 7, 2]  Sum: 9
# Sub List: [7, 2, 6]  Sum: 15
# Sub List: [2, 6, 4]  Sum: 12
# Sub List: [6, 4, 9]  Sum: 19

# Maximum Sum Sublist: [6, 4, 9]
# Maximum Sum: 19