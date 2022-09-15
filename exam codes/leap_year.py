year = int(input("enter a year "))
if year % 100 == 0 and year % 400 != 0:
    print("non leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("non leap year")
