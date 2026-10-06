# the number which has factors and add the factors if we get the same value except that number thats a perfect number
n = int(input("n :"))
res = 0
for i in range(1,n//2+1):
    if n%i==0:
        res+=i
if res==n:
    print("number is a perfect")
else:
    print("number is not a perfect")