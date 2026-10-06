n = int(input("n: "))
for val in range(1, n+1):
    res = 0
    temp = val
    while val>0:
        rem = val%10
        f=1
        for i in range (1,rem+1):
            f*=i
        res+=f
        val//=10
    if temp==res:
        print(temp)    