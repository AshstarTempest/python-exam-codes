# sum of series 0 ,1,1,2,3,5,8
last_no = int(input("nth term  : "))
first_term = 0
sum_of_first_3_nos = 2
sum_of_series = 0
a = 2
d = 1

while (last_no-3) >= 1:
    sum_of_series += a
    a += d
    d += 1
    last_no -= 1
print(sum_of_series+sum_of_first_3_nos)
