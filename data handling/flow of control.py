# a = int(input("Enter a no "))
# if a % 2 == 0:
#     print(a, "is even")
# else:
#     print(a, "odd no ")


# x = float(input("Enter a no "))
# y = float(input("Enter a no "))
# z = float(input("Enter a no "))
# if x > y and x > z:
#     print(x, "is greatest ")
# elif y > z and y > x:
#     print(y, "is greatest ")
# elif z > y and z > x:
#     print(z, "is greatest ")


x = float(input("Enter a no "))
y = float(input("Enter a no "))
z = float(input("Enter a no "))
sum1 = x + y + z
if x == y and x == z:
    print(sum1, 0)
elif x == y:
    print(sum1, z)
elif z == y:
    print(sum1, x)
elif x == z:
    print(sum1, y)
else:
    print(sum1)
