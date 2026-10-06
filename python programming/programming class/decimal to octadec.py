n = int(input("Enter a number :"))
octal=0
p =1
while n>0:
    rem = n%8
    octal=rem*p
print(octal)
