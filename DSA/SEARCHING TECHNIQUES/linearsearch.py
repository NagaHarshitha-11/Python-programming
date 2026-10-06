def Linear_Search(val, l1):
    for i in range(len(l1)):
        if l1[i] == val:
            print(f"{val} value is found ->", i)
            break
    else:
        print("Value not found")


l1 = [1,5,3,4,7,99,5,43,67]
val = int(input("Enter number: "))
Linear_Search(val, l1)