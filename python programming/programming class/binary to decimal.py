n = int(input("Enter a number :"))
p = 1
decimal = 0
while n > 0:
    rem =n % 10
    decimal+=rem*p
    n//=10
    p*=2
    print(decimal)