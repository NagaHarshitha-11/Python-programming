# a=int(input("a: "))
# b=int(input("b: "))
# print(f"Before Swapping\n a:{a}\t b:{b}")
# # logic
# a,b=b,a
# print(f"Before Swapping\n a:{a}\t b:{b}")


# # c=a
# # a=b
# # b=c

# # a=a+b
# # b=a-b
# # b=a-b

# # a=a*b
# # b=a//b
# # a=a//b

# # a=a^b
# # b=a^b
# # a=a^b


# print(f"After Swapping\n a:{a}\t b:{b}")


# a,b=1,2,3
# print(a,b)  ValueError: too many values to unpack (expected 2, got 3)

# a=1,2,3
# print(a)    (1, 2, 3)

# l1=[1,2,3]
# a,b=l1
# print(a,b)      ValueError: too many values to unpack (expected 2, got 3)

# l1=[1,2]
# a,b=l1
# print(a,b)     1 2

# l1=[1,2,3,4,5,6]
# a,*b=l1
# print(a,b)          1 [2, 3, 4, 5, 6]

# l1=[1,2,3,4,5,6]
# *a,b=l1
# print(a,b)           [1, 2, 3, 4, 5] 6

# l1=[1]
# a,b=l1 
# print(a,b)     ValueError: not enough values to unpack (expected 2, got 1)


# packing and unpacking 

# 1)packing

# a=12
# b=34
# c=45
# packed=a,b,c
# print(packed)
# print(type(packed))

#2)unpacking

packed=12,34,6
a,b,c=packed
print(a)
print(b)
print(c)


# swap of values using fourth variable
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# print(f"Before Swaping\n a:{a}\t b:{b}\t c:{c}")sdf



# # logic
# d=a
# a=c
# c=b
# b=d

# a=a+b+c
# b=a-(b+c)
# c=a-(b+c)
# a=a-(b+c)

# a=a^b^c
# b=a^b^c
# c=a^b^c
# a=a^b^c

# a=a*b*c
# b=a//(b*c)
# c=a//(b*c)
# a=a//(b*c)

a,b,c=c,a,b
print(f"After Swaping\n a:{a}\t b:{b}\t c:{c}")
