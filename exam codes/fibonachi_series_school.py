n = int(input("enter no of terms "))
a = 0
b = 1
s = 0
i = 1
while i <= n:
    s = s+a
    c = c+b
    a = b
    b = c
    i = i + 1

print("sum = ", s)
