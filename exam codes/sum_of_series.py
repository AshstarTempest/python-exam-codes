# sum till n factorial
a = int(input("enter last no "))
factorial = 1
while a != 0:
    factorial *= a

    a -= 1
print(factorial)
