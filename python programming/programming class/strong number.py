n = int(input("n: "))
res = 0
temp = n
while n>0:
    rem = n%10
    f=1
    for i in range (1,rem+1):
        f*=i
    res+=f
    n//=10
    if temp==res:
        print("strong number")
    else:
        print("not a strong number")
