n = int(input("n :"))
for val in range(1,n+1):
    res = 0
    for i in range(1,val//2+1):
        if val%i==0:
            res+=i
    if res==val:
        print(val,end=" ")