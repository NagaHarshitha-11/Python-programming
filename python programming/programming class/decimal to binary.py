n=int(input("Enter a number :"))
binary=0
pos=1
while n>0:
    rem=n%2
    binary+=rem*p
    n//=2
    p*=10
print(binary)    