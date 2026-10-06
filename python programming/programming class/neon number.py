#neon number is nothing but if a number is squared and adding the squared we need to get the actual number thats a neon number
n = int(input("n :"))
temp = n**2
sum  = 0
while temp>0:
    sum+=temp%10
    temp//=10
if sum==n:
    print("number is a neon number")
else:
    print("number is not a neon number")